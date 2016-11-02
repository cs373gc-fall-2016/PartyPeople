
from models import Candidate, Election, Party, State, ElectoralCollege, PartiesInvolved, ElectionsToState


def query_state_by_name(state_name):
    return State.query.filter_by(State.name == state_name).all()


def query_state_by_party():
    pass


def query_candidate_by_party(candidate_party):
    return Candidate.query.filter_by(Candidate.party == candidate_party).all()


def query_candidate_by_name(candidate_name):
    return Candidate.query.filter_by(Candidate.name == candidate_name).all()


def query_election_by_name(election_name):
    return Election.query.filter_by(Election.name == election_name).all()


def query_election_by_level(level):
    return Election.query.filter_by(Election.level == level).all()