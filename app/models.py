""" Models """
# pylint: disable=invalid-name,line-too-long,no-member,too-few-public-methods,locally-disabled
# from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

application = Flask(__name__)
database = SQLAlchemy(application)

class Candidate(database.Model):
    """ Candidate Model class """
    __tablename__ = "candidate"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
    dob = database.Column(database.String)
    job = database.Column(database.String)
    contact = database.Column(database.String)
    poll = database.Column(database.Float)
    election_id = database.Column(
        database.Integer, database.ForeignKey('election.id'))
    elections = database.relationship(
        'Election', backref='candidate_election', foreign_keys=[election_id])
    state_id = database.Column(
        database.Integer, database.ForeignKey('state.id'))
    states = database.relationship(
        'State', backref='candidate', foreign_keys=[state_id])
    party_id = database.Column(
        database.Integer, database.ForeignKey('party.id'))
    party = database.relationship(
        'Party', backref='candidate', foreign_keys=[party_id])

    def __repr__(self):
        return '{"Candidate" : {"name": %r, "dob": %r, "job": %r, "poll": %r, "contact": %r, "states": %r, "party": %r, "election": %r}}' %\
               (self.name, self.dob, self.job, self.poll, self.contact, self.states, self.party, self.elections)

    def get_state(self):
        return self.states


class Election(database.Model):
    """ Election Model class """
    __tablename__ = "election"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
    date = database.Column(database.String)
    level = database.Column(database.String)

    def __repr__(self):
        return '<Election %r %r %r>' % (self.name, self.date, self.level)


class Party(database.Model):
    """ Party Model class """
    __tablename__ = "party"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
    description = database.Column(database.String)
    hq = database.Column(database.String)
    leader = database.Column(database.String)

    def __repr__(self):
        return '<Party %r>' % (self.name)


class State(database.Model):
    """ State Model class
    :var id = id of the state in the datbase
    :var name = name of the state
    :var capital Current capital of the state
    :var population total population in the state as of last census
    :var governor Current Governor of the state
    """
    __tablename__ = "state"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
    capital = database.Column(database.String)
    population = database.Column(database.Integer)
    governor = database.Column(database.String)
    abbrev = database.Column(database.String)


    def __repr__(self):
        return '<State %r %r %r %r>' %\
               (self.name, self.capital, self.population,
                self.governor)


class ElectoralCollege(database.Model):
    """
    :Relations = State and Party
    Uses = Determine which party controls which state
    """
    __tablename__ = 'electoral_college'
    id = database.Column(database.Integer, primary_key=True)
    party_id = database.Column(
        database.Integer, database.ForeignKey('party.id'))
    party = database.relationship(
        'Party', backref='electoral', foreign_keys=[party_id])
    state_id = database.Column(
        database.Integer, database.ForeignKey('state.id'))
    states = database.relationship(
        'State', backref='electoral', foreign_keys=[state_id])

    def __repr__(self):
        return '<ElectoralCollege State %r Party %r>' % (self.states, self.party)


class PartiesInvolved(database.Model):
    """
    Relation (Party, Election) many different parties involved in a single election
    """
    __tablename__ = 'parties_involved'
    id = database.Column(database.Integer, primary_key=True)
    party_id = database.Column(
        database.Integer, database.ForeignKey('party.id'))
    party = database.relationship(
        'Party', backref='parties_involved', foreign_keys=[party_id])
    election_id = database.Column(
            database.Integer, database.ForeignKey('election.id'))
    elections = database.relationship(
       'Election', backref='parties_involved', foreign_keys=[election_id])

    def __repr__(self):
        return '<Party %r Election %r>' % (self.party, self.elections)


class ElectionsToState(database.Model):
    __tablename__ = 'election_to_state'
    id = database.Column(database.Integer, primary_key=True)
    election_id = database.Column(
        database.Integer, database.ForeignKey('election.id'))
    elections = database.relationship(
        'Election', backref='election_to_state', foreign_keys=[election_id])
    state_id = database.Column(
        database.Integer, database.ForeignKey('state.id'))
    states = database.relationship(
        'State', backref='election_to_state', foreign_keys=[state_id])

    def __repr__(self):
        return '<ElectionsToStates %r %r>' % (self.elections, self.states)

"""
Have more intermediate tables that will relate the main four models
"""

# # https://flask-restless.readthedocs.io/en/stable/customizing.html
# apimanager = APIManager(application, flask_sqlalchemy_db=database)
# apimanager.create_api(State)
# apimanager.create_api(Party)
# apimanager.create_api(Candidate)
# apimanager.create_api(Election)
# apimanager.create_api(ElectoralCollege)
# apimanager.create_api(PartiesInvolved)