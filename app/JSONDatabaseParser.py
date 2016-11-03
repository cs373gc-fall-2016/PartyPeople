"""
Module to populate the database
"""

import json
from app import database
from app.models import State, Candidate, Election, Party, ElectoralCollege, ElectionsToState, PartiesInvolved

database.drop_all()
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
                           population=int(state_json[key]['population'].replace(',', '')), governor=state_json[key]['governor'], abbrev=key)
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
    party_ind = Party(name='Independent', leader='None', hq='None', description='None')
    party_npa = Party(name='No Party Affiliation', leader='None', hq='None', description='None')
    database.session.add(party_ind)
    database.session.add(party_npa)
    database.session.commit()
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
            # print("Candidate's State == %r" % state_json[state]['name'])
            candidate_state_query = State.query.filter(State.name == state_json[state]['name']).first()
            # print('Candidate State Query == %r' % candidate_state_query)
            candidate_election_query = Election.query.filter(Election.name == candidate_json[rep]['election']).first()
            # print('Candidate Election Query == %r' % candidate_election_query)
            candidate_party = 'No Party Affiliation'
            if candidate_json[rep]['party'] == 'REP':
                candidate_party = 'Republican Party'
            elif candidate_json[rep]['party'] == 'DEM':
                candidate_party = 'Democratic Party'
            elif candidate_json[rep]['party'] == 'GRE':
                candidate_party = 'Green Party'
            elif candidate_json[rep]['party'] == 'IND':
                candidate_party = 'Independent'
            elif candidate_json[rep]['party'] == 'LIB':
                candidate_party = 'Libertarian Party'
            elif candidate_json[rep]['party'] == 'CON':
                candidate_party = 'The Constitution Party'
            candidate_party_query = Party.query.filter(Party.name == candidate_party).first()
            print('Candidate Party == %r' % candidate_json[rep]['party'])
            temp_candidate.states = candidate_state_query
            temp_candidate.party = candidate_party_query
            temp_candidate.elections = candidate_election_query
            database.session.add(temp_candidate)
            database.session.commit()
            # break
        # break


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
    for election in elections_json.keys():
        temp_parties_involved = PartiesInvolved()
        states_elections = elections_json[election][0]
        for election_name in states_elections.keys():
            parties_involved = set()
            for reps in states_elections[election_name]['candidates']:
                parties_involved.add(states_elections[election_name]['candidates'][reps][1])
            for party in parties_involved:
                party_query = Party.query.filter(Party.name == party).first()
                election_query = Election.query.filter(Election.name == election_name).first()
                temp_parties_involved.elections = election_query
                temp_parties_involved.party = party_query
                database.session.add(temp_parties_involved)
                database.session.commit()


def fill_elections_to_state():
    """This can be done purely with the elections json as the state names are in the election names
        Query Election and States tables
    """
    for election in elections_json.keys():
        temp_election_to_state = ElectionsToState()
        state_name = election[:election.index('-')]
        state_query = State.query.filter(State.abbrev == state_name).first()
        state_elections = elections_json[election][0]
        for key in state_elections.keys():
            print('Election == %r ' % election)
            print('Key == %r' % key)
            election_query = Election.query.filter(Election.name == key).first()
            print(election_query)
            print(state_query)
            temp_election_to_state.elections = election_query
            temp_election_to_state.states = state_query
            database.session.add(temp_election_to_state)
            database.session.commit()
            # break
        # break


if __name__ == '__main__':
    fill_state_table()
    fill_election_table()
    fill_party_table()
    fill_candidate_table()
    fill_elections_to_state()
    # fill_electoral_college()
    # fill_parties_involved()
    # state_query = State.query.all()
    # print(str(state_query).replace(',', ',\n'))

    party_query = Party.query.all()
    print(str(party_query).replace(',', ',\n'))

    # election_query = Election.query.all()
    # print(str(election_query).replace(',', ',\n'))

    candidate_query = Candidate.query.all()
    print(str(candidate_query))

    # electoral_college_query = ElectoralCollege.query.all()
    # print(str(electoral_college_query).replace(',', ',\n'))

    # parties_involved_query = PartiesInvolved.query.all()
    # print(str(parties_involved_query).replace(',', ',\n'))

    elections_to_state_query = ElectionsToState.query.all()
    print(str(elections_to_state_query))
