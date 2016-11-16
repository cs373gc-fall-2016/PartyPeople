from flask import Blueprint, send_from_directory

# from app.api_test import APITest

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

# @app.route('/favicon.ico')
# def send_favicon():
#     return send_from_directory('.', 'favicon.ico')

@frontend.route('/systemjs.config.js')
def send_systemconfig():
    return send_from_directory('.', 'systemjs.config.js')

