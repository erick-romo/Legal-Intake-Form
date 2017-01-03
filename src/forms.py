from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, TextAreaField

class ClientForm(Form):
	firstName = StringField([validators.DataRequired()])  
	lastName = StringField()
	dob = StringField()
	address = StringField()
	city = StringField()
	zipcode = StringField()
	telephone = StringField()
	safeNumber = BooleanField()
	language = StringField()
	income = IntegerField()
	incomeSource = StringField()
	dependents = IntegerField()
	health = StringField()
	military = BooleanField()
	immigration = StringField()
	legalIssue = StringField()
	county = StringField()
	caseNumber = StringField()
	deadlines = StringField()
	op = StringField()
	opCounsel = StringField()
	notes = TextAreaField()

class recipientEmail(Form):
	recipientEmail = StringField()
