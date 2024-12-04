from frappe.utils.pdf import get_pdf
from pwit.controllers.assessment import AssessmentAPIs
import frappe

class Result:
 def download_results(doctype, session):
    conditions = {
        1: {"width": "25%", "color": "#FF6464"},
        2: {"width": "50%", "color": "#FF6464"},
        3: {"width": "75%", "color": "#FFD23F"},
        4: {"width": "100%", "color": "#337357"}
    }
    user = None
    if frappe.session.user not in ["Administrator", "Guest"]:
        user = frappe.session.user
    try:
        doc = AssessmentAPIs.get_assistive_result(doctype, session, user)
        data = doc['data']
        # data = doc['data']['result']
        # result = [
        #     {
        #         "name": key,
        #         "value": value,
        #         "width": conditions[value]["width"],
        #         "color": conditions[value]["color"]
        #     }
        #     for key, value in data.items()
        # ]
        # if not data:
        #     frappe.throw(frappe._("No result data available for the provided session."))
        
        html = frappe.render_template('pwit/templates/pages/Result.html', {"doc": data})
        pdf = get_pdf(html, {
            "margin-top": "1mm",
            "margin-bottom": "1mm",
            "margin-left": "0mm",
            "margin-right": "0mm",
            "encoding": "UTF-8"
        })

        frappe.local.response.filename = f"{doctype}.pdf"
        frappe.local.response.filecontent = pdf
        frappe.local.response.type = "download"
    except Exception as e:
        frappe.log_error(f"Error generating PDF for {doctype} - {session}: {e}", "Download Results Error")
        frappe.throw(frappe._("An error occurred while generating the PDF."))
