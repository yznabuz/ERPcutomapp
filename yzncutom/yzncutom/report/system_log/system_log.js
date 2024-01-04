// Copyright (c) 2023, yzn and contributors
// For license information, please see license.txt

frappe.query_reports["System Log"] = {
	"filters": [
		{
			"fieldname":"owner",
			"label": __("Owner"),
			"fieldtype":"Link",
			"options": "data",

		},
	]
};
