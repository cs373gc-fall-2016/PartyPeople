""" Models """
# pylint: disable=invalid-name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ppdb'

db = SQLAlchemy(app)


class Candidate(db.Model):
    """ Candidate Model class """
    __tablename__ = "candidate"
    name = db.Column(db.String, primary_key=True)
    dob = db.Column(db.String)
    job = db.Column(db.Integer)
    party = db.Column(db.String)
    elections = db.Column(db.String)
    poll = db.Column(db.Float)
    contact = db.Column(db.String)

    def __repr__(self):
        return '<Candidate %r>' % self.name


class Election(db.Model):
    """ Election Model class """
    __tablename__ = "election"
    name = db.Column(db.String, primary_key=True)
    date = db.Column(db.String)
    level = db.Column(db.Integer)
    location = db.Column(db.String)
    politicians = db.Column(db.String)

    def __repr__(self):
        return '<Candidate %r>' % self.name


class Party(db.Model):
    """ Party Model class """
    __tablename__ = "party"
    name = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)
    politicians = db.Column(db.Integer)
    states = db.Column(db.String)
    hq = db.Column(db.String)
    leader = db.Column(db.String)

    def __repr__(self):
        return '<Party %r>' % self.name


class State(db.Model):
    """ State Model class """
    __tablename__ = "states"
    state_name = db.Column(db.String, primary_key=True)
    capital = db.Column(db.String)
    population = db.Column(db.Integer)
    governor = db.Column(db.String)
    party_affiliation = db.Column(db.String)
    elections = db.Column(db.PickleType)
    reps = db.Column(db.PickleType)

    def __repr__(self):
        return '<State %r>' % self.state_name
