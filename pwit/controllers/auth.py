import frappe
from frappe.utils import now_datetime
from hashlib import sha256
from frappe.utils import get_url

class AuthAPIs:
    def create_session():
        new_doc = frappe.new_doc('Session')
        new_doc.insert(ignore_permissions=True)
        return {'code':200,'data':new_doc} 
    
    def set_user_session(name,user):
        doc = frappe.get_doc('Session',name)
        doc.user = user
        doc.save()
        return {'code':200,'data':doc} 

    @frappe.whitelist(allow_guest=True)
    def register(data):
        if not data.get("email"):
            return {'code':400,'msg':'Email is required'} 
        try:
            exits = frappe.db.exists('User',data.get('email'))
            if exits:
                return {'code':400,'msg':'User already exists'}
            else:
                new_user = frappe.new_doc("User")
                new_user.email = data.get("email")

                if data.get("full_name"):
                    full_name = data.get("full_name").split(" ")
                    new_user.first_name = full_name[0]
                    new_user.last_name = full_name[1] if len(full_name) > 1 else ""

                new_user.save(ignore_permissions=True)
                # new_user.add_roles("System Manager")
                return {'code':200,'msg':'Password reset instructions have been sent to your email','data':new_user} 
        except Exception as e:
            return {'code':500,'msg':'Internal Server Error','data':str(e)} 
    
    def contact_us(data): 
        exits = frappe.db.exists('Contact Us',data.get('session'))
        if exits:
            return {'code':400,'msg':'You have already submitted a request'}
        else:
            new_doc = frappe.new_doc('Contact Us')
            new_doc.update(data)
            new_doc.insert(ignore_permissions=True)
            return {'code':200,'data':new_doc} 
            
    def set_route_logs(from_route,session,to): 
        doc = frappe.get_doc('Session', session)
        doc.append('routes', {
            'doctype': 'Route Child',
            'from': from_route,
            'to': to
        })
        doc.save(ignore_permissions=True)
        return {'code': 200, 'data': doc}
            
    def change_password(user,new_password): 
        doc = frappe.get_doc('User', user)
        doc.new_password = new_password
        doc.save(ignore_permissions=True)
        return {'code': 200, 'data': doc}
    
    def send_custom_welcome_email_method(doc):
        link= AuthAPIs.reset_password(doc)
        message_content = frappe.render_template("pwit/templates/pages/welcome_email_template.html",{"doc":doc, "verification_link": link})
        now = frappe.flags.in_test or frappe.flags.in_install
        frappe.sendmail(
            recipients=[doc.email],
            subject= 'Welcome to The Bridgespan Group Portal',
            message=message_content,
            delayed=(not now) if now is not None else doc.flags.delay_emails,
            retry=3,
        )

    def reset_password(self):  
        key = frappe.generate_hash()
        hashed_key = sha256(key.encode('utf-8')).hexdigest()
        frappe.db.set_value("User", self.name, "reset_password_key", hashed_key)
        frappe.db.set_value("User", self.name, "last_reset_password_key_generated_on", now_datetime())
        url = "/pwit/update-password?key=" + key
        link = get_url(url)
        return link