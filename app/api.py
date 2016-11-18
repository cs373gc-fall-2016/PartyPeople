""" API routes for individual model access """
# https://flask-restless.readthedocs.io/en/stable/customizing.html
from flask_restless import APIManager
# pylint: disable=import-error
import app.models as models


def create_api_endpoints(app):
    """ Create API endpoints available at /api/<tablename> by default """
    manager = APIManager(app, flask_sqlalchemy_db=models.database)
    manager.create_api(models.State, results_per_page=0)
    manager.create_api(models.Party, results_per_page=0)
    manager.create_api(models.Candidate, results_per_page=0)
    manager.create_api(models.Election, results_per_page=0)
    manager.create_api(models.ElectoralCollege,
                       results_per_page=0, collection_name='electoralcollege')
    manager.create_api(models.PartiesInvolved,
                       results_per_page=0, collection_name='partiesinvolved')
    manager.create_api(models.ElectionsToState,
                       results_per_page=0, collection_name='electionstostate')
