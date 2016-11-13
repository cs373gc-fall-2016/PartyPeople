"""
Module to populate the database
"""

import json
from models import database
from models import State, Candidate, Election, Party, ElectoralCollege, ElectionsToState, PartiesInvolved
from application import create_app

create_app().app_context().push()


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


def party_parser(party_abbrev):
    if party_abbrev == 'REP':
        return 'Republican Party'
    elif party_abbrev == 'DEM':
        return 'Democratic Party'
    elif party_abbrev == 'GRE':
        return 'Green Party'
    elif party_abbrev == 'IND':
        return 'Independent'
    elif party_abbrev == 'LIB':
        return 'Libertarian Party'
    elif party_abbrev == 'CON':
        return 'The Constitution Party'
    else:
        return 'No Party Affiliation'


def fill_state_table():
    """"""
    # rows = []
    counter = 0
    for key in state_json.keys():
        counter += 1
        # print("State %i == %s" % (counter, key))
        temp_state = State(name=state_json[key]['name'], capital=state_json[key]['capital'],
                           population=int(state_json[key]['population'].replace(',', '')),
                           governor=state_json[key]['governor'], abbrev=key)
        database.session.add(temp_state)
        # rows.append(temp_state)
    # for r in rows:
    #     database.session.add(r)
    database.session.commit()


def descriptive_name_parser(election_name):
    """Election name when split gives [State, House/Senate, District]"""
    election_fields = election_name.split("-")
    states_abbrevs = {"AL": "Alabama",
                      "MT": "Montana",
                      "AK": "Alaska",
                      "NE": "Nebraska"	,
                      "AZ": "Arizona",
                      "NV": "Nevada",
                      "AR": "Arkansas"	,
                      "NH": "New Hampshire",
                      "CA": "California",
                      "NJ": "New Jersey",
                      "CO": "Colorado"	,
                      "NM": "New Mexico"	,
                      "CT": "Connecticut"	,
                      "NY": "New York"	,
                      "DE": "Delaware"	,
                      "NC": "North Carolina"	,
                      "FL": "Florida"	,
                      "ND": "North Dakota"	,
                      "GA": "Georgia"	,
                      "OH": "Ohio"	,
                      "HI": "Hawaii"	,
                      "OK": "Oklahoma"	,
                      "ID": "Idaho"	,
                      "OR": "Oregon"	,
                      "IL": "Illinois"	,
                      "PA": "Pennsylvania"	,
                      "IN": "Indiana"	,
                      "RI": "Rhode Island"	,
                      "IA": "Iowa"	,
                      "SC": "South Carolina"	,
                      "KS": "Kansas"	,
                      "SD": "South Dakota"	,
                      "KY": "Kentucky"	,
                      "TN": "Tennessee"	,
                      "LA": "Louisiana"	,
                      "TX": "Texas"	,
                      "ME": "Maine"	,
                      "UT": "Utah"	,
                      "MD": "Maryland"	,
                      "VT": "Vermont"	,
                      "MA": "Massachusetts"	,
                      "VA": "Virginia"	,
                      "MI": "Michigan"	,
                      "WA": "Washington"	,
                      "MN": "Minnesota"	,
                      "WV": "West Virginia"	,
                      "MS": "Mississippi"	,
                      "WI": "Wisconsin"	,
                      "MO": "Missouri"	,
                      "WY": "Wyoming"}
    state_name = states_abbrevs[election_fields[0]]
    race = ''
    if election_fields[1] == "S":
        race = "Senate"
        return "%s, %s" % (state_name, race)
    else:
        race = "House"
    district = "District %s" % election_fields[2]
    return "%s, %s, %s" % (state_name, race, district)


def fill_election_table():
    # rows = []
    counter = 0
    for state_key in elections_json.keys():
        state_elections = elections_json[state_key][0]
        for key in state_elections.keys():
            counter += 1
            # print("Election %i == %s" % (counter, key))
            temp_election = Election(name=key, date=state_elections[key][
                                     'date'], level=state_elections[key]['type'],
                                     descriptive_name=descriptive_name_parser(key))
            database.session.add(temp_election)
            # rows.append(temp_election)
    # for r in rows:
    #     database.session.add(r)
    database.session.commit()


def fill_party_table():
    # rows = []
    party_ind = Party(name='Independent', leader='None',
                      hq='None', description='None', abbrev='IND')
    party_npa = Party(name='No Party Affiliation', leader='None',
                      hq='None', description='None', abbrev='NPA')
    database.session.add(party_ind)
    database.session.add(party_npa)
    for key in party_json.keys():
        temp_party = Party(name=party_json[key]['name'], leader=party_json[key]['leader'],
                           hq=party_json[key]['hq_address'], description=party_json[key]['description'], abbrev=key)
        database.session.add(temp_party)
        # rows.append(temp_party)
    # for r in rows:
    #     database.session.add(r)
    database.session.commit()


