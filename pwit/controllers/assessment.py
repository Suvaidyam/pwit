import frappe
from frappe.model.docstatus import DocStatus

class AssessmentAPIs:
    def question_list(doctype):
        assessments = frappe.get_all(doctype, fields=['*'])
        return {'code': 200, 'data': assessments}

    def get_results(doctype,session,user=None):
        assessments = []
        if not user:
            assessments = frappe.get_all(doctype,filters={'session':session,'docstatus':DocStatus.submitted()}, fields=['*'],order_by='creation desc', limit_page_length=1)
        else:
            all_session = frappe.get_all('Session', {'user': user}, pluck='name',order_by='creation desc')
            if len(all_session):
                assessments = frappe.get_all(doctype,filters={'session':["IN", all_session],'docstatus':DocStatus.submitted()}, fields=['*'],order_by='creation desc', limit_page_length=1)
        if len(assessments) > 0:
            assessment = assessments[0]
            meta = frappe.get_meta(doctype)
            if not meta:
                return {'code': 404, 'message': 'Meta not found'}
            option_fields = [field.fieldname for field in meta.fields if (field.fieldtype == 'Link' and field.options == 'Field Options')]
            options = frappe.db.get_list('Field Options', 
                filters={
                    'ref_doctype':doctype, 
                    'field':["IN", option_fields]
                }, 
                fields=['name','field','score'],ignore_permissions=True
            )
            data = {}
            for option in options:
                if assessment[option.field] == option.name:
                    data[option.field] = option.score
            return {'code': 200, 'data': data}
        else:
            return {'code': 200, 'data': {}}
        
    def get_assistive_result(doctype,session,user=None):
        assessments = []
        fields = []
        current_section = None
        meta = frappe.get_meta(doctype)
        for field in meta.fields: 
            if field.fieldtype == 'Section Break':
                current_section = field.label
            elif (field.fieldtype in ['Table MultiSelect', 'Link']) and field.hidden == 0:
                field_label_with_section = f"{current_section} - {field.label}" if current_section else field.label
                fields.append({
                    'fieldname': field.fieldname,
                    'label': field_label_with_section,
                    'fieldtype': field.fieldtype,
                    'short_name': field.get('short_name',None)
                })
        if not user:
            assessments = frappe.get_all(doctype,filters={'session':session,'docstatus':DocStatus.submitted()}, fields=['*'],order_by='creation desc', limit_page_length=1)
        else:
            all_session = frappe.get_all('Session', {'user': user}, pluck='name',order_by='creation desc')
            if len(all_session):
                assessments = frappe.get_all(doctype,filters={'session':["IN", all_session],'docstatus':DocStatus.submitted()}, fields=['*'],order_by='creation desc', limit_page_length=1)
        average=0
        data = {}
        details = {}
        group = {}
        if len(assessments) > 0:
            assessment = assessments[0]
            for field in fields:
                if field['fieldtype'] == 'Link':
                    options = frappe.db.get_list('Field Options', 
                        filters={
                            'ref_doctype':doctype, 
                            'field':field['fieldname']
                        }, 
                        fields=['name','field','score'],ignore_permissions=True
                    )
                    for option in options:
                        if assessment[field['fieldname']] == option.name:
                            data[field['short_name']] = option.score
                elif field['fieldtype'] == 'Table MultiSelect':
                    field_options = frappe.db.get_list('Options Child', 
                        filters={
                            'parent': assessment.name,
                            'parentfield': field['fieldname']
                        }, 
                        pluck='field_options',ignore_permissions=True
                    )
                    options = frappe.db.get_list('Field Options', 
                        filters={
                            'ref_doctype': doctype, 
                            'name':["IN", field_options]
                        }, 
                        fields=['name','field','score'],ignore_permissions=True
                    )
                    for option in options:
                        if option.name in field_options:
                            data[field['short_name']] += option.score
            average = round(sum(data.values()) / len(data),1)
            
            if doctype:
               details = AssessmentAPIs.get_assistive_results_details(doctype)
               group = AssessmentAPIs.get_section_by_result(doctype,session,user)
        return {'code': 200, 'data': {"average":average,"result":data,'details':details,'group':group}}

    def get_assistive_results_details(doctype):
        name = frappe.get_all('Results and Recommendtions', filters={'ref_doctype': doctype}, pluck='name')
        if len(name):
           return frappe.get_doc('Results and Recommendtions', name[0])

    def get_last_draft():
        user = frappe.session.user

        if not user:
            return {'code': 404, 'message': 'User not found'}
        session = frappe.get_all('Session', {'user': user}, pluck='name',order_by='creation desc' ,limit_page_length=1)
        if len(session):
            myp = frappe.get_all('Multi-year Partnerships', filters={'session': session[0]}, fields=['creation'],order_by='creation desc', limit_page_length=1)
            core_costs = frappe.get_all('Core Costs', filters={'session': session[0]}, fields=['creation'],order_by='creation desc', limit_page_length=1)
            dei = frappe.get_all('Diversity Equity Inclusion', filters={'session': session[0]}, fields=['creation'],order_by='creation desc', limit_page_length=1)
            od = frappe.get_all('Organization Development', filters={'session': session[0]}, fields=['creation'],order_by='creation desc', limit_page_length=1)
            fr = frappe.get_all('Financial Resilience', filters={'session': session[0]}, fields=['creation'],order_by='creation desc', limit_page_length=1)
            # Consolidate all results into a single list with labels
            all_draft = [
                {"doctype": "Multi-year Partnerships",'route':'multi-year-partnerships', "creation": myp[0]['creation']} if myp else None,
                {"doctype": "Core Costs" ,'route':'core-costs', "creation": core_costs[0]['creation']} if core_costs else None,
                {"doctype": "Diversity Equity Inclusion" ,'route':'diversity-equity-inclusion', "creation": dei[0]['creation']} if dei else None,
                {"doctype": "Organization Development" ,'route':'organization-development', "creation": od[0]['creation']} if od else None,
                {"doctype": "Financial Resilience" ,'route':'financial-resilience', "creation": fr[0]['creation']} if fr else None
            ]

            # Filter out None entries
            all_draft = [entry for entry in all_draft if entry is not None]

            # Find the latest creation
            if all_draft:
                latest_entry = max(all_draft, key=lambda x: x['creation'])
                return {'code': 200, 'data': latest_entry}
            else:
                return {'code': 404, 'message': 'No draft found'}

    def get_section_by_result(doctype,session,user=None):
        assessments = [] 
        meta = frappe.get_meta(doctype)
        if not user:
            assessments = frappe.get_all(doctype,filters={'session':session,'docstatus':DocStatus.submitted()}, fields=['*'],order_by='creation desc', limit_page_length=1)
        else:
            all_session = frappe.get_all('Session', {'user': user}, pluck='name',order_by='creation desc')
            if len(all_session):
                assessments = frappe.get_all(doctype,filters={'session':["IN", all_session],'docstatus':DocStatus.submitted()}, fields=['*'],order_by='creation desc', limit_page_length=1)
        data = {}
        if len(assessments) > 0:
            assessment = assessments[0]
            final_fields = {}
            sf = None   

            for field in meta.fields:
                if field.fieldtype == "Section Break":
                    sf = field.fieldname
                    final_fields[sf] = []  
                elif field.fieldtype in ["Link", "Table MultiSelect"] and field.options in ["Field Options", "Options Child"]:
                    if sf:
                        final_fields[sf].append(field)  # Add field to the section if sf is set
            data = {}
            # Calculate scores
            for section, fields in final_fields.items():
                section_field = next((field for field in meta.fields if field.fieldname == section), None)
                data[section_field.label] = 0
                table_fields = list(filter(lambda field: field.get('fieldtype') == 'Table MultiSelect', fields))
                link_fields = list(filter(lambda field: field.get('fieldtype') == 'Link' and field.get('hidden') == 0, fields))
                if len(link_fields):
                    options = frappe.db.get_list(
                        'Field Options',
                        filters={
                            'ref_doctype': doctype,
                            'field': ["IN", [field.fieldname for field in link_fields]]
                        },
                        fields=['name', 'field', 'score'],
                        ignore_permissions=True
                    )
                    for option in options:
                        if assessment.get(option.field) == option.name:
                            data[section_field.label] += round(option.score/len(link_fields),1)
                if len(table_fields):
                    for field in table_fields:
                        field_options = frappe.db.get_list(
                            'Options Child',
                            filters={
                                'parent': assessment.name,
                                'parentfield': field.get('fieldname')
                            },
                            pluck='field_options',
                            ignore_permissions=True
                        )
                        options = frappe.db.get_list(
                            'Field Options',
                            filters={
                                'ref_doctype': doctype,
                                'name': ["IN", field_options]
                            },
                            fields=['name', 'field', 'score'],
                            ignore_permissions=True
                        )
                        for option in options:
                            data[section_field.label] += round(option.score/len(table_fields),1)
            return data