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
            "label": (_("Owner")),
            "fieldname": "owner",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": (_("Creation time")),
            "fieldname": "creation",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": (_("Reference Doctype")),
            "fieldname": "ref_doctype",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": (_("Doctype name")),
            "fieldname": "docname",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": (_("Data")),
            "fieldname": "data",
            "fieldtype": "Data",
            "width": 500
        }

    ]
    return columns


def get_data(filters):

    if filters.get("owner"):
        query  += f" AND owner= '{frappe.db.escape(filters['owner'])}'"

    query = """select owner, creation, docname, data, ref_doctype from `tabVersion`"""
    data = frappe.db.sql(query,as_dict=True)
    return data


