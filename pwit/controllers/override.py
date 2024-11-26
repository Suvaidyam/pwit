from frappe.core.doctype.user.user import User
from pwit.controllers.api import send_custom_welcome_email
from pwit.controllers.api import reset_custom_password

class CustomAPIs(User):
   def send_welcome_mail_to_user(self):
        return send_custom_welcome_email(self)
   
   def reset_password(self, send_email=True):
        return reset_custom_password(self, send_email)