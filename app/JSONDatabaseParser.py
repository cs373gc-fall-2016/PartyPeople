"""
Module to populate the database
"""

# pylint:
# disable=invalid-name,line-too-long,no-member,bad-continuation,superfluous-parens,too-many-return-statements


import json
from models import database
from models import State, Candidate, Election, Party, ElectoralCollege, ElectionsToState, PartiesInvolved
from application import create_app

create_app().app_context().push()


database.drop_all()
database.create_all()

STATE_FILE = open('states.json')
STATE_JSON = json.loads(STATE_FILE.read())

CANDIDATE_FILE = open('candidates.json')
CANDIDATE_JSON = json.loads(CANDIDATE_FILE.read())

PARTY_FILE = open('parties.json')
PARTY_JSON = json.loads(PARTY_FILE.read())

ELECTION_FILE = open('elections.json')
ELECTION_JSON = json.loads(ELECTION_FILE.read())


def party_parser(party_abbrev):
    """IF/ELSE to give actual name of party instead of three letter abbreviation"""
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
    """
    Fill state table with information from state.json
    :return:
    """
    counter = 0
    for key in STATE_JSON.keys():
        counter += 1
        temp_state = State(name=STATE_JSON[key]['name'], capital=STATE_JSON[key]['capital'],
                           population=int(STATE_JSON[key][
                                          'population'].replace(',', '')),
                           governor=STATE_JSON[key]['governor'], abbrev=key)
        database.session.add(temp_state)
    database.session.commit()


def descriptive_name_parser(election_name):
    """Election name when split gives [State, House/Senate, District]
        Turn it into a more human readable form
    """
    election_fields = election_name.split("-")
    states_abbrevs = {"AL": "Alabama",
                      "MT": "Montana",
                      "AK": "Alaska",
                      "NE": "Nebraska",
                      "AZ": "Arizona",
                      "NV": "Nevada",
                      "AR": "Arkansas",
                      "NH": "New Hampshire",
                      "CA": "California",
                      "NJ": "New Jersey",
                      "CO": "Colorado",
                      "NM": "New Mexico",
                      "CT": "Connecticut",
                      "NY": "New York",
                      "DE": "Delaware",
                      "NC": "North Carolina",
                      "FL": "Florida",
                      "ND": "North Dakota",
                      "GA": "Georgia",
                      "OH": "Ohio",
                      "HI": "Hawaii",
                      "OK": "Oklahoma",
                      "ID": "Idaho",
                      "OR": "Oregon",
                      "IL": "Illinois",
                      "PA": "Pennsylvania",
                      "IN": "Indiana",
                      "RI": "Rhode Island",
                      "IA": "Iowa",
                      "SC": "South Carolina",
                      "KS": "Kansas",
                      "SD": "South Dakota",
                      "KY": "Kentucky",
                      "TN": "Tennessee",
                      "LA": "Louisiana",
                      "TX": "Texas",
                      "ME": "Maine",
                      "UT": "Utah",
                      "MD": "Maryland",
                      "VT": "Vermont",
                      "MA": "Massachusetts",
                      "VA": "Virginia",
                      "MI": "Michigan",
                      "WA": "Washington",
                      "MN": "Minnesota",
                      "WV": "West Virginia",
                      "MS": "Mississippi",
                      "WI": "Wisconsin",
                      "MO": "Missouri",
                      "WY": "Wyoming"}
    state_name = states_abbrevs[election_fields[0]]
    if election_fields[1] == "S":
        race = "Senate"
        return "%s, %s" % (state_name, race)
    else:
        race = "House"
    district = "District %s" % election_fields[2]
    return "%s, %s, %s" % (state_name, race, district)


def fill_election_table():
    """
    fills the election table with data from elections.json
    :return:
    """
    counter = 0
    for state_key in ELECTION_JSON.keys():
        state_elections = ELECTION_JSON[state_key][0]
        for key in state_elections.keys():
            counter += 1
            # print("Election %i == %s" % (counter, key))
            temp_election = Election(name=key, date=state_elections[key][
                                     'date'], level=state_elections[key]['type'],
                                     descriptive_name=descriptive_name_parser(key))
            database.session.add(temp_election)
    database.session.commit()


