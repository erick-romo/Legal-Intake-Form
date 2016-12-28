from settings.settings import *

SQLALCHEMY_DATABASE_URI = 'postgres://%s@localhost:5432/%s' %(db_username, db_databaseName)
SQLALCHEMY_TRACK_MODIFICATIONS = True


