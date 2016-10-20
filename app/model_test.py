import unittest
from app.state import State, db


class ModelTest(unittest.TestCase):

    def test_state(self):
        db.drop_all()
        db.create_all()
        state = State(state_name='alaska', capital='juneau', population=123456)
        db.session.add(state)
        db.session.commit()
        query = State.query.all()
        #Assert that the value in the database is the same as the value that was just passed in
        pass
