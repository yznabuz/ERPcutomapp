from hrms.hr.doctype.employee_checkin.employee_checkin import EmployeeCheckin
import frappe
from frappe import _

class customEmployeeChekin(EmployeeCheckin):
    # def before_save(self):
    #     frappe.throw("working")

    def manage_employee_checkin_duplicates():
        # Specify the doctype and fields
        doctype_to_check = 'Employee Checkin'
        fields_to_check = ['employee', 'time']

        # Get a list of all records for the specified doctype
        records = frappe.get_all(doctype_to_check, fields=fields_to_check + ['name'], filters={})

        # Dictionary to store duplicates
        duplicates = {}

        # Identify duplicates
        for record in records:
            key = tuple(record.get(field) for field in fields_to_check)
            if key:
                if key not in duplicates:
                    duplicates[key] = [record['name']]
                else:
                    duplicates[key].append(record['name'])

        # Handle duplicates
        for key, value in duplicates.items():
            if len(value) > 1:
                # Keep the first record and delete the rest
                keep_record = value[0]
                for record_to_delete in value[1:]:
                    frappe.delete_doc(doctype_to_check, record_to_delete)

                print(f'Duplicates for Employee and Time = {key} in {doctype_to_check}. Keeping {keep_record} and deleting the rest.')

    if __name__ == "__main__":
        # Execute the script
        manage_employee_checkin_duplicates()
