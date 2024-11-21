import frappe

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
        if not data.get("email") or not data.get("password"):
            return {'code':400,'msg':'Email and password are required'} 
        try:
            new_user = frappe.new_doc("User")
            new_user.email = data.get("email")

            if data.get("full_name"):
                full_name = data.get("full_name").split(" ")
                new_user.first_name = full_name[0]
                new_user.last_name = full_name[1] if len(full_name) > 1 else ""
            new_user.new_password = data.get("password")

            new_user.save(ignore_permissions=True)
            new_user.add_roles("System Manager")
            return {'code':200,'msg':'Register successfully','data':new_user} 
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
