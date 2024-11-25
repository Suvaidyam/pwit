import frappe

class AssessmentAPIs:
    def question_list(doctype):
        assessments = frappe.get_all(doctype, fields=['*'])
        return {'code': 200, 'data': assessments}

    def get_results(doctype,session,user=None):
        assessments = []
        if not user:
            assessments = frappe.get_all(doctype,filters={'session':session}, fields=['*'],order_by='creation desc', limit_page_length=1)
        else:
            all_session = frappe.get_all('Session', {'user': user}, pluck='name',order_by='creation desc')
            if len(all_session):
                assessments = frappe.get_all(doctype,filters={'session':["IN", all_session]}, fields=['*'],order_by='creation desc', limit_page_length=1)
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
        meta = frappe.get_meta(doctype)
        if not user:
            assessments = frappe.get_all(doctype,filters={'session':session}, fields=['*'],order_by='creation desc', limit_page_length=1)
        else:
            all_session = frappe.get_all('Session', {'user': user}, pluck='name',order_by='creation desc')
            if len(all_session):
                assessments = frappe.get_all(doctype,filters={'session':["IN", all_session]}, fields=['*'],order_by='creation desc', limit_page_length=1)
        if len(assessments) > 0:
            assessment = assessments[0]
            final_fields = {}
            sf = None  # Keep track of the current Section Break

            # Organize fields by section
            for field in meta.fields:
                if field.fieldtype == "Section Break":
                    sf = field.fieldname
                    final_fields[sf] = []  # Create a new entry for the section
                elif field.fieldtype == "Link" and field.options == "Field Options":
                    if sf:
                        final_fields[sf].append(field.fieldname)  # Add to the current section
            data = {}
            total = 0
            # Calculate scores
            for section, fields in final_fields.items():
                section_field = next((field for field in meta.fields if field.fieldname == section), None)
                data[section_field.label] = 0
                options = frappe.db.get_list(
                    'Field Options',
                    filters={
                        'ref_doctype': doctype,
                        'field': ["IN", fields]
                    },
                    fields=['name', 'field', 'score'],
                    ignore_permissions=True
                )
                for option in options:
                    # Check if the assessment matches this option
                    if assessment.get(option.field) == option.name:
                        data[section_field.label] += option.score
                        total += option.score
            average = round(total / len(final_fields),1)
            return {'code': 200,'data':{"average":average,"result":data}}
        else:
            return {'code': 200, 'data': {}}
     
