""" Frontend application routes """
# pylint: disable=import-error,invalid-name,unused-argument

from flask import Blueprint, send_from_directory, request
from app import searchdb, query

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
@frontend.route('/<path:path>')
def index(path=""):
    """
    Returns the home page
    """
    return send_from_directory('.', 'index.html')


@frontend.route('/node_modules/<path:path>')
def send_nodemodules(path):
    """
    Angular dependencies
    """
    return send_from_directory('node_modules', path)


@frontend.route('/app/<path:path>')
def send_app(path):
    """
    Navigate to app directory
    """
    return send_from_directory('app', path)


@frontend.route("/api/s_and")
def s_and():
    """
    Search route for AND
    """
    term = request.args.get("term")
    return searchdb.search_and(term)


@frontend.route("/api/s_or")
def s_or():
    """
    Search route for OR
    """
    term = request.args.get("term")
    return searchdb.search_or(term)


@frontend.route("/api/elections")
def elections():
    """
    Election api route
    """
    return query.query_election()


@frontend.route("/api/candidates")
def candidates():
    """
    Candidate api route
    """
    return query.query_candidate()


@frontend.route("/api/parties")
def parties():
    """
    Party api route
    """
    return query.query_party()


@frontend.route("/api/states")
def states():
    """
    State api route
    """
    return query.query_state()


@frontend.route('/api/test', methods=['GET'])
def run_tests():
    """
    Run model tests
    """
    import app.run_tests as test_suite
    return test_suite.run_tests()


@frontend.route('/systemjs.config.js')
def send_systemconfig():
    """
    Angular import mappings
    """
    return send_from_directory('.', 'systemjs.config.js')
