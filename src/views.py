from imports import * 


app = Flask(__name__)

import os
app.config.from_object(os.environ['APP_SETTINGS']
print os.environ['APP_SETTINGS']

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'erickalan.chavarria@gmail.com',
	MAIL_PASSWORD = 'behappy108'
	)
mail = Mail(app)

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Test]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <erick@codeforprogress.org>'



from models import db, Client
from forms import ClientForm, recipientEmail


@app.route('/', methods=['POST','GET'])
def home():
	session['client_data'] = ""
	form = ClientForm(request.form)
	if request.method == 'POST' and form.validate():
		newClient = Client(firstName=form.firstName.data,  
					lastName=form.lastName.data,
					dob=form.dob.data,
					address=form.address.data,
					city=form.city.data,
					zipcode=form.zipcode.data,
					telephone=form.telephone.data,
					safeNumber=form.safeNumber.data,
					language=form.language.data,
					income=form.income.data,
					incomeSource=form.incomeSource.data,
					dependents=form.dependents.data,
					health=form.health.data,
					military=form.military.data,
					immigration=form.immigration.data,
					legalIssue=form.legalIssue.data,
					county=form.county.data,
					caseNumber=form.caseNumber.data,
					deadlines=form.deadlines.data,
					op=form.op.data,
					opCounsel=form.opCounsel.data,
					notes=form.notes.data)

		db.session.add(newClient)
		db.session.commit()		

		session['client_data'] = {
		'First Name' : form.firstName.data, 
		'Last Name' : form.lastName.data,
		'Date of Birth' : form.dob.data,
		'Address' : form.address.data,
		'City': form.city.data,
		'Zip': form.zipcode.data,
		'Telephone' : form.telephone.data,
		'Safe Number to Call' : form.safeNumber.data,
		'Language' : form.language.data,
		'Income' : form.income.data,
		'Income Source' : form.incomeSource.data,
		'Dependents' : form.dependents.data,
		'Health Diagnosis' : form.health.data,
		'Military Service' : form.military.data,
		'Immigration Status' : form.immigration.data,
		'Legal Problem' : form.legalIssue.data,
		'County Where Case is Active' : form.county.data,
		'Case Number' : form.caseNumber.data,
		'Approaching Deadlines' : form.deadlines.data,
		'Opposing Party' : form.op.data,
		'Opposing Party Counsel' : form.opCounsel.data,
		'Notes' : form.notes.data}
		
		return redirect(url_for('clientInfo'))
	return render_template('home.html', form=form)


@app.route('/info')
def clientInfo(): 
	client_data = session['client_data']
	if request.method == 'GET': 
		return render_template('sendclient.html', client_data=client_data)
		return redirect(url_for('recipientEmail'))
	
@app.route('/info/receiver/', methods=['POST','GET'])
def recipient():
	form = recipientEmail(request.form)
	if request.method == 'POST':
		# email = form.recipientEmail.data
		session['email'] = {
		'recipientEmail' : form.recipientEmail.data}
		return redirect(url_for('send_mail'))
	return render_template('receiver.html', form=form)
	


@app.route('/info/receiver/send-mail/')
def send_mail():
	client_data = session['client_data']
	Finalemail = session['email']['recipientEmail']
	try:
		msg = Message("Client Information",
			sender="erickalan.chavarria@gmail.com",
			recipients= [Finalemail])
		msg.html = render_template('/mail/email.html', client_data=client_data)
		# msg.body = """Hello, this is a person in need of your services. Please check their information below: \n
		# First Name: %s
		# Last Name: %s
		# Date of Birth: %s
		# Address: %s
		# Telephone: %s
		# Safe Number to Call?: %s
		# Primary Language: %s
		# Income: %s
		# Income Source: %s
		# Dependents: %s
		# Health Diagnosis: %s
		# Military Service: %s
		# Immigration Status: %s
		# Legal Problem: %s
		# County Where Case is Active: %s
		# Case Number: %s
		# Approaching Deadlines: %s
		# Opposing Party: %s
		# Opposing Party Counsel: %s
		# Notes: %s
		# """ % (session['client_data']['First Name'], session['client_data']['Last Name'], session['client_data']['Date of Birth'], session['client_data']['Address'], session['client_data']['Telephone'], session['client_data']['Safe Number to Call'], session['client_data']['Language'], session['client_data']['Income'], session['client_data']['Income Source'], session['client_data']['Dependents'], session['client_data']['Health Diagnosis'], session['client_data']['Military Service'], session['client_data']['Immigration Status'], session['client_data']['Legal Problem'], session['client_data']['County Where Case is Active'], session['client_data']['Case Number'], session['client_data']['Approaching Deadlines'], session['client_data']['Opposing Party'], session['client_data']['Opposing Party Counsel'], session['client_data']['Notes'])

		mail.send(msg)
		return render_template('confirmation.html')
	except Exception as e: 
		return str(e)





