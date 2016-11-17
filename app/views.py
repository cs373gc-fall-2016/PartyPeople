from flask import Blueprint, send_from_directory, request
from app import searchdb, query

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
@frontend.route('/<path:path>')
def index(path = ""):
    """ Returns the home page """
    return send_from_directory('.', 'index.html')

@frontend.route('/node_modules/<path:path>')
def send_nodemodules(path):
    return send_from_directory('node_modules', path)

@frontend.route('/app/<path:path>')
def send_app(path):
    return send_from_directory('app', path)

@frontend.route("/api/s_and")
def s_and():
    term = request.args.get("term")
    return searchdb.search_and(term)

@frontend.route("/api/s_or")
def s_or():
    term = request.args.get("term")
    return searchdb.search_or(term)

@frontend.route("/api/elections")
def elections():
    return query.query_election()

@frontend.route("/api/candidates")
def candidates():
    return query.query_candidate()

@frontend.route("/api/parties")
def parties():
    return query.query_party()

@frontend.route("/api/states")
def states():
    return query.query_state()

@frontend.route('/api/test', methods=['GET'])
def run_tests():
    import app.run_tests as test_suite
    return test_suite.run_tests()

@frontend.route('/systemjs.config.js')
def send_systemconfig():
    return send_from_directory('.', 'systemjs.config.js')

