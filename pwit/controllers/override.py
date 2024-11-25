from frappe.core.doctype.user.user import User
from pwit.controllers.api import send_custom_welcome_email

class CustomAPIs(User):
   def send_welcome_mail_to_user(self):
        return send_custom_welcome_email(self)