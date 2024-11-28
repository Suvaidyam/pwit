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
                    'fieldtype': field.fieldtype
                })
        if not user:
            assessments = frappe.get_all(doctype,filters={'session':session,'docstatus':DocStatus.submitted()}, fields=['*'],order_by='creation desc', limit_page_length=1)
        else:
            all_session = frappe.get_all('Session', {'user': user}, pluck='name',order_by='creation desc')
            if len(all_session):
                assessments = frappe.get_all(doctype,filters={'session':["IN", all_session],'docstatus':DocStatus.submitted()}, fields=['*'],order_by='creation desc', limit_page_length=1)
        if len(assessments) > 0:
            assessment = assessments[0]
            data = {}
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
                            data[field['label']] = option.score
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
                            data[field['label']] += option.score
            average = round(sum(data.values()) / len(data),1)
            details = {}
            if doctype:
               details = AssessmentAPIs.get_assistive_results_details(doctype)
        return {'code': 200, 'data': {"average":average,"result":data,'details':details}}

    def get_assistive_results_details(doctype):
        name = frappe.get_all('Results and Recommendtions', filters={'ref_doctype': doctype}, pluck='name')
        if len(name):
           return frappe.get_doc('Results and Recommendtions', name[0])
