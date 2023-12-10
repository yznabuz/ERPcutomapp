// Copyright (c) 2023, yzn and contributors
// For license information, please see license.txt

frappe.ui.form.on("Send Whatsapp", {
    send(frm) {
        fetch("https://api.maytapi.com/api/c945096d-6054-4691-83f9-baa3fc1a0f1f/37914/sendMessage", {
            method: "POST",
            headers: {
                "x-maytapi-key": "7c414015-c261-4fdb-8f72-84e007044058",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                to_number: frm.doc.contacts_info,
                type: "text",
                message: frm.doc.massage,
            }),
        })
        .then(r => r.json())
        .catch(err => console.error(err));
    },
});

