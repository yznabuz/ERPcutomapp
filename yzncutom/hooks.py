app_name = "yzncutom"
app_title = "yzncutom"
app_publisher = "yzn"
app_description = "test customize"
app_email = "yzn@mai.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/yzncutom/css/yzncutom.css"
# app_include_js = "/assets/yzncutom/js/yzncutom.js"

# include js, css files in header of web template
# web_include_css = "/assets/yzncutom/css/yzncutom.css"
# web_include_js = "/assets/yzncutom/js/yzncutom.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "yzncutom/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Order" : "public/js/sales_order.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "yzncutom/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "yzncutom.utils.jinja_methods",
#	"filters": "yzncutom.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "yzncutom.install.before_install"
# after_install = "yzncutom.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "yzncutom.uninstall.before_uninstall"
# after_uninstall = "yzncutom.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "yzncutom.utils.before_app_install"
# after_app_install = "yzncutom.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "yzncutom.utils.before_app_uninstall"
# after_app_uninstall = "yzncutom.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "yzncutom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
    "Employee Checkin": "yzncutom.overrides.employee_chekin.customEmployeeChekin",
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"yzncutom.tasks.all"
#	],
#	"daily": [
#		"yzncutom.tasks.daily"
#	],
#	"hourly": [
#		"yzncutom.tasks.hourly"
#	],
#	"weekly": [
#		"yzncutom.tasks.weekly"
#	],
#	"monthly": [
#		"yzncutom.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "yzncutom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "yzncutom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "yzncutom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["yzncutom.utils.before_request"]
# after_request = ["yzncutom.utils.after_request"]

# Job Events
# ----------
# before_job = ["yzncutom.utils.before_job"]
# after_job = ["yzncutom.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"yzncutom.auth.validate"
# ]
