# Copyright (c) 2023, yzn and contributors
# For license information, please see license.txt

import frappe
from frappe import _
import random
from frappe.model.document import Document


class Itemrequest(Document):
    def on_submit(self):
        ran = str(random.randint(0, 9999))
        
        doc = frappe.new_doc("Item")
        doc.item_name = self.item_name
        doc.item_group = self.item_group
        doc.uom = self.uom
        doc.item_code = ran
        doc.save()
