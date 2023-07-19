from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tickterial.tickloader import Tickloader

# main application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

# extensions
db = SQLAlchemy(app)
tickloader = Tickloader(db)

# import routes
from tickterial.routes import *

# create app instance
def create_app():
	with app.app_context():
		db.create_all()
	return app
