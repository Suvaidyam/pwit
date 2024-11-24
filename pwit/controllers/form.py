import frappe

class FormAPIs:
    def get_meta(doctype):
        return frappe.get_meta(doctype)
    
    def save_doc(doctype, doc):
        cleaned_doc = {key: value for key, value in doc.items() if value is not None}
        new_doc = frappe.new_doc(doctype)
        new_doc.update(cleaned_doc)
        new_doc.save(ignore_permissions=True)

        return {'code': 200, 'message': 'Document saved successfully', 'data': new_doc}