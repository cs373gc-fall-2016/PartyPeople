from app.models import State, Candidate, Election, Party, ElectoralCollege, ElectionsToState, PartiesInvolved
import os
from application import create_app

create_app().app_context().push()
os.remove('/home/ndseeg/Documents/cs373/dbout.txt')
db_out = open('/home/ndseeg/Documents/cs373/dbout.txt', 'w')

state_query = State.query.all()
print(state_query)
db_out.write(str(state_query))
db_out.write("\n")
candidate_query = Candidate.query.all()
print(candidate_query)
db_out.write(str(candidate_query))
db_out.write("\n")
party_query = Party.query.all()
print(party_query)
db_out.write(str(party_query))
db_out.write("\n")

election_query = Election.query.all()
print(election_query)
db_out.write(str(election_query))
db_out.write("\n")

electoral_college_query = ElectoralCollege.query.all()
print(electoral_college_query)
db_out.write(str(electoral_college_query))
db_out.write("\n")

elections_to_state_query = ElectionsToState.query.all()
print(elections_to_state_query)
db_out.write(str(elections_to_state_query))
db_out.write("\n")

parties_involved_query = PartiesInvolved.query.all()
print(parties_involved_query)
db_out.write(str(parties_involved_query))
db_out.write("\n")

db_out.close()

