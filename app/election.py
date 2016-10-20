from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ppdb'

database = SQLAlchemy(application)


class Election(database.Model):
    __tablename__ = "election"
    name = database.Column(database.String, primary_key=True)
    date = database.Column(database.DateTime)
    level = database.Column(database.String)
    location = database.Column(database.String)
    politicians = database.Column(database.PickleType)

    def __repr__(self):
        return '<Election %r %r %r %r %r>' % (self.name, self.date, self.level, self.location, self.politicians)
