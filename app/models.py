""" Models """
# pylint: disable=invalid-name,line-too-long,no-member,too-few-public-methods,locally-disabled
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ppdb'

database = SQLAlchemy(application)


class Candidate(database.Model):
    """ Candidate Model class """
    __tablename__ = "candidate"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
#     dob = database.Column(database.DateTime)
#     job = database.Column(database.String)
#     election_id = database.Column(
#         database.Integer, database.ForeignKey('election.id'))
#     state_id = database.Column(
#         database.Integer, database.ForeignKey('state.id', use_alter=True, name=''))
#     states = database.relationship(
#         'State', backref='candidate', foreign_keys=[state_id])
#     party_id = database.Column(
#         database.Integer, database.ForeignKey('party.id'))
#     party = database.relationship(
#         'Party', backref='candidate', foreign_keys=[party_id])
#     elections = database.relationship(
#         'Election', backref='candidate_election', foreign_keys=[election_id])
#     poll = database.Column(database.Float)
#     contact = database.Column(database.String)
#
#     def __repr__(self):
#         return '<Candidate %r %r %r %r %r %r %r %r>' %\
#                (self.name, self.dob, self.job, self.party, self.state,
#                 self.elections, self.poll, self.contact)
#
#
class Election(database.Model):
    """ Election Model class """
    __tablename__ = "election"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
#     date = database.Column(database.DateTime)
#     level = database.Column(database.String)
#     candidate_id = database.Column(
#         database.Integer, database.ForeignKey('candidate.id'))
#     state_id = database.Column(
#         database.Integer, database.ForeignKey('state.id'))
#     party_id = database.Column(
#         database.Integer, database.ForeignKey('party.id'))
#     politicians = database.relationship(
#         'Candidate', backref='election', foreign_keys=[candidate_id])
#     state = database.relationship(
#         'State', backref='election_state', foreign_keys=[state_id])
#     party = database.relationship(
#         'Party', backref='election', foreign_keys=[party_id])
#
#     def __repr__(self):
#         return '<Election %r %r %r %r %r>' % (self.name, self.date, self.level, self.location, self.politicians)
#
#
class Party(database.Model):
    """ Party Model class """
    __tablename__ = "party"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
#     description = database.Column(database.String)
#     candidate_id = database.Column(
#         database.Integer, database.ForeignKey('candidate.id'))
#     state_id = database.Column(
#         database.Integer, database.ForeignKey('state.id'))
#     politicians = database.relationship(
#         'Candidate', backref='party', foreign_keys=[candidate_id])
#     state = database.relationship(
#         'State', backref='party_state', foreign_keys=[state_id])
#     hq = database.Column(database.String)
#     leader = database.Column(database.String)
#
#     def __repr__(self):
#         return '<Party %r %r %r %r>' % (self.name, self.description, self.state, self.leader)
#

class State(database.Model):
    """ State Model class """
    __tablename__ = "state"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
    capital = database.Column(database.String)
    population = database.Column(database.Integer)
    governor = database.Column(database.String)
    candidate_id = database.Column(
        database.Integer, database.ForeignKey('candidate.id'))
    candidates = database.relationship(
        'Candidate', backref='state', foreign_keys=[candidate_id])
    # election_id = database.Column(
    #     database.Integer, database.ForeignKey('election.id'))
    # elections = database.relationship(
    #     'Election', backref='state_election', foreign_keys=[])
    # party_id = database.Column(
    #     database.Integer, database.ForeignKey('party.id'))
    # party_affiliation = database.relationship(
    #     'Party', backref='state_party')

    def __repr__(self):
        return '<State %r %r %r %r>' %\
               (self.name, self.capital, self.population,
                self.governor)
