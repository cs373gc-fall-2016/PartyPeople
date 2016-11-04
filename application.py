""" Launch the application and route to other pages """
from flask import Flask, render_template, send_from_directory

import unittest
from StringIO import StringIO
from app.api_test import APITest

# EB looks for an 'application' callable by default.
# pylint: disable=invalid-name
application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://partypeople:sweatypeople@' \
                                                'partypeople-postgresql.cldmkovirzyt.us-west-2.rds.amazonaws.com:5432/partypeople_database'

@application.route('/')
@application.route('/<path:path>')
def index(path = ""):
    """ Returns the home page """
    return send_from_directory('.', 'index.html')


@application.route('/node_modules/<path:path>')
def send_nodemodules(path):
    return send_from_directory('node_modules', path)

@application.route('/app/<path:path>')
def send_app(path):
    return send_from_directory('app', path)

# @app.route('/favicon.ico')
# def send_favicon():
#     return send_from_directory('.', 'favicon.ico')

@application.route('/systemjs.config.js')
def send_systemconfig():
    return send_from_directory('.', 'systemjs.config.js')

@application.route('/api/test', methods=['GET'])
def run_tests():
	output = StringIO()
	suite = unittest.TestLoader().loadTestsFromTestCase(APITest)
	unittest.TextTestRunner(stream=output,verbosity=2).run(suite)
	result = output.getvalue().replace('\n', '<br />')
	output.close()
	return result


# Run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run(debug=False)
