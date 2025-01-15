from pwit.controllers.api import get_results,get_recommended_principles
import frappe, re
from frappe.utils.pdf import get_pdf

@frappe.whitelist(allow_guest=True)
def download_funder(session):
    user = frappe.session.user if frappe.session.user != 'Guest' else ''
    fd_results = get_results('Funder Diagnostic',session,user)
    updated_data = []
    data = [
    {
        "name": 1,
        "score": 0,
        "group": "Recommended",
        "code": "myp",
        "name1": "DEVELOP MULTIYEAR FUNDER-NONPROFIT PARTNERSHIPS",
        "description": "Multiyear partnerships nurture trust between funders and nonprofits while simplifying the grantmaking process. Adopting a longer-term partnership approach can help funders increasingly focus on creating lasting change, over immediate and short-term outputs.",
        "icon": "https://res.cloudinary.com/dkb3hvxhf/image/upload/v1736846693/myp_c6bxyx.png", 
        "doctype": "Multi-year Partnerships",
        "color": "#59467b",
    },
    {
        "name": 2,
        "score": 0,
        "group": "Recommended",
        "code": "core_cost",
        "name1": "PAY A FAIR SHARE OF CORE COSTS",
        "description": "Core costs – often referred to as indirect costs or administrative costs – are associated with support functions essential for nonprofits to conduct day-to-day operations and deliver on their impact mandates. Supporting nonprofits in this regard aligns with the funder’s goals of ensuring that nonprofits have the critical investments required to enable operational effectiveness, have sound governance processes and structures in place, are compliant with regulations, and have solid financial management practices.",
        "icon": "https://res.cloudinary.com/dkb3hvxhf/image/upload/v1736846692/cc_uv8mer.png", 
        "doctype": "Core Costs",
        "color": "#136096",
    },
    {
        "name": 3,
        "score": 0,
        "group": "Recommended",
        "code": "od",
        "name1": "INVEST IN ORGANISATIONAL DEVELOPMENT",
        "description": "Organisational development (OD) investments build and strengthen a range of critical efficiency and growth-oriented capabilities (e.g., strategic planning, fundraising, human resources, etc.) that enable nonprofits to deliver greater impact.",
        "icon": "https://res.cloudinary.com/dkb3hvxhf/image/upload/v1736846693/od_jcasnj.png", 
        "doctype": "Organisational Development",
        "color": "#029fd9",
    },
    {
        "name": 4,
        "score": 0,
        "group": "Additional",
        "code": "dei",
        "name1": "EMBED DIVERSITY, EQUITY, AND INCLUSION IN GRANTMAKING",
        "description": "An intentional focus on DEI can help funders address the disproportional funding gap that persists for organisations not located in major cities and headed by members of historically marginalised populations, such as Dalit, Bahujan, and Adivasi (DBA) communities. By supporting these critical agents of social change, funders can accelerate progress on India’s steepest challenges.",
        "icon": "https://res.cloudinary.com/dkb3hvxhf/image/upload/v1736846692/dei_sjctcg.png", 
        "doctype": "Diversity Equity Inclusion",
        "color": "#f38714",
    },
    {
        "name": 5,
        "score": 0,
        "group": "Additional",
        "code": "fr",
        "name1": "BUILD FINANCIAL RESILIENCE",
        "description": "Financial resilience refers to a nonprofit’s ability to sustain its operations over the long term and withstand external stresses and shocks. By supporting nonprofits in building their financial resilience, funders can help strengthen an organisation’s ability to continue creating impact in targeted communities and geographies.",
        "icon": "https://res.cloudinary.com/dkb3hvxhf/image/upload/v1736846692/fr_x7w2fy.png",
        "doctype": "Financial Resilience",
        "color": "#058248",
    }
]

    
    # Group the results by prefix
    grouped_sums = {}
    if fd_results.get('data'):
        for key, value in fd_results['data'].items():
            key_parts = key.split('_')
            key_parts.pop()
            prefix = '_'.join(key_parts)
            grouped_sums[prefix] = grouped_sums.get(prefix, 0) + value

    # Get the recommended principles
    recommended = get_recommended_principles()
    topMatching = evaluate_logic(recommended, grouped_sums)
    
    if not topMatching:
        # If no matching logic, return updated data with scores
        for item in data:
            item['score'] = grouped_sums.get(item['code'], 0)
            updated_data.append(item)
        updated_data = sort_and_assign(updated_data)  # Add sorting if necessary
    else:
        topMatching = topMatching[0]
        # Return data in recommended and additional groups based on topMatching
        updated_data = [
            {**next((item for item in data if item['code'] == topMatching.get('recommendation_1')), {}), 'group': 'Recommended'},
            {**next((item for item in data if item['code'] == topMatching.get('recommendation_2')), {}), 'group': 'Recommended'},
            {**next((item for item in data if item['code'] == topMatching.get('recommendation_3')), {}), 'group': 'Recommended'},
            {**next((item for item in data if item['code'] == topMatching.get('additional_1')), {}), 'group': 'Additional'},
            {**next((item for item in data if item['code'] == topMatching.get('additional_2')), {}), 'group': 'Additional'}
        ]

    html = frappe.render_template('pwit/templates/pages/funder_diagnostic.html', {"data": updated_data})
    pdf = get_pdf(html, {
        "margin-top": "1mm",
        "margin-bottom": "1mm",
        "margin-left": "0mm",
        "margin-right": "0mm",
        "encoding": "UTF-8"
    })
    frappe.local.response.filename = f"Funder Diagnostic.pdf"
    frappe.local.response.filecontent = pdf
    frappe.local.response.type = "download"


def evaluate_logic(logic_array, results):
    filtered_entries = []
    for entry in logic_array['data']:
        try:
            if entry.get('logic', '').strip():
                substituted_logic = entry['logic']
                
                # Replace terms in the logic with the corresponding results values
                substituted_logic = re.sub(
                    r'\b(core_cost|od|myp|fr|dei)\b',
                    lambda match: str(results.get(match.group(), 0)),
                    substituted_logic
                )
                substituted_logic = substituted_logic.replace('&&', 'and').replace('||', 'or')
                # Evaluate the substituted logic
                if eval(substituted_logic):
                    filtered_entries.append(entry)
                    
        except Exception as e:
            print(f"Error evaluating logic for entry {entry['name']}: {e}")
            
    return filtered_entries

def sort_and_assign(d):
    d.sort(key=lambda x: (x['score'], x['name']))
    
    for index, item in enumerate(d):
        item['group'] = 'Recommended' if index < 3 else 'Additional'
    return d

