""" Launch the application and route to other pages """
from flask import Flask, request
from app import searchdb, query
from app.models import Candidate, Election, Party, State, ElectoralCollege, PartiesInvolved, ElectionsToState

def create_app():
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://partypeople:sweatypeople@partypeople-postgresql.cldmkovirzyt.us-west-2.rds.amazonaws.com:5432/partypeople_database'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ppdb'
    application.debug = True

    from app.models import database
    database.init_app(application)

    from app.api import create_api_endpoints
    create_api_endpoints(application)

    from app.views import frontend
    application.register_blueprint(frontend)

    @app.route("/api/s_and")
    def s_and():
        term = request.args.get("term")
        return searchdb.search_and(term)

    @app.route("/api/s_or")
    def s_or():
        term = request.args.get("term")
        return searchdb.search_or(term)

    @app.route("/api/elections")
    def elections():
        return query.query_election()

    @app.route("/api/candidates")
    def candidates():
        return query.query_candidate()

    @app.route("/api/parties")
    def parties():
        return query.query_party()

    @app.route("/api/states")
    def states():
        return query.query_state()


    return application

if __name__ == "__main__":
    application = create_app()
    application.run()