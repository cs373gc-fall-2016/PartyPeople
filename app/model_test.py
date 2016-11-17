"""
Module for testing models
"""
# pylint: disable=invalid-name,line-too-long,no-member,locally-disabled

from unittest import TestCase
from app.models import State, Party, Candidate, database, Election, ElectoralCollege, PartiesInvolved, ElectionsToState

class ModelTest(TestCase):
    """ Class for testing models """

    def setUp(self):
        """Set up the database and the Models for testing
        Will have multiple of each type of model to be placed in the tables, to test different types of relationships
        """
        pass

    def tearDown(self):
        """Drop all the tables so on subsequent tests it doesn't complain that elements already exist"""
        pass

    def test_candidate_attributes(self):
        query = Candidate.query.first()
        self.assertEqual(query.name, 'LOUDERMILK, BARRY')
        self.assertEqual(query.dob, '1963-12-22')
        self.assertEqual(query.job, "Representative for Georgia's 11th congressional district")
        self.assertEqual(query.contact['fax'], '202-225-2944')
        self.assertEqual(query.poll, 0.0)

    def test_candidate_relationships_1(self):
        query = Candidate.query.first()
        election = query.elections
        self.assertEqual(election.date, 'November 8th, 2016')

    def test_candidate_relationships_2(self):
        query = Candidate.query.first()
        party = query.party
        self.assertEqual(party.name, 'Republican Party')

    def test_candidate_relationships_3(self):
        query = Candidate.query.first()
        state = query.states
        self.assertEqual(state.name, 'Georgia')

    def test_candidate_by_relationship_filter(self):
        query = Candidate.query.join(Party).filter_by(abbrev='DEM').first()
        self.assertEqual(query.name, 'LEWIS, JOHN R.')
        self.assertEqual(query.dob, '1940-02-21')
        self.assertEqual(query.job, "Representative for Georgia's 5th congressional district")
        self.assertEqual(query.contact['address'], '343 Cannon HOB; Washington DC 20515-1005')
        self.assertEqual(query.poll, 0.0)

    def test_election_attributes(self):
        query = Election.query.first()
        self.assertEqual(query.name, 'MO-S-00')
        self.assertEqual(query.date, 'November 8th, 2016')
        self.assertEqual(query.level, 'State - S')
        self.assertEqual(query.descriptive_name, 'Missouri, Senate')
        
        # x = Dish.query.filter(Dish.restaurants.any(name=name)).all()

    def test_election_relationships_1(self):
        query = Election.query.first()
        candidates = query.candidate_election
        cand0 = candidates[0]
        cand1 = candidates[1]
        self.assertEqual(cand0.name, 'BLUNT, ROY')
        self.assertEqual(cand1.name, 'MCCASKILL, CLAIRE')

    def test_election_relationships_2(self):
        query = Election.query.first()
        parties = query.parties_involved
        self.assertEqual(len(parties), 2)

    def test_election_relationships_3(self):
        query = Election.query.first()
        election_state = query.election_to_state[0]
        self.assertEqual(election_state.states.name, 'Missouri')

    # def test_state(self):
    #     """ Test state model
    #         Test if only a single file is being put in and retrieved
    #     """
    #     print('Running State Model Test')
    #     state = self.state_1
    #     # state.party_affiliation = self.party
    #     database.session.add(state)
    #     database.session.commit()
    #     query = State.query.first()
    #     print(query)
    #     self.assertEqual(query.name, state.name)
    #     self.assertEqual(query, state)

    # def test_state_2(self):
    #     """
    #     Test if multiple states are committed to a database, then they are all returned on a query
    #     :return:
    #     """
    #     state_1 = self.state_1
    #     state_2 = self.state_2
    #     database.session.add(state_1)
    #     database.session.add(state_2)
    #     database.session.commit()
    #     query = State.query.all()
    #     print(State.query.all())
    #     self.assertIn(state_1, query)
    #     self.assertIn(state_2, query)

    # def test_state_3(self):
    #     """
    #     Test if multiple states are added to a database, then they can be queried by one of their attributes
    #     :return:
    #     """
    #     state_1 = self.state_1
    #     state_2 = self.state_2
    #     state_3 = self.state_3
    #     database.session.add(state_1)
    #     database.session.add(state_2)
    #     database.session.add(state_3)
    #     database.session.commit()
    #     query = State.query.filter_by(population=1000).all()
    #     print(query)
    #     self.assertIn(state_1, query)
    #     self.assertIn(state_3, query)

    # def test_election_1(self):
    #     """ Test election model basics"""
    #     print('Running Election Model Test')
    #     election_1 = self.election_1
    #     database.session.add(election_1)
    #     database.session.commit()
    #     query = Election.query.first()
    #     print(query)
    #     self.assertEqual(query.name, election_1.name)
    #     self.assertEqual(query, election_1)

    # def test_election_2(self):
    #     """
    #     Test if multiple elections can be committed to a table and queried
    #     :return:
    #     """
    #     election_1 = self.election_1
    #     election_2 = self.election_2
    #     database.session.add(election_1)
    #     database.session.add(election_2)
    #     database.session.commit()
    #     query = Election.query.all()
    #     print(query)
    #     self.assertIn(election_1, query)
    #     self.assertIn(election_2, query)

    # def test_election_3(self):
    #     """
    #     Test if the elections can be added and queried by one of their attribures
    #     :return:
    #     """
    #     election_1 = self.election_1
    #     election_2 = self.election_2
    #     election_3 = self.election_3
    #     election_4 = self.election_4
    #     database.session.add(election_1)
    #     database.session.add(election_2)
    #     database.session.add(election_3)
    #     database.session.add(election_4)
    #     database.session.commit()
    #     query = Election.query.filter_by(level='local').all()
    #     print(query)
    #     self.assertIn(election_2, query)
    #     self.assertIn(election_3, query)

    # def test_party_1(self):
    #     """ Test state model, if something can be added in and queried """
    #     print('Running Election Model Test')
    #     party_1 = self.party_1
    #     database.session.add(party_1)
    #     database.session.commit()
    #     query = Party.query.first()
    #     print(query)
    #     self.assertEqual(query.name, party_1.name)
    #     self.assertEqual(query, party_1)

    # def test_party_2(self):
    #     """
    #     Test if multiple states are committed to a database, then they are all returned on a query
    #     """
    #     party_1 = self.party_1
    #     party_2 = self.party_2
    #     database.session.add(party_1)
    #     database.session.add(party_2)
    #     database.session.commit()
    #     query = Party.query.all()
    #     print(query)
    #     self.assertIn(party_1, query)
    #     self.assertIn(party_2, query)

    # def test_party_3(self):
    #     """
    #     Test if the parties can be queried by attributes
    #     :return:
    #     """
    #     party_1 = self.party_1
    #     party_2 = self.party_2
    #     party_3 = self.party_3
    #     database.session.add(party_1)
    #     database.session.add(party_2)
    #     database.session.add(party_3)
    #     database.session.commit()
    #     query = Party.query.filter_by(hq='hq_1').all()
    #     print(query)
    #     self.assertIn(party_1, query)
    #     self.assertIn(party_3, query)

    # def test_electoral_college(self):
    #     """
    #     Test the intermediate table for states and the parties that control them,
    #     this also tests the results of a join are non empty
    #     """
    #     print("Running the Electoral College Test")
    #     party_1 = self.party_1
    #     party_2 = self.party_2
    #     party_3 = self.party_3
    #     relation_1 = ElectoralCollege()
    #     relation_2 = ElectoralCollege()
    #     relation_3 = ElectoralCollege()

    #     relation_1.party = self.party_1
    #     relation_1.states = self.state_1

    #     relation_2.party = self.party_1
    #     relation_2.states = self.state_2

    #     relation_3.party = self.party_2
    #     relation_3.states = self.state_3

    #     database.session.add(relation_1)
    #     database.session.add(relation_2)
    #     database.session.add(relation_3)
    #     database.session.add(party_1)
    #     database.session.add(party_2)
    #     database.session.add(party_3)
    #     database.session.commit()
    #     joined_table = ElectoralCollege.query.join(Party, State).add_columns(Party.name, State.name).all()
    #     print('Joined Table %r' % joined_table)
    #     select = ElectoralCollege.query.filter_by(party=self.party_1).all()
    #     print('SELECT %r' % select)
    #     self.assertIsNotNone(joined_table)

    # def test_parties_involved(self):
    #     """
    #     Test the intermediate table for states and the parties that control them,
    #     this also tests the results of a join are non empty

    #     :return:
    #     """
    #     relation_1 = PartiesInvolved(party=self.party_1, elections=self.election_1)
    #     relation_2 = PartiesInvolved(party=self.party_2, elections=self.election_1)
    #     relation_3 = PartiesInvolved(party=self.party_1, elections=self.election_2)
    #     relation_4 = PartiesInvolved(party=self.party_2, elections=self.election_2)
    #     database.session.add(relation_1)
    #     database.session.add(relation_2)
    #     database.session.add(relation_3)
    #     database.session.add(relation_4)
    #     database.session.commit()
    #     joined_table = PartiesInvolved.query.join(Election, Party).add_columns(Election.name, Party.name).all()
    #     print("JOINED TABLE %r" % joined_table)
    #     self.assertIsNotNone(joined_table)

    # def test_elections_to_states(self):
    #     """
    #     Test the intermediate table for elections and the states they are held in
    #     this also tests the results of a join are non empty
    #     :return:
    #     """
    #     relation_1 = ElectionsToState(elections=self.election_1, states=self.state_1)
    #     relation_2 = ElectionsToState(elections=self.election_2, states=self.state_2)
    #     relation_3 = ElectionsToState(elections=self.election_1, states=self.state_2)
    #     relation_4 = ElectionsToState(elections=self.election_1, states=self.state_3)
    #     database.session.add(relation_1)
    #     database.session.add(relation_2)
    #     database.session.add(relation_3)
    #     database.session.add(relation_4)
    #     database.session.commit()
    #     joined_table = ElectionsToState().query.join(Election, State).add_columns(Election.name, State.name).all()
    #     print("JOINED TABLE : ElectionsToStates %r" % joined_table)
    #     self.assertIsNotNone(joined_table)