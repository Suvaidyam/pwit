# Copyright (c) 2024, Rahul Sah and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Session(Document):
	def after_insert(self):
		self.session_id = self.name
		self.save(ignore_permissions=True)