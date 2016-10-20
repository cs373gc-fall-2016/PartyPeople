""" Models """
# pylint: disable=invalid-name,line-too-long
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ppdb'

database = SQLAlchemy(application)


class Candidate(database.Model):
    """ Candidate Model class """
    __tablename__ = "candidate"
    name = database.Column(database.String, primary_key=True)
    dob = database.Column(database.DateTime)
    job = database.Column(database.String)
    party = database.Column(database.String)
    elections = database.Column(database.PickleType)
    poll = database.Column(database.Float)
    contact = database.Column(database.String)

    def __repr__(self):
        return '<Candidate %r %r %r %r %r %r %r>' %\
               (self.name, self.dob, self.job, self.party, self.elections, self.poll, self.contact)


class Election(database.Model):
    """ Election Model class """
    __tablename__ = "election"
    name = database.Column(database.String, primary_key=True)
    date = database.Column(database.DateTime)
    level = database.Column(database.String)
    location = database.Column(database.String)
    politicians = database.Column(database.PickleType)

    def __repr__(self):
        return '<Election %r %r %r %r %r>' % (self.name, self.date, self.level, self.location, self.politicians)


class Party(database.Model):
    """ Party Model class """
    __tablename__ = "party"
    name = database.Column(database.String, primary_key=True)
    description = database.Column(database.String)
    politicians = database.Column(database.Integer)
    states = database.Column(database.String)
    hq = database.Column(database.String)
    leader = database.Column(database.String)

    def __repr__(self):
        return '<Party %r %r %r %r %r %r>' % (self.name, self.description, self.politicians, self.states, self.hq, self.leader)


class State(database.Model):
    """ State Model class """
    __tablename__ = "states"
    state_name = database.Column(database.String, primary_key=True)
    capital = database.Column(database.String)
    population = database.Column(database.Integer)
    governor = database.Column(database.String)
    party_affiliation = database.Column(database.String)
    elections = database.Column(database.PickleType)
    reps = database.Column(database.PickleType)

    def __repr__(self):
        return '<State %r %r %r %r %r %r %r>' %\
               (self.state_name, self.capital, self.population,
                self.governor, self.party_affiliation, self.elections, self.reps)
