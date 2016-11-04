# Start manually:
# pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/sercer.log start
# Stop manually:
# pg_ctl -D /usr/local/var/postgres stop -s -m fast
import os
import unittest
import json

from flask import Flask
from models import application, database, State, Party, Candidate, Election, ElectoralCollege, PartiesInvolved

class APITest(unittest.TestCase):
    """ Tests API interface """
    def setUp(self):
        # application = Flask(__name__)
        self.app = application.test_client()
        self.create_local_db()

    def tearDown(self):
        pass
        # database.session.close()
        # database.reflect()
        # database.drop_all()

    def create_local_db(self):
        candidate_1 = Candidate(name="Candidate_1", dob=None, job='politician', contact='candidate1@us.gov', poll=50.0)
        candidate_2 = Candidate(name="Candidate_2", dob=None, job='politician', contact='candidate2@us.gov', poll=75.0)
        candidate_3 = Candidate(name="Candidate_3", dob=None, job='governor', contact='candidate3@us.gov', poll=50.0)

        election_1 = Election(name="general", date=None, level='federal')
        election_2 = Election(name="local_1", date=None, level='local')
        election_3 = Election(name="local_2", date=None, level='local')
        election_4 = Election(name="state", date=None, level='state')

        state_1 = State(name='State_1', capital='Capital_1', population=1000)
        state_2 = State(name='State_2', capital='Capital_2', population=2000)
        state_3 = State(name='State_3', capital='Capital_3', population=1000)

        party_1 = Party(name="Party_1", description='party people', hq='hq_1', leader='leader_1')
        party_2 = Party(name="Party_2", description='people party', hq='hq_2', leader='leader_2')
        party_3 = Party(name="Party_3", description='people people', hq='hq_1', leader='leader_3')

        # database.create_all()
        # database.session.add(candidate_1)
        # database.session.add(candidate_2)
        # database.session.add(candidate_3)
        # database.session.add(election_1)
        # database.session.add(election_2)
        # database.session.add(election_3)
        # database.session.add(election_4)
        # database.session.add(state_1)
        # database.session.add(state_2)
        # database.session.add(state_3)
        # database.session.add(party_1)
        # database.session.add(party_2)
        # database.session.add(party_3)
        # database.session.commit()

    def test_state_all(self):
        rc = self.app.get('/api/state')
        # self.assertEqual(rc.mimetype, 'application/json')
        # print (rc.data.decode('utf-8'));
        data = json.loads(rc.data.decode('utf-8'))
        # print(data)
        # print("\n\n")
        self.assertEqual(data['num_results'], 3)
        state_1 = data['objects'][0]
        state_2 = data['objects'][1]
        # test data

    def test_state_single(self):
        rc = self.app.get('/api/state/1')
        self.assertEqual(rc.mimetype, 'application/json')
        # print (rc.data.decode('utf-8'));
        data = json.loads(rc.data.decode('utf-8'))
        # print(data)
        # print("\n\n")
        self.assertEqual(data['id'], 1)


    def test_state_relationship(self):
        rc = self.app.get('/api/state/2')
        self.assertEqual(rc.mimetype, 'application/json')
        # print (rc.data.decode('utf-8'));
        data = json.loads(rc.data.decode('utf-8'))
        # print(data)
        # print("\n\n")


    def test_party_all(self):
        rc = self.app.get('/api/party')
        self.assertEqual(rc.mimetype, 'application/json')
        # print (rc.data.decode('utf-8'));
        data = json.loads(rc.data.decode('utf-8'))
        # print(data)
        # print("\n\n")
        self.assertEqual(data['num_results'], 3)
        party_1 = data['objects'][0]
        party_2 = data['objects'][1]
        party_3 = data['objects'][2]


    def test_party_single(self):
        rc = self.app.get('/api/party/2')
        self.assertEqual(rc.mimetype, 'application/json')
        # print (rc.data.decode('utf-8'));
        data = json.loads(rc.data.decode('utf-8'))
        # print(data)
        # print("\n\n")


    def test_party_relationship(self):
        rc = self.app.get('/api/party/3')
        self.assertEqual(rc.mimetype, 'application/json')
        # print (rc.data.decode('utf-8'));
        data = json.loads(rc.data.decode('utf-8'))
        # print(data)
        # print("\n\n")


    def test_candidate_all(self):
        rc = self.app.get('/api/candidate')
        self.assertEqual(rc.mimetype, 'application/json')
        # print (rc.data.decode('utf-8'));
        data = json.loads(rc.data.decode('utf-8'))
        # print(data)
        # print("\n\n")
        self.assertEqual(data['num_results'], 3)
        candidate_1 = data['objects'][0]
        candidate_2 = data['objects'][1]


    def test_candidate_single(self):
        rc = self.app.get('/api/candidate/1')
        self.assertEqual(rc.mimetype, 'application/json')
        # print (rc.data.decode('utf-8'));
        data = json.loads(rc.data.decode('utf-8'))
        # print(data)
        # print("\n\n")


    def test_candidate_relationship(self):
        rc = self.app.get('/api/candidate/1')
        self.assertEqual(rc.mimetype, 'application/json')
        # print (rc.data.decode('utf-8'));
        data = json.loads(rc.data.decode('utf-8'))
        # print(data)
        # print("\n\n")


    def test_election_single(self):
        rc = self.app.get('/api/election/1')
        self.assertEqual(rc.mimetype, 'application/json')
        # print (rc.data.decode('utf-8'));
        data = json.loads(rc.data.decode('utf-8'))
        # print(data)
        # print("\n\n")


    def test_election_relationship(self):
        rc = self.app.get('/api/election/1')
        self.assertEqual(rc.mimetype, 'application/json')
        # print (rc.data.decode('utf-8'));
        data = json.loads(rc.data.decode('utf-8'))
        # print(data)
        # print("\n\n")

if __name__ == '__main__':
    unittest.main()
