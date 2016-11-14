
from app.models import Candidate, Party, Election, State
import json
import re

def search_and(term):
	term = str(term).lower()
	r = dict()
	r["candidates"] = search_and_relation(Candidate, term)
	r["elections"] = search_and_relation(Election, term)
	r["states"] = search_and_relation(State, term)
	r["parties"] = search_and_relation(Party, term)
	# r = {"Candidates" : candidates, "Elections" : elections, "States" : states, "Parties" : parties}
	
	return json.dumps(r, ensure_ascii=False)
	# return "searching..."

def search_or(term):
	term = str(term).lower()
	r = dict()
	r["candidates"] = search_or_relation(Candidate, term)
	r["elections"] = search_or_relation(Election, term)
	r["states"] = search_or_relation(State, term)
	r["parties"] = search_or_relation(Party, term)
	# r = {"Candidates" : candidates, "Elections" : elections, "States" : states, "Parties" : parties}
	
	return json.dumps(r, ensure_ascii=False)
	# return "searching..."

def search_and_relation(r, term):
	result = r.query.all()
	d = dict()
	if result:
		exists = False
		for item in result:
			temp = dict()
			for key, value in item.__dict__.items():
				key = str(key).lower()
				value = str(value).lower()
				temp[key] = value
				if term in key or term in value:
					exists = True
					print("term in " + str(key) + " = " + str(value))
			if exists:
				d[str(item.id)] = temp
				exists = False
	return d

def search_or_relation(r, term):
	words = re.split(' ', term)
	result = r.query.all()
	d = dict()
	if result:
		exists = False
		# e_words = list()
		for item in result:
			temp = dict()
			for key, value in item.__dict__.items():
				key = str(key).lower()
				value = str(value).lower()
				temp[key] = value
				for word in words:
					if word in key or word in value:
						exists = True
						print("term in " + str(key) + " = " + str(value))
			if exists:
				d[str(item.id)] = temp
				exists = False
	return d