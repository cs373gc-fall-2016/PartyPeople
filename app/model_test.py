"""
Module for testing models.py
"""
# pylint:disable=invalid-name,line-too-long,no-member,locally-disabled,import-error,too-many-public-methods

from unittest import TestCase
from app.models import State, Party, Candidate, Election, ElectoralCollege, PartiesInvolved, ElectionsToState

from application import create_app

create_app().app_context().push()


class ModelTest(TestCase):
    """ Class for testing models """

    def test_candidate_repr(self):
        """
        Test candidate representation
        """
        cand = Candidate()
        self.assertEqual(cand.__repr__(
        ), '{"Candidate" : {"name": None, "dob": None, "job": None, "poll": None, '
           '"contact": None, "states": None, "party": None, "election": None}}')

    def test_candidate_attributes(self):
        """
        Test the first candidate's attributes
        """
        query = Candidate.query.first()
        self.assertEqual(query.name, 'LOUDERMILK, BARRY')
        self.assertEqual(query.dob, '1963-12-22')
        self.assertEqual(
            query.job, "Representative for Georgia's 11th congressional district")
        self.assertEqual(query.contact['fax'], '202-225-2944')
        self.assertEqual(query.poll, 0.0)

    def test_candidate_relationships_1(self):
        """
        Test the first candidate's election backref
        """
        query = Candidate.query.first()
        election = query.elections
        self.assertEqual(election.date, 'November 8th, 2016')

    def test_candidate_relationships_2(self):
        """
        Test the first candidate's party backref
        """
        query = Candidate.query.first()
        party = query.party
        self.assertEqual(party.name, 'Republican Party')

    def test_candidate_relationships_3(self):
        """
        Test the first candidate's state backref
        """
        query = Candidate.query.first()
        state = query.states
        self.assertEqual(state.name, 'Georgia')

    def test_candidate_by_relationship_filter(self):
        """
        Filter the candidate by the Democratic Party and check its attributes
        """
        query = Candidate.query.join(Party).filter_by(abbrev='DEM').first()
        self.assertEqual(query.name, 'LEWIS, JOHN R.')
        self.assertEqual(query.dob, '1940-02-21')
        self.assertEqual(
            query.job, "Representative for Georgia's 5th congressional district")
        self.assertEqual(query.contact['address'],
                         '343 Cannon HOB; Washington DC 20515-1005')
        self.assertEqual(query.poll, 0.0)

    def test_election_repr(self):
        """
        Test election representation
        """
        elec = Election()
        self.assertEqual(elec.__repr__(
        ), '{"Election" : {"name": None, "date": None, "level": None, "descriptive_name": None}}')

    def test_election_attributes(self):
        """
        Test the first election attributes
        """
        query = Election.query.first()
        self.assertEqual(query.name, 'MO-S-00')
        self.assertEqual(query.date, 'November 8th, 2016')
        self.assertEqual(query.level, 'State - S')
        self.assertEqual(query.descriptive_name, 'Missouri, Senate')

    def test_election_relationships_1(self):
        """
        Test the relationship between candidates by examining the first two candidate names
        """
        query = Election.query.first()
        candidates = query.candidate_election
        cand0 = candidates[0]
        cand1 = candidates[1]
        self.assertEqual(cand0.name, 'BLUNT, ROY')
        self.assertEqual(cand1.name, 'MCCASKILL, CLAIRE')

    def test_election_relationships_2(self):
        """
        Check the party relationship by counting the number of parties
        """
        query = Election.query.first()
        parties = query.parties_involved
        self.assertEqual(len(parties), 2)

    def test_election_relationships_3(self):
        """
        Check the first state relation
        """
        query = Election.query.first()
        election_state = query.election_to_state[0]
        self.assertEqual(election_state.states.name, 'Missouri')

    def test_party_repr(self):
        """
        Test party representation representation
        """
        party = Party()
        self.assertEqual(party.__repr__(
        ), '{Party : {"name": None, "hq": None, "leader": None, "abbrev": None}}')

    def test_party_attributes(self):
        """
        Examine party attributes
        """
        query = Party.query.first()
        self.assertEqual(query.name, 'Independent')
        self.assertEqual(query.hq, 'None')
        self.assertEqual(query.leader, 'None')
        self.assertEqual(query.abbrev, 'IND')

    def test_party_number(self):
        """
        Examine the number of parties
        """
        query = Party.query.all()
        self.assertEqual(len(query), 7)

    def test_party_relation_1(self):
        """
        Check the first candidate relation
        """
        query = Party.query.filter_by(abbrev='IND').first()
        candidates = query.candidate
        cand0 = candidates[0]
        self.assertEqual(cand0.name, 'SANDERS, BERNARD')

    def test_party_relation_2(self):
        """
        Count the number of democratic and republican controlled states
        """
        query1 = Party.query.filter_by(name='Republican Party').first()
        query2 = Party.query.filter_by(abbrev='DEM').first()
        r_states_controlled = query1.electoral
        d_states_controlled = query2.electoral
        self.assertEqual(len(r_states_controlled), 35)
        self.assertEqual(len(d_states_controlled), 15)

    def test_state_repr(self):
        """
        Test state representation representation
        """
        state = State()
        self.assertEqual(state.__repr__(
        ), '{"State" : {"name": None, "capital": None, "population": None, "governor": None, "abbrev": None}}')

    def test_state_attributes(self):
        """
        Assert state attribute values
        """
        query = State.query.filter_by(abbrev='GA').first()
        self.assertEqual(query.name, 'Georgia')
        self.assertEqual(query.capital, 'Atlanta')
        self.assertEqual(query.population, 10214860)
        self.assertEqual(query.governor, 'Nathan Deal')
        self.assertEqual(query.abbrev, 'GA')

    def test_state_number(self):
        """
        Count the number of states
        """
        query = State.query.all()
        self.assertEqual(len(query), 50)

    def test_state_relation(self):
        """
        Test the relationship between elections using the state of Texas
        """
        query = State.query.filter_by(name='Texas').first()
        elections_in_state = query.election_to_state
        first_election = elections_in_state[0].elections
        self.assertEqual(first_election.name, 'TX-S-00')
        self.assertEqual(first_election.date, 'November 8th, 2016')
        self.assertEqual(first_election.level, 'State - S')
        self.assertEqual(first_election.descriptive_name, 'Texas, Senate')

    def test_electoral_college_repr(self):
        """
        Test electoral college representation
        """
        electoral_college = ElectoralCollege()
        self.assertEqual(electoral_college.__repr__(),
                         '{ElectoralCollege : { "State": None, "Party": None}}')

    def test_electoral_college_1(self):
        """
        Test of the electoral college to see if the Name of the State and Party are the same as expected
        """
        query = ElectoralCollege.query.filter(
            ElectoralCollege.state_name == "Georgia").first()
        self.assertEqual(query.states.name, "Georgia")
        self.assertEqual(query.party.name, "Republican Party")

    def test_electoral_college_2(self):
        """
        Test to see if the attributes in the electoral college are the same as the rows in the main models
        """
        electoral_query = ElectoralCollege.query.filter(
            ElectoralCollege.state_name == "Georgia").first()
        party_query = Party.query.filter(
            Party.name == "Republican Party").first()
        state_query = State.query.filter(State.name == "Georgia").first()
        self.assertEqual(electoral_query.states, state_query)
        self.assertEqual(electoral_query.party, party_query)

    def test_electoral_college_3(self):
        """
        Test to see if two different rows in the electoral college share the same row from party (Many to One)
        """
        electoral_query_1 = ElectoralCollege.query.filter(
            ElectoralCollege.state_name == "Georgia").first()
        electoral_query_2 = ElectoralCollege.query.filter(
            ElectoralCollege.state_name == "Texas").first()
        party_query = Party.query.filter(
            Party.name == "Republican Party").first()
        self.assertEqual(electoral_query_1.party, party_query)
        self.assertEqual(electoral_query_2.party, party_query)

    def test_parties_involved_repr(self):
        """
        Test parties involved representation
        """
        parties_involved = PartiesInvolved()
        self.assertEqual(parties_involved.__repr__(
        ), '{"PartiesInvolved": {"Party": None, "Election": None}}')

    def test_parties_involved_1(self):
        """
        Test of the Parties Involved Model to see if the Name of the Election and Party are the same as expected
        """
        query = PartiesInvolved.query.filter(
            PartiesInvolved.election_id == 1).first()
        self.assertEqual(query.party.name, "Republican Party")
        self.assertEqual(query.elections.name, "MO-S-00")

    def test_parties_involved_2(self):
        """
        Test to see if the attributes in the Parties Involved Model are the same as the rows in the main models
        """
        involved_query = PartiesInvolved.query.filter(
            PartiesInvolved.election_id == 1).first()
        party_query = Party.query.filter(
            Party.name == "Republican Party").first()
        election_query = Election.query.filter(
            Election.name == "MO-S-00").first()
        self.assertEqual(involved_query.elections, election_query)
        self.assertEqual(involved_query.party, party_query)

    def test_parties_involved_3(self):
        """
        Test to see if two different rows in the Parties Involved Model share the same row from party (Many to One)
        """
        involved_query_1 = PartiesInvolved.query.filter(
            PartiesInvolved.election_id == 1).first()
        involved_query_2 = PartiesInvolved.query.filter(
            PartiesInvolved.election_id == 3).first()
        party_query = Party.query.filter(
            Party.name == "Republican Party").first()
        self.assertEqual(involved_query_1.party, party_query)
        self.assertEqual(involved_query_2.party, party_query)

    def test_elections_to_state_repr(self):
        """
        Test election to state representation
        """
        elections_to_state = ElectionsToState()
        self.assertEqual(elections_to_state.__repr__(
        ), '{"ElectionsToStates" : {"elections": None, "states":None}}')

    def test_elections_to_state_1(self):
        """
        Test of the Elections to State Model to see if the Name of the Election and Party are the same as expected
        """
        query = ElectionsToState.query.filter(
            ElectionsToState.election_id == 1).first()
        self.assertEqual(query.state_name, "Missouri")
        self.assertEqual(query.elections.name, "MO-S-00")

    def test_elections_to_state_2(self):
        """
        Test to see if the attributes in the Elections to State Model are the same as the rows in the main models
        """
        elections_to_state_query = ElectionsToState.query.filter(
            ElectionsToState.election_id == 1).first()
        state_query = State.query.filter(State.name == "Missouri").first()
        election_query = Election.query.filter(
            Election.name == "MO-S-00").first()
        self.assertEqual(elections_to_state_query.elections, election_query)
        self.assertEqual(elections_to_state_query.states, state_query)

    def test_elections_to_state_3(self):
        """
        Test to see if two different rows in the Elections To State Model share the same row from party (Many to One)
        """
        elections_to_states_1 = ElectionsToState.query.filter(
            ElectionsToState.election_id == 1).first()
        elections_to_states_2 = ElectionsToState.query.filter(
            ElectionsToState.election_id == 330).first()
        state_query = State.query.filter(State.name == "Missouri").first()
        self.assertEqual(elections_to_states_1.states, state_query)
        self.assertEqual(elections_to_states_2.states, state_query)
