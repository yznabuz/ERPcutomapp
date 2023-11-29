# Copyright (c) 2023, yzn and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    columns = [
        {
            "label": (_("Item Code")),
            "fieldname": "item_code",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": (_(" Actual Qty")),
            "fieldname": "actual_qty",
            "fieldtype": "Integer",
            "width": 100
        },
        {
            "label": (_(" Warehouse")),
            "fieldname": "warehouse",
            "fieldtype": "Data",
            "width": 200
        }

    ]
    return columns


def get_data(filters):
    conditions = get_conditions(filters)
    data = frappe.db.get_all("Bin", filters=conditions, fields=["item_code", "actual_qty","warehouse"] )
    return data


def get_conditions(filters):
    conditions = {}

    if filters.item_code:
        conditions["item_code"] = filters.item_code
        
    if filters.warehouse:
        conditions["warehouse"] = filters.warehouse
    
    return conditions