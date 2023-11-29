// Copyright (c) 2023, yzn and contributors
// For license information, please see license.txt

frappe.ui.form.on("Exchange rate", {
    setup(frm) {
        frm.set_value("to_currency", "")
        frm.set_value("from_currency", "")

    },
	to_currency(frm) {
        frm.events.get_exchange_rate(frm)
	},
    from_currency(frm) {
        frm.events.get_exchange_rate(frm)
    },
    amount(frm) {
        frm.events.get_exchange_rate(frm)
    },
    get_exchange_rate(frm) {
        if(frm.doc.from_currency!=""&& frm.doc.to_currency!=""&& frm.doc.amount!=""){
        if (frm.doc.from_currency == frm.doc.to_currency) {
            frappe.set_value("from_currency","")
            frappe.throw(__("From and To currency cannot be same"));
        }else{
            fetch (`https://v6.exchangerate-api.com/v6/379f9c53b991dc13db2dc9b5/pair/${frm.doc.from_currency}/${frm.doc.to_currency}`)
            .then(r => r.json())
            .then(data => {
                frm.set_value("exchange_rate",data.conversion_rate)
                frm.set_value("to_amount",data.conversion_rate * frm.doc.amount)
            });
        }
    }
    }
});


