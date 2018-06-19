# -*- coding: utf-8 -*-

def home():
	form = FORM(
		INPUT(
			_type = "text",
			_name = "email",
			requires = IS_EMAIL(
				error_message = "please enter a valid e-mail address"
				)
			),
		INPUT(
			_type = "submit",
			_value = "Submit Email",
			)
		)
	if (form.process().accepted):
		db.emails.insert(
			email = form.vars.email,
			)
		db.commit()
		redirect(
			URL(
				a = "validation",
				c = "c01",
				f = "entered",
				)
			)
	return dict(
		form = form,
		)
def entered():
	message = "thanks for submitting your email"
	home = A(
		"home",
		_href = URL(
			a = "validation",
			c = "c01",
			f = "home",
			)
		)
	return dict(
		home = home,
		message = message,
		)
