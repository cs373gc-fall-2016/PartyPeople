from flask import Blueprint, send_from_directory
from StringIO import StringIO
import unittest

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

# @frontend.route('/api/test', methods=['GET'])
# def run_tests():
# 	output = StringIO()
# 	suite = unittest.TestLoader().loadTestsFromTestCase(APITest)
# 	unittest.TextTestRunner(stream=output,verbosity=2).run(suite)
# 	result = output.getvalue().replace('\n', '<br />')
# 	output.close()
# 	return result