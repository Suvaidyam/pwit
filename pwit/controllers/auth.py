import frappe

class AuthAPIs:
    def create_session():
        new_doc = frappe.new_doc('Session')
        new_doc.insert() 
        return new_doc
    
    def set_user_session(name,user):
        doc = frappe.get_doc('Session',name)
        doc.user = user
        doc.save()
        return doc
    
    def register(data):
        if not data.get("email") or not data.get("password"):
            frappe.throw("Email and password are required")

        new_user = frappe.new_doc("User")
        new_user.email = data.get("email")

        if data.get("full_name"):
            full_name = data.get("full_name").split(" ")
            new_user.first_name = full_name[0]
            new_user.last_name = full_name[1] if len(full_name) > 1 else ""
        new_user.new_password = data.get("password")

        new_user.save()
        new_user.add_roles("System Manager")

        return new_user
