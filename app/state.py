from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ppdb'

db = SQLAlchemy(app)


class State(db.Model):
    __tablename__ = "states"
    state_name = db.Column(db.String, primary_key=True)
    capital = db.Column(db.String)
    population = db.Column(db.Integer)
    governor = db.Column(db.String)
    party_affiliation = db.Column(db.String)
    elections = db.Column(db.PickleType)
    reps = db.Column(db.PickleType)

    def __repr__(self):
        return '<State %r %r %r %r %r %r %r>' %\
               (self.state_name, self.capital, self.population,
                self.governor, self.party_affiliation, self.elections, self.reps)
