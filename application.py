""" Launch the application and route to other pages """
from flask import Flask, render_template, send_from_directory

# EB looks for an 'application' callable by default.
# pylint: disable=invalid-name
application = Flask(__name__)


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






# @application.route('/states/texas')
# def texas():
#     """ Returns the state of Texas page """
#     return render_template('states_texas.html')


# @application.route('/states/alaska')
# def alaska():
#     """ Returns the state of Alaska page """
#     return render_template('states_alaska.html')


# @application.route('/states/california')
# def california():
#     """ Returns the state of California page """
#     return render_template('states_california.html')



# @application.route('/elections/general_election_2016')
# def general_election_2016():
#     """ Returns the general election page """
#     return render_template('elections_general_election_2016.html')


# @application.route('/elections/texas_23_district_2016')
# def texas_23_district_2016():
#     """ Returns the Texas District 23 page """
#     return render_template('elections_texas_23_district_2016.html')


# @application.route('/elections/california_12_district_2016')
# def california_12_district_2016():
#     """ Returns the California District 12 page """
#     return render_template('elections_california_12_district_2016.html')



# @application.route('/candidates/gary_johnson')
# def gary_johnson():
#     """ Returns the page for Gary Johnson """
#     return render_template('candidates_gary_johnson.html')


# @application.route('/candidates/ted_cruz')
# def ted_cruz():
#     """ Returns the page for Ted Cruz """
#     return render_template('candidates_ted_cruz.html')


# @application.route('/candidates/nancy_pelosi')
# def nancy_pelosi():
#     """ Returns the page for Nancy Pelosi """
#     return render_template('candidates_nancy_pelosi.html')



# @application.route('/parties/libertarian')
# def libertarian():
#     """ Returns the Libertarian party page """
#     return render_template('parties_libertarian.html')


# @application.route('/parties/democratic')
# def democratic():
#     """ Returns the Democratic party page """
#     return render_template('parties_democratic.html')


# @application.route('/parties/republican')
# def republican():
#     """ Returns the Republican party page """
#     return render_template('parties_republican.html')



# @application.route('/states')
# def states():
#     """ Returns the states model page """
#     return render_template('states_model.html')


# @application.route('/elections')
# def elections():
#     """ Returns the elections model page """
#     return render_template('elections_model.html')


# @application.route('/candidates')
# def candidates():
#     """ Returns the candidate model page """
#     return render_template('candidates_model.html')


# @application.route('/parties')
# def parties():
#     """ Returns the parties model page """
#     return render_template('parties_model.html')

# @application.route('/about')
# def about():
#     """ Returns the team about page """
#     return render_template('about.html')


# Run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run(debug=False)