def fill_candidate_table():
    """Load the state json file, iterate over all the reps in the state
        for each rep, look up their id in the candidate json file
        use info in candidate json to fill out the State section of the candidate,
        for the other relations, query the already created tables for the values stored in json
    """
    rows = []
    for state in state_json.keys():
        reps = state_json[state]['representatives']
        for rep in reps.keys():
            temp_candidate = Candidate(name=candidate_json[rep]['name'], dob=str(candidate_json[rep]['birthday']), job=candidate_json[
                                       rep]['position'], contact=candidate_json[rep]['contact'], poll=candidate_json[rep]['favorability'])
            candidate_state_query = State.query.filter(
                State.name == state_json[state]['name']).first()
            candidate_election_query = Election.query.filter(
                Election.name == candidate_json[rep]['election']).first()
            candidate_party = party_parser(candidate_json[rep]['party'])
            candidate_party_query = Party.query.filter(
                Party.name == candidate_party).first()
            temp_candidate.states = candidate_state_query
            temp_candidate.party = candidate_party_query
            temp_candidate.elections = candidate_election_query
            database.session.add(temp_candidate)
            # rows.append(temp_candidate)
    # for r in rows:
    #     database.session.add(r)
    database.session.commit()


def fill_electoral_college():
    """Use state json and look at the states controlled tag"""
    # rows = []
    for party in party_json.keys():
        party_controlled_states = party_json[party]['states']
        for state in party_controlled_states.keys():
            temp_electoral = ElectoralCollege()
            state_query = State.query.filter(State.abbrev == state).first()
            party_query = Party.query.filter(Party.abbrev == party).first()
            temp_electoral.party = party_query
            temp_electoral.states = state_query
            temp_electoral.state_name_relationship = state_query
            database.session.add(temp_electoral)
            # rows.append(temp_electoral)
    # for r in rows:
    #     database.session.add(r)
    database.session.commit()


def fill_parties_involved():
    """Fill the table that relates which parties are involved in a given election
        Loop over all the elections and look at the candidates in each election
        Look at what the parties the candidates are from
        In the table create there will be multiple rows with the same election, but will have different parties
    """
    for election in elections_json.keys():
        states_elections = elections_json[election][0]
        for election_name in states_elections.keys():
            parties_involved = set()

            for reps in states_elections[election_name]['candidates']:
                parties_involved.add(states_elections[election_name][
                                     'candidates'][reps][1])
            for party in parties_involved:
                temp_parties_involved = PartiesInvolved()
                party_query = Party.query.filter(Party.abbrev == party).first()
                election_query = Election.query.filter(
                    Election.name == election_name).first()
                temp_parties_involved.elections = election_query
                temp_parties_involved.party = party_query
                database.session.add(temp_parties_involved)
    database.session.commit()


def fill_elections_to_state():
    """This can be done purely with the elections json as the state names are in the election names
        Query Election and States tables
        Right now the behaviour is not working correctly. It is only adding 100 rows instead of 486.
        There are only two rows per each state. One with the election for the Senate, and one of the House
    """
    for election in elections_json.keys():

        state_name = election[:election.index('-')]
        state_query = State.query.filter(State.abbrev == state_name).first()
        state_elections = elections_json[election][0]
        for key in state_elections.keys():
            temp_election_to_state = ElectionsToState()
            election_query = Election.query.filter(
                Election.name == key).first()
            temp_election_to_state.elections = election_query
            temp_election_to_state.states = state_query
            temp_election_to_state.election_name_relationship = election_query
            database.session.add(temp_election_to_state)
    database.session.commit()


if __name__ == '__main__':
    print("Filling State Table")
    fill_state_table()
    print("Filling Election Table")
    fill_election_table()
    print("Filling Party Table")
    fill_party_table()
    print("Filling Candidate Table")
    fill_candidate_table()
    print("Filling Elections to States Table")
    fill_elections_to_state()
    print("Filling Electoral College Table")
    fill_electoral_college()
    print("Filling Parties Involved")
    fill_parties_involved()
    state_query = State.query.all()
    print(state_query)

    party_query = Party.query.all()
    print(party_query)

    election_query = Election.query.all()
    print(election_query)

    candidate_query = Candidate.query.all()
    print(candidate_query)

    electoral_college_query = ElectoralCollege.query.all()
    print(electoral_college_query)

    parties_involved_query = PartiesInvolved.query.all()
    print(parties_involved_query)

    elections_to_state_query = ElectionsToState.query.all()
    print(elections_to_state_query)
