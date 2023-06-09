# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors
# For license information, please see license.txt


import frappe


def execute():
	frappe.get_doc("DocType", "Database Server MariaDB Variable").run_module_method(
		"on_doctype_update"
	)
