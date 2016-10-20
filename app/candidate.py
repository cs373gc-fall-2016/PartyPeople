from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ppdb'

db = SQLAlchemy(app)


class Candidate(db.Model):
    __tablename__ = "candidate"
    name = db.Column(db.String, primary_key=True)
    dob = db.Column(db.DateTime)
    job = db.Column(db.String)
    party = db.Column(db.String)
    elections = db.Column(db.PickleType)
    poll = db.Column(db.Float)
    contact = db.Column(db.String)

    def __repr__(self):
        return '<Candidate %r %r %r %r %r %r %r>' %\
               (self.name, self.dob, self.job, self.party, self.elections, self.poll, self.contact)
