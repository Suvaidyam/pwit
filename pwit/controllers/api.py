import frappe
from pwit.controllers.auth import AuthAPIs

@frappe.whitelist(allow_guest=True)
def create_session():
    return AuthAPIs.create_session()

@frappe.whitelist(allow_guest=True)
def set_user_session(name,user):
    return AuthAPIs.set_user_session(name,user)

@frappe.whitelist(allow_guest=True)
def register(data):
    return AuthAPIs.register(data)

@frappe.whitelist(allow_guest=True)
def contact_us(data):
    return AuthAPIs.contact_us(data)

@frappe.whitelist(allow_guest=True)
def get_faq():
    data = frappe.get_all('FAQs',fields=['name','question','answer'])
    return {'code':200,'data':data}