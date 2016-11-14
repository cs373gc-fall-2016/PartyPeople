"""
Module for testing models
"""
# pylint: disable=invalid-name,line-too-long,no-member,locally-disabled

import unittest
from app.models import State, Party, Candidate, database, Election, ElectoralCollege, PartiesInvolved, ElectionsToState


class ModelTest(unittest.TestCase):
    """ Class for testing models """

    def setUp(self):
        """Set up the database and the Models for testing
        Will have multiple of each type of model to be placed in the tables, to test different types of relationships
        """
        database.create_all()
        self.candidate_1 = Candidate(name="Candidate_1", dob=None, job='politician',
                                     contact='candidate1@us.gov', poll=50.0)
        self.candidate_2 = Candidate(name="Candidate_2", dob=None, job='politician',
                                     contact='candidate2@us.gov', poll=75.0)
        self.candidate_3 = Candidate(name="Candidate_3", dob=None, job='governor',
                                     contact='candidate3@us.gov', poll=50.0)

        self.election_1 = Election(name="general", date=None, level='federal')
        self.election_2 = Election(name="local_1", date=None, level='local')
        self.election_3 = Election(name="local_2", date=None, level='local')
        self.election_4 = Election(name="state", date=None, level='state')

        self.state_1 = State(name='State_1', capital='Capital_1', population=1000)
        self.state_2 = State(name='State_2', capital='Capital_2', population=2000)
        self.state_3 = State(name='State_3', capital='Capital_3', population=1000)

        self.party_1 = Party(name="Party_1", description='party people', hq='hq_1', leader='leader_1')
        self.party_2 = Party(name="Party_2", description='people party', hq='hq_2', leader='leader_2')
        self.party_3 = Party(name="Party_3", description='people people', hq='hq_1', leader='leader_3')

    def tearDown(self):
        """Drop all the tables so on subsequent tests it doesn't complain that elements already exist"""
        database.session.close()
        database.reflect()
        database.drop_all()
        # Using the drop all command will give an 'index out of bounds error'
        # Without the drop test will fail because it might not be testing the same table that was just placed in
        # Can drop when the table is just freshly created

    def test_state(self):
        """ Test state model
            Test if only a single file is being put in and retrieved
        """
        print('Running State Model Test')
        state = self.state_1
        # state.party_affiliation = self.party
        database.session.add(state)
        database.session.commit()
        query = State.query.first()
        print(query)
        self.assertEqual(query.name, state.name)
        self.assertEqual(query, state)

    def test_state_2(self):
        """
        Test if multiple states are committed to a database, then they are all returned on a query
        :return:
        """
        state_1 = self.state_1
        state_2 = self.state_2
        database.session.add(state_1)
        database.session.add(state_2)
        database.session.commit()
        query = State.query.all()
        print(State.query.all())
        self.assertIn(state_1, query)
        self.assertIn(state_2, query)

    def test_state_3(self):
        """
        Test if multiple states are added to a database, then they can be queried by one of their attributes
        :return:
        """
        state_1 = self.state_1
        state_2 = self.state_2
        state_3 = self.state_3
        database.session.add(state_1)
        database.session.add(state_2)
        database.session.add(state_3)
        database.session.commit()
        query = State.query.filter_by(population=1000).all()
        print(query)
        self.assertIn(state_1, query)
        self.assertIn(state_3, query)

    def test_candidate_1(self):
        """ Test state model , adding and committing a single candidate row"""
        print('Running State Model Test')
        candidate_1 = self.candidate_1
        # candidate_1.party = self.party
        database.session.add(candidate_1)
        database.session.commit()
        query = Candidate.query.first()
        print(query)
        self.assertEqual(query.name, candidate_1.name)
        self.assertEqual(query, candidate_1)

    def test_candidate_2(self):
        """
        Test if multiple candidates are committed to a database, then they are all returned on a query
        """
        candidate_1 = self.candidate_1
        candidate_2 = self.candidate_2
        database.session.add(candidate_1)
        database.session.add(candidate_2)
        database.session.commit()
        query = Candidate.query.all()
        self.assertIn(candidate_1, query)
        self.assertIn(candidate_2, query)

    def test_candidate_3(self):
        """
        Test if multiple candidates can be committed and queried based on an attribute
        :return:
        """
        candidate_1 = self.candidate_1
        candidate_2 = self.candidate_2
        candidate_3 = self.candidate_3
        database.session.add(candidate_1)
        database.session.add(candidate_2)
        database.session.add(candidate_3)
        database.session.commit()
        query = Candidate.query.filter_by(job='politician').all()
        print(query)
        self.assertIn(candidate_1, query)
        self.assertIn(candidate_2, query)

    def test_election_1(self):
        """ Test election model basics"""
        print('Running Election Model Test')
        election_1 = self.election_1
        database.session.add(election_1)
        database.session.commit()
        query = Election.query.first()
        print(query)
        self.assertEqual(query.name, election_1.name)
        self.assertEqual(query, election_1)

    def test_election_2(self):
        """
        Test if multiple elections can be committed to a table and queried
        :return:
        """
        election_1 = self.election_1
        election_2 = self.election_2
        database.session.add(election_1)
        database.session.add(election_2)
        database.session.commit()
        query = Election.query.all()
        print(query)
        self.assertIn(election_1, query)
        self.assertIn(election_2, query)

    def test_election_3(self):
        """
        Test if the elections can be added and queried by one of their attribures
        :return:
        """
        election_1 = self.election_1
        election_2 = self.election_2
        election_3 = self.election_3
        election_4 = self.election_4
        database.session.add(election_1)
        database.session.add(election_2)
        database.session.add(election_3)
        database.session.add(election_4)
        database.session.commit()
        query = Election.query.filter_by(level='local').all()
        print(query)
        self.assertIn(election_2, query)
        self.assertIn(election_3, query)

    def test_party_1(self):
        """ Test state model, if something can be added in and queried """
        print('Running Election Model Test')
        party_1 = self.party_1
        database.session.add(party_1)
        database.session.commit()
        query = Party.query.first()
        print(query)
        self.assertEqual(query.name, party_1.name)
        self.assertEqual(query, party_1)

    def test_party_2(self):
        """
        Test if multiple states are committed to a database, then they are all returned on a query
        """
        party_1 = self.party_1
        party_2 = self.party_2
        database.session.add(party_1)
        database.session.add(party_2)
        database.session.commit()
        query = Party.query.all()
        print(query)
        self.assertIn(party_1, query)
        self.assertIn(party_2, query)

    def test_party_3(self):
        """
        Test if the parties can be queried by attributes
        :return:
        """
        party_1 = self.party_1
        party_2 = self.party_2
        party_3 = self.party_3
        database.session.add(party_1)
        database.session.add(party_2)
        database.session.add(party_3)
        database.session.commit()
        query = Party.query.filter_by(hq='hq_1').all()
        print(query)
        self.assertIn(party_1, query)
        self.assertIn(party_3, query)

    def test_electoral_college(self):
        """
        Test the intermediate table for states and the parties that control them,
        this also tests the results of a join are non empty
        """
        print("Running the Electoral College Test")
        party_1 = self.party_1
        party_2 = self.party_2
        party_3 = self.party_3
        relation_1 = ElectoralCollege()
        relation_2 = ElectoralCollege()
        relation_3 = ElectoralCollege()

        relation_1.party = self.party_1
        relation_1.states = self.state_1

        relation_2.party = self.party_1
        relation_2.states = self.state_2

        relation_3.party = self.party_2
        relation_3.states = self.state_3

        database.session.add(relation_1)
        database.session.add(relation_2)
        database.session.add(relation_3)
        database.session.add(party_1)
        database.session.add(party_2)
        database.session.add(party_3)
        database.session.commit()
        joined_table = ElectoralCollege.query.join(Party, State).add_columns(Party.name, State.name).all()
        print('Joined Table %r' % joined_table)
        select = ElectoralCollege.query.filter_by(party=self.party_1).all()
        print('SELECT %r' % select)
        self.assertIsNotNone(joined_table)

    def test_parties_involved(self):
        """
        Test the intermediate table for states and the parties that control them,
        this also tests the results of a join are non empty

        :return:
        """
        relation_1 = PartiesInvolved(party=self.party_1, elections=self.election_1)
        relation_2 = PartiesInvolved(party=self.party_2, elections=self.election_1)
        relation_3 = PartiesInvolved(party=self.party_1, elections=self.election_2)
        relation_4 = PartiesInvolved(party=self.party_2, elections=self.election_2)
        database.session.add(relation_1)
        database.session.add(relation_2)
        database.session.add(relation_3)
        database.session.add(relation_4)
        database.session.commit()
        joined_table = PartiesInvolved.query.join(Election, Party).add_columns(Election.name, Party.name).all()
        print("JOINED TABLE %r" % joined_table)
        self.assertIsNotNone(joined_table)

    def test_elections_to_states(self):
        """
        Test the intermediate table for elections and the states they are held in
        this also tests the results of a join are non empty
        :return:
        """
        relation_1 = ElectionsToState(elections=self.election_1, states=self.state_1)
        relation_2 = ElectionsToState(elections=self.election_2, states=self.state_2)
        relation_3 = ElectionsToState(elections=self.election_1, states=self.state_2)
        relation_4 = ElectionsToState(elections=self.election_1, states=self.state_3)
        database.session.add(relation_1)
        database.session.add(relation_2)
        database.session.add(relation_3)
        database.session.add(relation_4)
        database.session.commit()
        joined_table = ElectionsToState().query.join(Election, State).add_columns(Election.name, State.name).all()
        print("JOINED TABLE : ElectionsToStates %r" % joined_table)
        self.assertIsNotNone(joined_table)


# if __name__ == '__main__':
#     # unittest.main()
#     pass
