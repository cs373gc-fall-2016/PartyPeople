# https://flask-restless.readthedocs.io/en/stable/customizing.html
from flask_restless import APIManager

import app.models as models

def create_api_endpoints(app):
	""" Create API endpoints available at /api/<tablename> by default """
	manager = APIManager(app, flask_sqlalchemy_db=models.database)
	manager.create_api(models.State)
	manager.create_api(models.Party)
	manager.create_api(models.Candidate)
	manager.create_api(models.Election)
	manager.create_api(models.ElectoralCollege)
	manager.create_api(models.PartiesInvolved)