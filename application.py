""" Launch the application and route to other pages """
from flask import Flask, request
from app import searchdb, query
from app.models import Candidate, Election, Party, State, ElectoralCollege, PartiesInvolved, ElectionsToState

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://partypeople:sweatypeople@partypeople-postgresql.cldmkovirzyt.us-west-2.rds.amazonaws.com:5432/partypeople_database'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ppdb'
    app.debug = True

    from app.models import database
    database.init_app(app)

    from app.api import create_api_endpoints
    create_api_endpoints(app)

    from app.views import frontend
    app.register_blueprint(frontend)

    @app.route("/api/s_and")
    def  s_and():
        term = request.args.get("term")
        return searchdb.search_and(term)

    @app.route("/api/s_or")
    def  s_or():
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


    return app

application = create_app()

if __name__ == "__main__":
    # app = create_app()
    application.run()