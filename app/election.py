from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ppdb'

db = SQLAlchemy(app)


class Election(db.Model):
    __tablename__ = "election"
    name = db.Column(db.String, primary_key=True)
    date = db.Column(db.String)
    level = db.Column(db.Integer)
    location = db.Column(db.String)
    politicians = db.Column(db.String)

    def __repr__(self):
        return '<Candidate %r>' % self.name