def fill_party_table():
    """
    Fill party table with information from party.json
    :return:
    """
    party_ind = Party(name='Independent', leader='None',
                      hq='None', description='None', abbrev='IND')
    party_npa = Party(name='No Party Affiliation', leader='None',
                      hq='None', description='None', abbrev='NPA')
    database.session.add(party_ind)
    database.session.add(party_npa)
    for key in PARTY_JSON.keys():
        temp_party = Party(name=PARTY_JSON[key]['name'], leader=PARTY_JSON[key]['leader'],
                           hq=PARTY_JSON[key]['hq_address'], description=PARTY_JSON[key]['description'], abbrev=key)
        database.session.add(temp_party)
    database.session.commit()


def fill_candidate_table():
    """Load the state json file, iterate over all the reps in the state
        for each rep, look up their id in the candidate json file
        use info in candidate json to fill out the State section of the candidate,
        for the other relations, query the already created tables for the values stored in json
    """
    for state in STATE_JSON.keys():
        reps = STATE_JSON[state]['representatives']
        for rep in reps.keys():
            temp_candidate = Candidate(name=CANDIDATE_JSON[rep]['name'], dob=str(CANDIDATE_JSON[rep]['birthday']),
                                       job=CANDIDATE_JSON[rep][
                                           'position'], contact=CANDIDATE_JSON[rep]['contact'],
                                       poll=CANDIDATE_JSON[rep]['favorability'])
            candidate_state_query = State.query.filter(
                State.name == STATE_JSON[state]['name']).first()
            candidate_election_query = Election.query.filter(
                Election.name == CANDIDATE_JSON[rep]['election']).first()
            candidate_party = party_parser(CANDIDATE_JSON[rep]['party'])
            candidate_party_query = Party.query.filter(
                Party.name == candidate_party).first()
            temp_candidate.states = candidate_state_query
            temp_candidate.party = candidate_party_query
            temp_candidate.elections = candidate_election_query
            database.session.add(temp_candidate)
    database.session.commit()


def fill_electoral_college():
    """Use state json and look at the states controlled tag"""
    for party in PARTY_JSON.keys():
        party_controlled_states = PARTY_JSON[party]['states']
        for state in party_controlled_states.keys():
            temp_electoral = ElectoralCollege()
            state_query = State.query.filter(State.abbrev == state).first()
            party_query = Party.query.filter(Party.abbrev == party).first()
            temp_electoral.party = party_query
            temp_electoral.states = state_query
            temp_electoral.state_name_relationship = state_query
            database.session.add(temp_electoral)
    database.session.commit()


def fill_parties_involved():
    """Fill the table that relates which parties are involved in a given election
        Loop over all the elections and look at the candidates in each election
        Look at what the parties the candidates are from
        In the table create there will be multiple rows with the same election, but will have different parties
    """
    for election in ELECTION_JSON.keys():
        states_elections = ELECTION_JSON[election][0]
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
                temp_parties_involved.party_name_relationship = party_query
                database.session.add(temp_parties_involved)
    database.session.commit()


def fill_elections_to_state():
    """This can be done purely with the elections json as the state names are in the election names
        Query Election and States tables
        Right now the behaviour is not working correctly. It is only adding 100 rows instead of 486.
        There are only two rows per each state. One with the election for the Senate, and one of the House
    """
    for election in ELECTION_JSON.keys():

        state_name = election[:election.index('-')]
        state_query = State.query.filter(State.abbrev == state_name).first()
        state_elections = ELECTION_JSON[election][0]
        for key in state_elections.keys():
            temp_election_to_state = ElectionsToState()
            election_query = Election.query.filter(
                Election.name == key).first()
            temp_election_to_state.elections = election_query
            temp_election_to_state.states = state_query
            temp_election_to_state.election_name_relationship = election_query
            temp_election_to_state.state_name_relationship = state_query
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
    STATE_QUERY = State.query.all()
    print(STATE_QUERY)

    PARTY_QUERY = Party.query.all()
    print(PARTY_QUERY)

    ELECTION_QUERY = Election.query.all()
    print(ELECTION_QUERY)

    CANDIDATE_QUERY = Candidate.query.all()
    print(CANDIDATE_QUERY)

    ELECTORAL_COLLEGE_QUERY = ElectoralCollege.query.all()
    print(ELECTORAL_COLLEGE_QUERY)

    PARTIES_INVOLVED_QUERY = PartiesInvolved.query.all()
    print(PARTIES_INVOLVED_QUERY)

    ELECTION_TO_STATE_QUERY = ElectionsToState.query.all()
    print(ELECTION_TO_STATE_QUERY)
