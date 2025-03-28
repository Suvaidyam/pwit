import frappe
from frappe.model.docstatus import DocStatus
from hashlib import md5
class FormAPIs:
    def get_meta(doctype):
        return frappe.get_meta(doctype)
    
    def save_doc(doctype, doc,name=None):
        cleaned_doc = {key: value for key, value in doc.items() if value is not None}
        if name:
            new_doc = frappe.get_doc(doctype, name)
            new_doc.update(cleaned_doc)
            new_doc.docstatus = DocStatus.submitted()
            new_doc.save(ignore_permissions=True)
        else:
            new_doc = frappe.new_doc(doctype)
            new_doc.update(cleaned_doc)
            new_doc.docstatus = DocStatus.submitted()
            new_doc.save(ignore_permissions=True)

        return {'code': 200, 'message': 'Document saved successfully', 'data': new_doc}
    
    def save_as_draft(doctype, doc,name=None):
        cleaned_doc = {key: value for key, value in doc.items() if value is not None}
        if name:
            new_doc = frappe.get_doc(doctype, name)
            new_doc.update(cleaned_doc)
            new_doc.flags.ignore_mandatory = True
            new_doc.save(ignore_permissions=True)
        else:
            new_doc = frappe.new_doc(doctype)
            new_doc.update(cleaned_doc)
            new_doc.docstatus = DocStatus.draft()
            new_doc.insert(ignore_permissions=True,ignore_mandatory=True)

        return {'code': 200, 'message': 'Document saved as draft successfully', 'data': new_doc}
    
    def get_save_as_draft(doctype, user):
        user = md5(user.encode('utf-8')).hexdigest()
        draft = {}
        session = frappe.get_all('Session', filters={'user': user}, pluck='name')
        if session:
            draft_name = frappe.get_list(doctype, filters={'session': ['IN',session],'docstatus':DocStatus.draft()}, pluck='name',order_by='creation desc',  limit_page_length=1,ignore_permissions=True )
            if len(draft_name):
                draft = frappe.get_doc(doctype, draft_name[0], ignore_permissions=True)
            else:
                draft = {}
        return {'code': 200, 'data': draft}
    
    import frappe

    def profile_dropdown_options():
        meta = frappe.get_meta('Session')
        fields = ['funder_type', 'designation', 'annual_budget']
        
        data = {}
        
        for field in fields:
            field_meta = meta.get_field(field)
            if field_meta and hasattr(field_meta, 'options') and field_meta.options:
                data[field] = field_meta.options.split('\n')[1:] 
            else:
                data[field] = []
        
        return {'code': 200, 'data': data}


    