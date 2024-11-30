from frappe.utils.pdf import get_pdf
from frappe.utils.file_manager import save_file
import frappe

class Result:
    def download_results():
        html = frappe.render_template('pwit/templates/pages/Result.html',{"doc":'Rahul'})
        pdf = get_pdf(html, {"margin-top": "1mm", "margin-bottom": "1mm", "margin-left": "0mm", "margin-right": "0mm","encoding": "UTF-8"})

        frappe.local.response.filename = f"results.pdf"
        frappe.local.response.filecontent = pdf
        frappe.local.response.type = "download"