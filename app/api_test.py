# # Start manually:
# # pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/sercer.log start
# # Stop manually:
# # pg_ctl -D /usr/local/var/postgres stop -s -m fast
import os
import unittest
import json

from flask import Flask
from app.models import database, State, Party, Candidate, Election, ElectoralCollege, PartiesInvolved

class APITest(unittest.TestCase):
    """ Tests API interface """
    # candidate1 = Candidate.query.first()
    # state1 = State.query.first()
    # party1 = Party.query.first()
    # election1 = Election.query.first()
    # elec_col1 = ElectoralCollege.query.first()
    # parties_inv = PartiesInvolved.query.first()

    def setUp(self):
        # self.app = 
        self.app = Flask(__name__).test_client()
        pass

    def tearDown(self):
        # database.session.close()
        # database.reflect()
        # database.drop_all()
        pass

    # def test_state_all(self):
    #     rc = self.app.get('/api/state')
    #     # self.assertEqual(rc.mimetype, 'application/json')
    #     # print (rc.data.decode('utf-8'));
    #     data = json.loads(rc.data.decode('utf-8'))
    #     self.assertEqual(data['num_results'], 3)
    #     state_1 = data['objects'][0]
    #     state_2 = data['objects'][1]
    #     # test data

    def test_state_single(self):
        rc = self.app.get('/api/state/1')
        # self.assertEqual(rc.mimetype, 'application/json')
        print(rc.data.decode('utf-8'))
        # data = json.loads(rc.data.decode('utf-8'))
        # state = data['objects'][0]
        # print(state['id'])
        # self.assertEqual(data['id'], 1)
        pass


    # def test_state_relationship(self):
    #     rc = self.app.get('/api/state/2')
    #     self.assertEqual(rc.mimetype, 'application/json')
    #     # print (rc.data.decode('utf-8'));
    #     data = json.loads(rc.data.decode('utf-8'))


    # def test_party_all(self):
    #     rc = self.app.get('/api/party')
    #     self.assertEqual(rc.mimetype, 'application/json')
    #     # print (rc.data.decode('utf-8'));
    #     data = json.loads(rc.data.decode('utf-8'))
    #     self.assertEqual(data['num_results'], 3)
    #     party_1 = data['objects'][0]
    #     party_2 = data['objects'][1]
    #     party_3 = data['objects'][2]


    # def test_party_single(self):
    #     rc = self.app.get('/api/party/2')
    #     self.assertEqual(rc.mimetype, 'application/json')
    #     # print (rc.data.decode('utf-8'));
    #     data = json.loads(rc.data.decode('utf-8'))


    # def test_party_relationship(self):
    #     rc = self.app.get('/api/party/3')
    #     self.assertEqual(rc.mimetype, 'application/json')
    #     # print (rc.data.decode('utf-8'));
    #     data = json.loads(rc.data.decode('utf-8'))


    # def test_candidate_all(self):
    #     rc = self.app.get('/api/candidate')
    #     self.assertEqual(rc.mimetype, 'application/json')
    #     # print (rc.data.decode('utf-8'));
    #     data = json.loads(rc.data.decode('utf-8'))
    #     self.assertEqual(data['num_results'], 3)
    #     candidate_1 = data['objects'][0]
    #     candidate_2 = data['objects'][1]


    # def test_candidate_single(self):
    #     rc = self.app.get('/api/candidate/1')
    #     self.assertEqual(rc.mimetype, 'application/json')
    #     # print (rc.data.decode('utf-8'));
    #     data = json.loads(rc.data.decode('utf-8'))


    # def test_candidate_relationship(self):
    #     rc = self.app.get('/api/candidate/1')
    #     self.assertEqual(rc.mimetype, 'application/json')
    #     # print (rc.data.decode('utf-8'));
    #     data = json.loads(rc.data.decode('utf-8'))


    # def test_election_single(self):
    #     rc = self.app.get('/api/election/1')
    #     self.assertEqual(rc.mimetype, 'application/json')
    #     # print (rc.data.decode('utf-8'));
    #     data = json.loads(rc.data.decode('utf-8'))


    # def test_election_relationship(self):
    #     rc = self.app.get('/api/election/1')
    #     self.assertEqual(rc.mimetype, 'application/json')
    #     # print (rc.data.decode('utf-8'));
    #     data = json.loads(rc.data.decode('utf-8'))

    def test_s_and_single_1(self):
    	pass

    def test_s_and_single_2(self):
    	pass

    def test_s_and_single_3(self):
    	pass

    def test_s_and_single_4(self):
    	pass

    def test_s_and_single_5(self):
    	pass

    def test_s_and_single_6(self):
    	pass

    def test_s_and_multi_1(self):
    	pass

    def test_s_and_multi_2(self):
    	pass

    def test_s_and_multi_3(self):
    	pass

    def test_s_and_multi_4(self):
    	pass

    def test_s_and_multi_5(self):
    	pass

    def test_s_or_single_1(self):
    	pass

    def test_s_or_single_2(self):
    	pass

    def test_s_or_single_3(self):
    	pass

    def test_s_or_single_4(self):
    	pass

    def test_s_or_single_5(self):
    	pass

    def test_s_or_multi_1(self):
    	pass

    def test_s_or_multi_2(self):
    	pass

    def test_s_or_multi_3(self):
    	pass

    def test_s_or_multi_4(self):
    	pass

    def test_s_or_multi_5(self):
    	pass

    def test_s_or_multi_6(self):
    	pass

    def test_states(self):
    	pass

    def test_elections(self):
    	pass

    def test_candidates(self):
    	pass

    def test_parties(self):
    	pass

    def test_query_states(self):
    	pass

    def test_query_elections(self):
    	pass

    def test_query_candidates(self):
    	pass

    def test_query_parties(self):
    	pass

if __name__ == '__main__':
    unittest.main()