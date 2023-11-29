# Copyright (c) 2023, yzn and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class motocycle(Document):
	def validate(self):
		start_date=self.start_date
		end_date=self.end_date
		if end_date < start_date:
			frappe.throw(_("End Date cannot be less than Start Date"))
