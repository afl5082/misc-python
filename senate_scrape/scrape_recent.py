from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest
from datetime import datetime 
import requests
import re

def last_vote ():
	poll_page = 'https://www.senate.gov/legislative/votes_new.htm'
	page1 =requests.get(poll_page)
	page = page1.text 

	soup = BeautifulSoup(page, 'html.parser')

	last_vote = soup.find(href=re.compile("vote=")).text
	regex = re.compile("(.*?)\s*\(")
	last_vote_out = regex.match(last_vote)
	return(int(last_vote_out.group(1)))
