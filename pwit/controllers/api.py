import frappe

@frappe.whitelist(allow_guest=True)
def create_session():
    new_doc = frappe.new_doc('Session')
    new_doc.insert() 
    return new_doc