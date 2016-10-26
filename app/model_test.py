"""
Module for testing models
"""
# pylint: disable=invalid-name,line-too-long,no-member,locally-disabled
# todo : test multi relationships [State(Many), Party(One)], [State(One), Politician(Many)]
# todo : [Election(One), Party(Many)], [Election(One), Politician(Many)]
# todo : [Politician(Many), Party(One)]
import unittest
from models import State, Party, Candidate, database, Election, ElectoralCollege, PartiesInvolved
from datetime import datetime


class ModelTest(unittest.TestCase):
    """ Class for testing models """

    def setUp(self):
        """Set up the database and the Models for testing
        Will have multiple of each type of model to be placed in the tables, to test different types of relationships
        """
        database.create_all()
        self.candidate_1 = Candidate(name="Candidate_1", dob=None, job='politician', contact='candidate1@us.gov', poll=50.0)
        self.candidate_2 = Candidate(name="Candidate_2", dob=None, job='politician', contact='candidate2@us.gov', poll=75.0)
        self.candidate_3 = Candidate(name="Candidate_3", dob=None, job='governor', contact='candidate3@us.gov', poll=50.0)
        self.election_1 = Election(name="general", date=None, level='federal')
        self.election_2 = Election(name="local_1", date=None, level='local_1')
        self.election_3 = Election(name="local_2", date=None, level='local_2')
        self.election_3 = Election(name="state", date=None, level='state')

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
        """ Test state model """
        print('Running State Model Test')
        state = self.state_1
        # state.party_affiliation = self.party
        database.session.add(state)
        database.session.commit()
        query = State.query.all()
        print(query)
        self.assertEqual(query[0].name, state.name)

    def test_candidate(self):
        """Test the Candidate model"""
        print('Running Candidate Model Test')
        candidate = self.candidate_1
        database.session.add(candidate)
        database.session.commit()
        query = Candidate.query.all()
        print(query)
        self.assertEqual(query[0].name, candidate.name)

    def test_election(self):
        """Test the Election Model"""
        print('Running the Election Model Test')
        election = self.election_1
        database.session.add(election)
        database.session.commit()
        query = Election.query.all()
        self.assertEqual(query[0], election)

    def test_party(self):
        """Test the party Model"""
        print('Running the Party Model Test')
        party = self.party_1
        database.session.add(party)
        database.session.commit()
        query = Party.query.all()
        self.assertEqual(query[0], party)

    def test_electoral_college(self):
        """
        :return:
        """
        print("Running the Electoral College Test")
        relation = ElectoralCollege()
        relation.party = self.party_1
        relation.states = self.state_1
        database.session.add(relation)
        database.session.commit()
        query = ElectoralCollege.query.all()
        print(query)

    def test_parties_involved(self):
        pass

# if __name__ == '__main__':
#     # unittest.main()
#     pass
