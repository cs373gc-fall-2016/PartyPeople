from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ppdb'

db = SQLAlchemy(app)


class Party(db.Model):
    __tablename__ = "party"
    name = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)
    politicians = db.Column(db.Integer)
    states = db.Column(db.String)
    hq = db.Column(db.String)
    leader = db.Column(db.String)

    def __repr__(self):
        return '<Party %r>' % self.name
