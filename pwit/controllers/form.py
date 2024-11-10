import frappe

class FormAPIs:
    def get_meta(doctype):
        return frappe.get_meta(doctype)