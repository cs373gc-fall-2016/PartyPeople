"""
Module for testing models
"""
# pylint: disable=invalid-name,line-too-long,no-member,locally-disabled

import unittest
from models import State, Party, Candidate, database #, Candidate, Election, Party, database
from datetime import datetime


class ModelTest(unittest.TestCase):
    """ Class for testing models """

    def setUp(self):
        """Set up the database and the Models for testing"""
        database.create_all()
        self.candidate = Candidate(name="Bill") #, dob=datetime(1900, 2, 3, 4, 12, 30, 00), job="candidate",
                                   # party="Democratic", poll=50.0, contact="bill@bill.org")
        # self.election = Election(ename="general", date=datetime(
        #     2016, 11, 8, 12, 0, 0), level='state')
        # self.election2 = Election(name="local", date=datetime(2016, 11, 8, 12, 0, 0), level='state',
        #                           location="texas", politicians=["nobody", "anybody"])
        self.state = State(name='alaska', capital='juneau', population=123456)
        self.party = Party(name="Republican") #, description="Republican Party", politicians=["Trump", "Bush"],
        #                    state=["Texas", "Mississippi"], hq="DC", leader="Mr. President")

    def tearDown(self):
        """Drop all the tables so on subsequent tests it doesn't complain that elements already exist"""
        database.session.close()
        database.reflect()
        database.drop_all()

    def test_state(self):
        """ Test state model """
        state = self.state
        state.candidates = self.candidate
        # state.party_affiliation = self.party
        database.session.add(state)
        database.session.commit()
        query = State.query.all()
        print(query)

        self.assertEqual(query[0].name, state.name)
        print(query[0].candidates)
        print(self.candidate)
    # def test_Candidate(self):
    #     """Test the Candidate model"""
    #     candidate = self.candidate
    #     database.session.add(candidate)
    #     database.session.commit()
    #     query = Candidate.query.all()
    #     self.assertEqual(query[0], candidate)
    #     print(query[0])
    #     print(query[0].elections)
    #
    # def test_election(self):
    #     """Test the Election Model"""
    #     election = self.election
    #     database.session.add(election)
    #     database.session.commit()
    #     query = Election.query.all()
    #     self.assertEqual(query[0], election)
    #
    # def test_party(self):
    #     """Test the party Model"""
    #     party = self.party
    #     database.session.add(party)
    #     database.session.commit()
    #     query = Party.query.all()
    #     self.assertEqual(query[0], party)
    #
    # def test_relation(self):
    #     """Test the relationship between two models"""
    #     self.candidate.elections = [self.election, self.election2]


# if __name__ == '__main__':
#     # unittest.main()
#     pass
