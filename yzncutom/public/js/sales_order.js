frappe.ui.form.on("Sales Order", {
    refresh(frm){
        console.log(frm.doc.status)
        if(frm.doc.status == "Draft"){
            frappe.throw(__("Draft Sales Order"));
        }
    }
})