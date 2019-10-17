
from scrape_recent import last_vote
from senate_db import max_indb

def firstparam ():
	return(max_indb() + 1)

def secondparam ():
	return(last_vote() +1)
	
def lastparam():
	return(last_vote() - max_indb())
