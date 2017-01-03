import os 
basedir= os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'trulyrandomkey'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] 
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	db_username = 'postgres'
db_databaseName = 'example'


class DevelopmentConfig(BaseConfig):
	DEVELOPMENT = True
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False