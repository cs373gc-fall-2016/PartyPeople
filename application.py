from flask import Flask, render_template

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# Return the home page.
@application.route('/')
def index():
    return render_template('index.html')

# Run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run(debug=True)