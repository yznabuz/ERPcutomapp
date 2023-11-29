// Copyright (c) 2023, yzn and contributors
// For license information, please see license.txt

frappe.query_reports["Item stok"] = {
	"filters": [
		{
			"fieldname":"item_code",
			"label": __("Item Code"),
			"fieldtype": "Link",
			"options": "Item",

		},
		{
			"fieldname":"warehouse",
            "label": __("Warehouse"),
            "fieldtype": "Link",
            "options": "Warehouse"
		}
	]
};
