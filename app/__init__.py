from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
# For AWS
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://partypeople:sweatypeople@' \
                                                'partypeople-postgresql.cldmkovirzyt.us-west-2.rds.amazonaws.com:5432/partypeople_database'

# For Local
# application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ppdb'
database = SQLAlchemy(application)