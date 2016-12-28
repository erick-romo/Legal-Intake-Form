from flask_sqlalchemy import SQLAlchemy
from views import app

db = SQLAlchemy(app)

class Client(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	firstName = db.Column(db.String)  
	lastName = db.Column(db.String)
	dob = db.Column(db.String)
	address = db.Column(db.String)
	city = db.Column(db.String)
	zipcode = db.Column(db.String)
	telephone = db.Column(db.String)
	safeNumber = db.Column(db.Boolean)
	language = db.Column(db.String)
	income = db.Column(db.Numeric)
	incomeSource = db.Column(db.String)
	dependents = db.Column(db.Integer)
	health = db.Column(db.String)
	military = db.Column(db.Boolean)
	immigration = db.Column(db.String)
	legalIssue = db.Column(db.String)
	county = db.Column(db.String)
	caseNumber = db.column(db.String)
	deadlines = db.column(db.String)
	op = db.Column(db.String)
	opCounsel = db.Column(db.String)
	notes = db.Column(db.Text)

