import frappe
from frappe.utils import now_datetime
from hashlib import sha256
from frappe.utils import get_url
from hashlib import md5

class AuthAPIs:
    def create_session():
        new_doc = frappe.new_doc('Session')
        new_doc.insert(ignore_permissions=True)
        return {'code':200,'data':new_doc} 
    
    def set_user_session(name,user):
        doc = frappe.get_doc('Session',name)
        encrypt_user = md5(user.encode('utf-8')).hexdigest()
        doc.user = encrypt_user
        doc.save(ignore_permissions=True)
        return {'code':200,'data':doc} 
    
    def set_policyconsent_session(name,value):
        doc = frappe.get_doc('Session',name)
        doc.policyconsent = value
        doc.save(ignore_permissions=True)
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
        # exits = frappe.db.exists('Contact Us',data.get('session'))
        # if exits:
        #     return {'code':400,'msg':'You have already submitted a request'}
        # else:
            new_doc = frappe.new_doc('Contact Us')
            new_doc.update(data)
            new_doc.insert(ignore_permissions=True)
            # send email
            message_content = frappe.render_template("pwit/templates/pages/contact.html",{"doc":new_doc})
            now = frappe.flags.in_test or frappe.flags.in_install
            # shashank.rastogi@bridgespan.org
            frappe.sendmail(
                recipients= ['rahul.suvaidyam@gmail.com'],
                subject= 'Message submitted through Assistive Funder Toolkit',
                message=message_content,
                delayed=(not now) if now is not None else new_doc.flags.delay_emails,
                retry=3,
            )
            return {'code':200,'data':new_doc} 
            
    def set_route_logs(from_route,session,to): 
        doc = frappe.new_doc('Route Logs')
        doc.session = session
        doc.from_route = from_route
        doc.to_route = to
        doc.save(ignore_permissions=True)
        return {'code': 200, 'data': doc}
            
    def change_password(user,new_password): 
        doc = frappe.get_doc('User', user)
        doc.new_password = new_password
        doc.save(ignore_permissions=True)
        return {'code': 200, 'data': doc}
    
    def send_custom_welcome_email_method(doc):
        link= AuthAPIs.reset_password(doc)
        url = frappe.utils.get_url()
        message_content = frappe.render_template("pwit/templates/pages/verify_email.html",{"doc":doc, "verification_link": link, "url": url})
        now = frappe.flags.in_test or frappe.flags.in_install
        frappe.sendmail(
            recipients=[doc.email],
            subject= 'Verify your e-mail address',
            message=message_content,
            delayed=(not now) if now is not None else doc.flags.delay_emails,
            retry=3,
        )
   
    def reset_custom_password_method(doc, send_email=True):
        link= AuthAPIs.reset_password(doc)
        message_content = frappe.render_template("pwit/templates/pages/forget_email_template.html",{"doc":doc, "verification_link": link})
        now = frappe.flags.in_test or frappe.flags.in_install
        frappe.sendmail(
            recipients=[doc.email],
            subject= 'Forgot password',
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
    
    def save_user_details(data,session):  
        if session:
            doc = frappe.get_doc('Session', session)
            doc.designation = data.get('designation')
            doc.annual_budget = data.get('annual_budget')
            doc.funder_type = data.get('funder_type')
            doc.save(ignore_permissions=True)
            return {'code': 200, 'data': doc}
        else:
            return {'code': 400, 'msg': 'Session not found'}
        
    def check_user_details(session):  
        details = {}
        session_exits = frappe.get_all('Session', filters={'name': session,'designation':['is', 'set']}, pluck='name',order_by='creation desc',  limit_page_length=1,ignore_permissions=True )
        if frappe.session.user and not session_exits:
            user = user = md5(frappe.session.user.encode('utf-8')).hexdigest()
            details_exits = frappe.get_all('Session', filters={'user': user,'designation':['is', 'set']}, pluck='name',order_by='creation desc',  limit_page_length=1,ignore_permissions=True )
            if details_exits:
                session_details = frappe.get_doc('Session', details_exits[0])
                if session_details:
                    details = frappe.get_doc('Session', session)
                    details.designation = session_details.get('designation')
                    details.annual_budget = session_details.get('annual_budget')
                    details.funder_type = session_details.get('funder_type')
                    details.save(ignore_permissions=True)
                return {'code': 200, 'data': details}
            else:
                return {'code': 400, 'msg': 'Session not found'}
        else:
            return {'code': 200, 'data':{},'msg':'Already set'}
   
    def get_other_details(session):
        session_details = {}
        existing_session = frappe.get_all(
            'Session',
            filters={'name': session, 'designation': ['is', 'set']},
            pluck='name',
            order_by='creation desc',
            limit_page_length=1,
            ignore_permissions=True
        )
        
        if frappe.session.user and existing_session:
            user = md5(frappe.session.user.encode('utf-8')).hexdigest()
            existing_user_session = frappe.get_all(
                'Session',
                filters={'user': user, 'designation': ['is', 'set']},
                pluck='name',
                order_by='creation desc',
                limit_page_length=1,
                ignore_permissions=True
            )
            
            if existing_user_session:
                session_doc = frappe.get_doc('Session', existing_user_session[0])
                session_details = session_doc.as_dict()

            return {'code': 200, 'data': session_details}
        
        return {'code': 404, 'message': 'Session or user not found'}
    
    def user_mobile_no():
        user_mobile = frappe.get_value('User', frappe.session.user, 'mobile_no')
        return {'code': 200, 'data': user_mobile}


        