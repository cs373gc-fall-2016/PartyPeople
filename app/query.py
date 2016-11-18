
from app.models import Candidate, Election, Party, State, ElectoralCollege, PartiesInvolved, ElectionsToState
import json


def query_election():
    """

    :return: returns JSON of the table State
    """
    r_list = list()
    result = Election.query.all()

    candidates = dict()
    candidate_election = Candidate.query.all()
    for item in candidate_election:
        if not candidates.get(item.election_id):
            candidates[item.election_id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        candidates[item.election_id] += [temp]

    states = dict()
    state_election = ElectionsToState.query.all()
    for item in state_election:
        if not states.get(item.election_id):
            states[item.election_id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        states[item.election_id] += [temp]

    parties = dict()
    party_election = PartiesInvolved.query.all()
    for item in party_election:
        if not parties.get(item.election_id):
            parties[item.election_id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        parties[item.election_id] += [temp]

    counter = 0
    for item in result:
        counter = counter + 1
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.id))
        if not candidates.get(item.id):
            candidates[item.id] = list()
        if not states.get(item.id):
            states[item.id] = list()
        if not parties.get(item.id):
            parties[item.id] = list()
        temp["candidate_election"] = candidates.get(item.id)
        temp["election_to_state"] = states.get(item.id)
        temp["parties_involved"] = parties.get(item.id)
        r_list += [temp]

    ret = dict()
    ret["num_results"] = counter
    ret["objects"] = r_list
    ret["page"] = 1
    ret["total_pages"] = 1
    return json.dumps(ret)


def query_state():
    """

    :return: returns JSON of the table State
    """
    r_list = list()
    result = State.query.all()

    candidates = dict()
    candidate_state = Candidate.query.all()
    for item in candidate_state:
        if not candidates.get(item.state_id):
            candidates[item.state_id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        candidates[item.state_id] += [temp]

    elections = dict()
    state_election = ElectionsToState.query.all()
    for item in state_election:
        if not elections.get(item.state_id):
            elections[item.state_id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        elections[item.state_id] += [temp]

    parties = dict()
    party_state = ElectoralCollege.query.all()
    for item in party_state:
        if not parties.get(item.state_id):
            parties[item.state_id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        parties[item.state_id] += [temp]

    counter = 0
    for item in result:
        counter = counter + 1
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.id))
        if not candidates.get(item.id):
            candidates[item.id] = list()
        if not elections.get(item.id):
            elections[item.id] = list()
        if not parties.get(item.id):
            parties[item.id] = list()
        temp["candidate"] = candidates.get(item.id)
        temp["election_to_state"] = elections.get(item.id)
        temp["electoral"] = parties.get(item.id)
        r_list += [temp]

    ret = dict()
    ret["num_results"] = counter
    ret["objects"] = r_list
    ret["page"] = 1
    ret["total_pages"] = 1
    return json.dumps(ret)


def query_candidate():
    """
    :return: returns JSON of the table Candidate
    """
    r_list = list()
    result = Candidate.query.all()

    elections = dict()
    election_candidate = Election.query.all()
    for item in election_candidate:
        # if not elections.get(item.id):
        # 	elections[item.id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        elections[item.id] = temp

    parties = dict()
    party_candidate = Party.query.all()
    for item in party_candidate:
        # if not parties.get(item.id):
        # 	parties[item.id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        parties[item.id] = temp

    states = dict()
    state_candidate = State.query.all()
    for item in state_candidate:
        # if not states.get(item.id):
        # 	states[item.id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        states[item.id] = temp

    counter = 0
    for item in result:
        counter = counter + 1
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.id))
        if not elections.get(item.id):
            elections[item.id] = dict()
        if not states.get(item.id):
            states[item.id] = dict()
        if not parties.get(item.id):
            parties[item.id] = dict()
        temp["elections"] = elections.get(item.election_id)
        temp["party"] = parties.get(item.party_id)
        temp["states"] = states.get(item.state_id)
        r_list += [temp]

    ret = dict()
    ret["num_results"] = counter
    ret["objects"] = r_list
    ret["page"] = 1
    ret["total_pages"] = 1
    return json.dumps(ret)


def query_party():
    """
    :return: returns JSON of the table Party
    """
    r_list = list()
    result = Party.query.all()

    candidates = dict()
    candidate_party = Candidate.query.all()
    for item in candidate_party:
        if not candidates.get(item.party_id):
            candidates[item.party_id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        candidates[item.party_id] += [temp]

    states = dict()
    state_party = ElectoralCollege.query.all()
    for item in state_party:
        if not states.get(item.party_id):
            states[item.party_id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        states[item.party_id] += [temp]

    elections = dict()
    party_election = PartiesInvolved.query.all()
    for item in party_election:
        if not elections.get(item.party_id):
            elections[item.party_id] = list()
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.election_id))
        elections[item.party_id] += [temp]

    counter = 0
    for item in result:
        counter = counter + 1
        temp = dict()
        for key, value in item.__dict__.items():
            if not "_sa_instance_state" in key:
                temp[key] = value
        # print(str(item.id))
        if not candidates.get(item.id):
            candidates[item.id] = list()
        if not states.get(item.id):
            states[item.id] = list()
        if not elections.get(item.id):
            elections[item.id] = list()
        temp["candidate"] = candidates.get(item.id)
        temp["electoral"] = states.get(item.id)
        temp["parties_involved"] = elections.get(item.id)
        r_list += [temp]

    ret = dict()
    ret["num_results"] = counter
    ret["objects"] = r_list
    ret["page"] = 1
    ret["total_pages"] = 1
    return json.dumps(ret)
