from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, TextAreaField

class ClientForm(Form):
	firstName = StringField('First Name', [validators.DataRequired()])  
	lastName = StringField('Last Name',)
	dob = StringField('Date of Birth', [validators.Length(max=25)])
	address = StringField('Address')
	city = StringField('City', [validators.Length(max=25)])
	zipcode = StringField('Zip Code', [validators.Length(max=25)])
	telephone = StringField('Telephone', [validators.Length(max=25)])
	safeNumber = BooleanField('SAFE NUMBER TO CALL?')
	language = StringField('Primary Language', [validators.Length(max=25)])
	income = IntegerField('Income')
	incomeSource = StringField('Source of Income', [validators.Length(max=25)])
	dependents = IntegerField('Number of Dependents')
	health = StringField('If Health Issues, Diagnosis', [validators.Length(max=25)])
	military = BooleanField('Military Service?')
	immigration = StringField('Immigration Status', [validators.Length(max=25)])
	legalIssue = StringField('Legal Problem', [validators.Length(max=25)])
	county = StringField('If Active Case, County', [validators.Length(max=25)])
	caseNumber = StringField('If Active Case, Case Number', [validators.Length(max=25)])
	deadlines = StringField('Any Known Deadlines', [validators.Length(max=25)])
	op = StringField('Opposing Party', [validators.Length(max=25)])
	opCounsel = StringField('Opposing Party Counsel', [validators.Length(max=25)])
	notes = TextAreaField('Notes')

class recipientEmail(Form):
	recipientEmail = StringField('Which Email(s) would you like to send this information to: ')
