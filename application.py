from flask import Flask, render_template

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# Return the home page.


@application.route('/')
def index():
    return render_template('index.html')

# Routes to STATES


@application.route('/states/texas')
def texas():
    return render_template('states_texas.html')


@application.route('/states/alaska')
def alaska():
    return render_template('states_alaska.html')


@application.route('/states/california')
def california():
    return render_template('states_california.html')

# Routes to ELECTIONS


@application.route('/elections/general_election_2016')
def general_election_2016():
    return render_template('elections_general_election_2016.html')


@application.route('/elections/texas_23_district_2016')
def texas_23_district_2016():
    return render_template('elections_texas_23_district_2016.html')


@application.route('/elections/california_12_district_2016')
def california_12_district_2016():
    return render_template('elections_california_12_district_2016.html')

# Routes to CANDIDATES


@application.route('/candidates/gary_johnson')
def gary_johnson():
    return render_template('candidates_gary_johnson.html')


@application.route('/candidates/ted_cruz')
def ted_cruz():
    return render_template('candidates_ted_cruz.html')


@application.route('/candidates/nancy_pelosi')
def nancy_pelosi():
    return render_template('candidates_nancy_pelosi.html')

# Routes to PARTIES


@application.route('/parties/libertarian')
def libertarian():
    return render_template('parties_libertarian.html')


@application.route('/parties/democratic')
def democratic():
    return render_template('parties_democratic.html')


@application.route('/parties/republican')
def republican():
    return render_template('parties_republican.html')

# Routes to MODEL pages


@application.route('/states')
def states():
    return render_template('states_model.html')


@application.route('/elections')
def elections():
    return render_template('elections_model.html')


@application.route('/candidates')
def candidates():
    return render_template('candidates_model.html')


@application.route('/parties')
def parties():
    return render_template('parties_model.html')

# Route to ABOUT page


@application.route('/about')
def about():
    return render_template('about.html')

# Route to MODELS page


@application.route('/data_summary')
def data_summary():
    return render_template('data_summary.html')

# Run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run(debug=True)
