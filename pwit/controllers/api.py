import frappe
from pwit.controllers.auth import AuthAPIs
from pwit.controllers.left_menu import LeftMenuAPIs
from pwit.controllers.assessment import AssessmentAPIs
from pwit.controllers.form import FormAPIs
from pwit.controllers.results import Result

@frappe.whitelist(allow_guest=True)
def create_session():
    return AuthAPIs.create_session()

@frappe.whitelist(allow_guest=True)
def set_user_session(name,user):
    return AuthAPIs.set_user_session(name,user)

@frappe.whitelist(allow_guest=True)
def set_policyconsent_session(name,value):
    return AuthAPIs.set_policyconsent_session(name,value)

@frappe.whitelist(allow_guest=True)
def register(data):
    return AuthAPIs.register(data)

@frappe.whitelist(allow_guest=True)
def change_password(user,new_password):
    return AuthAPIs.change_password(user,new_password)

@frappe.whitelist(allow_guest=True)
def contact_us(data):
    return AuthAPIs.contact_us(data)

@frappe.whitelist(allow_guest=True)
def get_faq():
    data = frappe.get_all('FAQs',fields=['name','question','answer'])
    return {'code':200,'data':data}

@frappe.whitelist(allow_guest=True)
def left_menu_list():
    return LeftMenuAPIs.left_menu_list()

@frappe.whitelist(allow_guest=True)
def route():
    return LeftMenuAPIs.route()

@frappe.whitelist(allow_guest=True)
def get_recommended_principles():
    return LeftMenuAPIs.get_recommended_principles()

@frappe.whitelist(allow_guest=True)
def set_route_logs(**args):
    from_route = args.get('from')
    session = args.get('session')
    to = args.get('to')  

    return AuthAPIs.set_route_logs(from_route,session,to)

@frappe.whitelist(allow_guest=True)
def question_list(doctype):
    return AssessmentAPIs.question_list(doctype)

@frappe.whitelist(allow_guest=True)
def get_results(doctype,session,user=None):
    return AssessmentAPIs.get_results(doctype,session,user)

@frappe.whitelist(allow_guest=True)
def get_assistive_result(doctype,session,user=None):
    return AssessmentAPIs.get_assistive_result(doctype,session,user)

@frappe.whitelist()
def get_last_draft():
    return AssessmentAPIs.get_last_draft()

@frappe.whitelist(allow_guest=True)
def get_meta(doctype):
    return FormAPIs.get_meta(doctype)


@frappe.whitelist(allow_guest=True)
def save_image(data): 
    doc = frappe.get_doc('User',data.get('user'))
    doc.first_name=data.get('first_name')
    if data.get('last_name'):
        doc.last_name=data.get('last_name')
    doc.mobile_no=data.get('mobile_no')
    doc.user_image=data.get('user_image')
    doc.save()

@frappe.whitelist(allow_guest=True)
def save_doc(doctype, doc,name=None):
    return FormAPIs.save_doc(doctype, doc,name)

@frappe.whitelist(allow_guest=True)
def save_as_draft(doctype, doc,name=None):
    return FormAPIs.save_as_draft(doctype, doc,name)

@frappe.whitelist(allow_guest=False)
def get_save_as_draft(doctype, user):
    return FormAPIs.get_save_as_draft(doctype, user)

def send_custom_welcome_email(doc):
    AuthAPIs.send_custom_welcome_email_method(doc)

def reset_custom_password(doc, send_email=True):
    AuthAPIs.reset_custom_password_method(doc, send_email)

@frappe.whitelist(allow_guest=True)
def result_download():
    return Result.download_results()