"""
Module for testing models
"""
import unittest
from models import State, database


class ModelTest(unittest.TestCase):
    """ Class for testing models """

    def test_state(self):
        """ Test state model """
        database.drop_all()
        database.create_all()
        state = State(state_name='alaska', capital='juneau', population=123456)
        database.session.add(state)
        database.session.commit()
        query = State.query.all()
        # Assert that the value in the database is the same as the value that
        # was just passed in
