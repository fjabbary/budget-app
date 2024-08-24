import os
from flask import Flask # Import the Flask class from the flask library
from app.database import db, migrate #Import the instance of SQALchemy (db) and instance of Migrate (migrate) from database module


# Create an instance of the flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL')
#initializing the app with flask-sqlalchemy
db.init_app(app)
#initialize the app and db with migrate
migrate.init_app(app, db)

# Import the routes file so that it runs
from . import routes