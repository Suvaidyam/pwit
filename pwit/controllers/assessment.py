import frappe

class AssessmentAPIs:
    def question_list(doctype):
        assessments = frappe.get_all(doctype, fields=['*'])
        return {'code': 200, 'data': assessments}
        