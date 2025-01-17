// Copyright (c) 2024, Rahul Sah and contributors
// For license information, please see license.txt

frappe.ui.form.on("Session", {
	refresh(frm) {
        frm.set_df_property('session_id', 'hidden', 1);
	},
});
