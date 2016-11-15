
from app.models import Candidate, Party, Election, State
import json
import re

def search_and(term):
	term = str(term).lower()
	print(term)
	r = dict()
	r["candidates"] = search_and_relation(Candidate, term)
	r["elections"] = search_and_relation(Election, term)
	r["states"] = search_and_relation(State, term)
	r["parties"] = search_and_relation(Party, term)
	
	return json.dumps(r, ensure_ascii=False)

def search_or(term):
	term = str(term).lower()
	r = dict()
	r["candidates"] = search_or_relation(Candidate, term)
	r["elections"] = search_or_relation(Election, term)
	r["states"] = search_or_relation(State, term)
	r["parties"] = search_or_relation(Party, term)
	
	return json.dumps(r, ensure_ascii=False)

def search_and_relation(r, term):
	
	d = dict()
	
	if not term or term == "none":
		return d
	
	result = r.query.all()
	
	if result:
		
		exists = False
		for item in result:
			
			temp = dict()
			i = 0
			context = dict()
			for key, value in item.__dict__.items():
				
				key = str(key)
				value = str(value)

				tkey = key.lower()
				tvalue = value.lower()
				temp[key] = value
				
				if not "_sa_instance_state" in tkey and (term in tkey or term in tvalue):
					exists = True
					context[str(i)] = bold_words((key, value), term)
					i = i + 1
					# print("term in " + str(tkey) + " = " + str(tvalue))
			if exists:
				temp["context"] = context
				d[str(item.id)] = temp
				exists = False
	return d

def search_or_relation(r, term):
	
	d = dict()
	
	if not term or term == "none":
		return d
	
	words = re.split(' ', term)
	result = r.query.all()

	if result:
		
		exists = False
		# e_words = list()
		for item in result:
			
			temp = dict()
			i = 0
			context = dict()
			for key, value in item.__dict__.items():
				
				key = str(key)
				value = str(value)
				
				tkey = key.lower()
				tvalue = value.lower()
				temp[key] = value
				
				for word in words:
					if not "_sa_instance_state" in tkey and (word in tkey or word in tvalue):
						exists = True
						context[str(i)] = bold_words((key, value), word)
						i = i + 1
						# print("term in " + str(key) + " = " + str(value))
			if exists:
				temp["context"] = context
				d[str(item.id)] = temp
				exists = False
	return d


def bold_words(t, term):
	context = ""
	words = tuple()

	if term in t[1].lower():
		words = re.split(' ', t[1])

		for word in words:
			if term in word.lower():
				context = context + " " + bold_word(word, term)
			else:
				context = context + " " + word
	else:
		context = bold_word(t[0], term)
	return t[0] + " : " + context

def bold_word(word, term):
	bw = ""
	i = word.lower().find(term)
	if i >= 0:
		bw = word[:i] + '<span class="context"><b>' + word[i:(i+len(term))] + '</b></span>' +  word[(i+len(term)):]
	return bw


