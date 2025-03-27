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
def get_results(doctype,session=None,user=None):
    return AssessmentAPIs.get_results(doctype,session,user)

@frappe.whitelist(allow_guest=True)
def get_assistive_result(doctype,session=None,user=None):
    return AssessmentAPIs.get_assistive_result(doctype,session,user)

@frappe.whitelist(allow_guest=True)
def get_dei_result(doctype,session=None,user=None):
    return AssessmentAPIs.get_dei_result(doctype,session,user)

@frappe.whitelist()
def get_last_draft():
    return AssessmentAPIs.get_last_draft()

@frappe.whitelist(allow_guest=True)
def get_sub(session):
    return AssessmentAPIs.get_sub(session)

@frappe.whitelist(allow_guest=True)
def get_meta(doctype):
    return FormAPIs.get_meta(doctype)


@frappe.whitelist(allow_guest=True)
def update_user_dt(data): 
    doc = frappe.get_doc('User',data.get('user'))
    doc.first_name=data.get('first_name')
    if data.get('last_name'):
        doc.last_name=data.get('last_name')
    doc.mobile_no=data.get('mobile_no')
    doc.user_image=data.get('user_image')
    doc.save()
    return {'code':200,'message':'Profile updated successfully'}

@frappe.whitelist(allow_guest=True)
def save_doc(doctype, doc,name=None):
    return FormAPIs.save_doc(doctype, doc,name)

@frappe.whitelist(allow_guest=True)
def save_as_draft(doctype, doc,name=None):
    return FormAPIs.save_as_draft(doctype, doc,name)

@frappe.whitelist(allow_guest=True)
def get_save_as_draft(doctype, user):
    return FormAPIs.get_save_as_draft(doctype, user)

@frappe.whitelist(allow_guest=True)
def funder_type_options():
    return FormAPIs.funder_type_options()

def send_custom_welcome_email(doc):
    AuthAPIs.send_custom_welcome_email_method(doc)

def reset_custom_password(doc, send_email=True):
    AuthAPIs.reset_custom_password_method(doc, send_email)

@frappe.whitelist(allow_guest=True)
def download_results(doctype, session):
    return Result.download_results(doctype, session)

@frappe.whitelist(allow_guest=True)
def save_user_details(data,session):
    return AuthAPIs.save_user_details(data,session)

@frappe.whitelist(allow_guest=True)
def check_user_details(session):
    return AuthAPIs.check_user_details(session)

@frappe.whitelist(allow_guest=True)
def get_other_details(session):
    return AuthAPIs.get_other_details(session)

@frappe.whitelist(allow_guest=True)
def user_mobile_no():
    return AuthAPIs.user_mobile_no()

@frappe.whitelist(allow_guest=True)
def page_switch():
    data = frappe.get_doc('pwit settings')
    return {'data':data}

@frappe.whitelist(allow_guest=True)
def subscribe(email):
    exits = frappe.db.exists('Subscribe Mail', {'email': email})
    if exits:
        return {'code': 201, 'message': 'Email already submited'}
    else:
        doc = frappe.new_doc('Subscribe Mail')
        doc.email = email
        doc.save(ignore_permissions=True)
        return {'data':doc,'code': 200, 'message': 'Thank you for showing interest. We will notify you when we go live.'}

from frappe.auth import MAX_PASSWORD_SIZE
from frappe.core.doctype.user.user import test_password_strength, handle_password_test_fail,_get_user_for_update_password,reset_user_data
from frappe.utils import (
	cint,
	today
)
from frappe.utils.password import update_password as _update_password
from frappe.website.utils import get_home_page
from frappe.apps import get_default_path
from frappe import _
import frappe
@frappe.whitelist(allow_guest=True, methods=["POST"])
def custom_update_password(
    new_password: str, logout_all_sessions: int = 0, key: str | None = None, old_password: str | None = None
):

    if len(new_password) > MAX_PASSWORD_SIZE:
        frappe.throw(_("Password size exceeded the maximum allowed size."))

    result = test_password_strength(new_password)
    feedback = result.get("feedback", None)

    if feedback and not feedback.get("password_policy_validation_passed", False):
        handle_password_test_fail(feedback)

    res = _get_user_for_update_password(key, old_password)
    if res.get("message"):
        frappe.local.response.http_status_code = 410
        return res["message"]
    else:
        user = res["user"]

    logout_all_sessions = cint(logout_all_sessions) or frappe.get_system_settings("logout_on_password_reset")
    _update_password(user, new_password, logout_all_sessions=cint(logout_all_sessions))

    user_doc, redirect_url = reset_user_data(user)
    newurl = frappe.utils.get_url()
    newurl = newurl + "/pwit"
    email = frappe.db.get_value("User", user, "email")
    message_content = frappe.render_template("pwit/templates/pages/welcome_email_template.html",{"url": newurl})
    now = frappe.flags.in_test or frappe.flags.in_install
    frappe.sendmail(
        recipients=[email],
        subject= 'Welcome to the Bridgespan Group portal',
        message=message_content,
        delayed= (not now) if now is not None else user_doc.flags.delay_emails,
        retry=3
    )
    # get redirect url from cache
    redirect_to = frappe.cache.hget("redirect_after_login", user)
    if redirect_to:
        redirect_url = redirect_to
        frappe.cache.hdel("redirect_after_login", user)

    frappe.local.login_manager.login_as(user)

    frappe.db.set_value("User", user, "last_password_reset_date", today())
    frappe.db.set_value("User", user, "reset_password_key", "")

    if user_doc.user_type == "System User":
        return get_default_path() or "/app"
    else:
        return redirect_url or get_default_path() or get_home_page()

