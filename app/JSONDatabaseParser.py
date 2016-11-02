"""
Module to populate the database
"""

import json
from app import database
from app.models import State, Candidate, Election, Party, ElectoralCollege, ElectionsToState, PartiesInvolved

database.create_all()

state_file = open('states.json')
state_json = json.loads(state_file.read())

candidate_file = open('candidates.json')
candidate_json = json.loads(candidate_file.read())

party_file = open('parties.json')
party_json = json.loads(party_file.read())

election_file = open('elections.json')
elections_json = json.loads(election_file.read())


def fill_state_table():

    for key in state_json.keys():
        temp_state = State(name=state_json[key]['name'], capital=state_json[key]['capital'],
                           population=int(state_json[key]['population'].replace(',', '')), governor=state_json[key]['governor'])
        database.session.add(temp_state)
        database.session.commit()


def fill_election_table():
    for state_key in elections_json.keys():
        state_elections = elections_json[state_key][0]
        for key in state_elections.keys():
            temp_election = Election(name=key, date=state_elections[key]['date'], level=state_elections[key]['type'])
            database.session.add(temp_election)
            database.session.commit()


def fill_party_table():
    for key in party_json.keys():
        temp_party = Party(name=party_json[key]['name'], leader=party_json[key]['leader'],
                           hq=party_json[key]['hq_address'], description=party_json[key]['description'])
        database.session.add(temp_party)
        database.session.commit()


def fill_candidate_table():
    """Load the state json file, iterate over all the reps in the state
        for each rep, look up their id in the candidate json file
        use info in candidate json to fill out the State section of the candidate,
        for the other relations, query the already created tables for the values stored in json
    """
    for state in state_json.keys():
        reps = state_json[state]['representatives']
        for rep in reps.keys():
            temp_candidate = Candidate(name=candidate_json[rep]['name'], dob=str(candidate_json[rep]['birthday']), job=candidate_json[rep]['position']
                                       , contact=str(candidate_json[rep]['contact']), poll=candidate_json[rep]['favorability'])
            candidate_state_query = State.query.filter(State.name == state).first()
            candidate_election_query = Election.query.filter(Election.name == candidate_json[rep]['election']).first()
            candidate_party_query = Party.query.filter(Party.name == candidate_json[rep]['party']).first()
            temp_candidate.states = candidate_state_query
            temp_candidate.party = candidate_party_query
            temp_candidate.elections = candidate_election_query
            database.session.add(temp_candidate)
            database.session.commit()


def fill_electoral_college():
    """Use state json and look at the states controlled tag"""
    for party in party_json.keys():
        party_controlled_states = party_json[party]['states']
        for state in party_controlled_states.keys():
            temp_electoral = ElectoralCollege()
            state_query = State.query.filter(State.name == state).first()
            party_query = Party.query.filter(Party.name == party).first()
            temp_electoral.party = party_query
            temp_electoral.states = state_query
            database.session.add(temp_electoral)
            database.session.commit()


def fill_parties_involved():
    """Fill the table that relates which parties are involved in a given election
        Loop over all the elections and look at the candidates in each election
        Look at what the parties the candidates are from
        In the table create there will be multiple rows with the same election, but will have different parties
    """

    pass


def fill_elections_to_state():
    """This can be done purely with the elections json as the state names are in the election names"""
    pass


if __name__ == '__main__':
    fill_state_table()
    fill_election_table()
    fill_party_table()
    fill_candidate_table()
    query = State.query.first()
    print(query)
    candidate = Candidate(name='candidate', dob='12-16-1994', job='job', contact='come@me', poll=0.0)
    candidate.states = query
    print(candidate)
    print(candidate.get_state())