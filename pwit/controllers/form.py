import frappe
from frappe.model.docstatus import DocStatus

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
        draft = {}
        session = frappe.get_all('Session', filters={'user': user}, pluck='name')
        if session:
            draft_name = frappe.get_list(doctype, filters={'session': ['IN',session],'docstatus':DocStatus.draft()}, pluck='name',order_by='creation desc', limit=1)
            if len(draft_name):
                draft = frappe.get_doc(doctype, draft_name[0])
            else:
                draft = {}
        return {'code': 200, 'data': draft}