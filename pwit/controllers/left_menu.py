import frappe

class LeftMenuAPIs:
    def left_menu_list():
        left_menu = frappe.get_all('Left-Menu',fields=['name','label','icon','ref_doctype','code'],filters={'disabled':0},order_by='label')
        
        return {'code': 200, 'data': left_menu}
    
    def route():
        left_menu = frappe.get_all('Left-Menu', fields=['ref_doctype'], filters={'disabled': 0})
        data = []  # Initialize data as a list
        for item in left_menu:
            # Create a dictionary for each item
            item_data = {
                'path': item.get('ref_doctype').lower().replace(" ", "-"),
                'name': item.get('ref_doctype').replace(" ", "")
            }
            data.append(item_data)  # Append the dictionary to the data list
        return {'code': 200, 'data': data}
    
    def get_recommended_principles():
        data = frappe.get_all('Recommendation Logic', fields=['*'])
        return {'code': 200, 'data': data}
