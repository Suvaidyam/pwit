from frappe.utils.pdf import get_pdf
from pwit.controllers.assessment import AssessmentAPIs
import frappe

class Result:
 def download_results(doctype, session):
    user = None
    main = [{
                'label':'Multiyear funder-nonprofit partnerships',
                'name':'Multi-year Partnerships'
            },
            {
                'label':'Embedding diversity, equity and inclusion (DEI) in grantmaking',
                'name':'Diversity Equity Inclusion'
            },
            {
                'label':'Invest in organisational development',
                'name':'Organization Development'
            },
            {
                'label':'Building financial resilience',
                'name':'Financial Resilience'
            },
            {
                'label':'Pay a fair share of core costs',
                'name':'Core Costs'
            }
        ]
    selected_main = next((item for item in main if item['name'] == doctype), None)
    if frappe.session.user not in ["Administrator", "Guest"]:
        user = frappe.session.user
    try:
        data = {}
        if doctype =='Diversity Equity Inclusion':
            doc = AssessmentAPIs.get_dei_result(doctype, session, user)
            data = doc['data']
            groups = data['group']
            actions = []
            if data.get('details'):
                actions = data['details'].get('recommended_actions', [])
            if actions:
                sorted_actions = sorted(
                    actions,
                    key=lambda action: groups.get(action.title, float('inf')) 
                )
                data['details'].recommended_actions = sorted_actions
            data['main_title'] = selected_main['label']
        else:
            doc = AssessmentAPIs.get_assistive_result(doctype, session, user)
            data = doc['data']
            groups = data['group']
            actions = []
            if data.get('details'):
                actions = data['details'].get('recommended_actions', [])
            if actions:
                sorted_actions = sorted(
                    actions,
                    key=lambda action: groups.get(action.title, float('inf')) 
                )
                data['details'].recommended_actions = sorted_actions
            data['main_title'] = selected_main['label']
        # return
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
