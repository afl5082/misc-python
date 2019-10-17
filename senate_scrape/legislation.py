
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest
from datetime import datetime 
import requests
from roll_number_calc import *

def legislation(poll_page): 
	#poll_page = 'https://www.senate.gov/legislative/LIS/roll_call_votes/vote1161/vote_116_1_00001.xml'
	page1 =requests.get(poll_page)
	page = page1.text 

	soup = BeautifulSoup(page, 'xml')


	vote_date = soup.find('vote_date')   #parsing xml to find vote date
	vote_number = soup.find('vote_number')
	congress = soup.find('congress')
	session = soup.find('session')
	vote_result = soup.find('vote_result_text')
	document_name = soup.find('document_name')
	amend_num = soup.find('amendment_number') 

	vote_question = soup.find('vote_question_text')
	vote_document = soup.find('vote_document_text')
	vote_title = soup.find('vote_title')
	yeas = soup.find('yeas')
	nays = soup.find('nays')
	absent = soup.find('absent')
	amend_num_todoc = soup.find('amendment_to_document_number')
	tie_breaker =soup.find('by_whom')
	tie_breaker_vote =soup.find('tie_breaker_vote')
	
	tie_breaker_rf=tie_breaker.text
	tie_breaker_vote_rf = tie_breaker_vote.text

	vote_question_rf = vote_question.text
	vote_document_rf = vote_document.text
	vote_title_rf = vote_title.text
	yeas_rf = yeas.text
	nays_rf = nays.text
	absent_rf = absent.text
	amend_num_todoc_rf = amend_num_todoc.text 
	congress_rf = congress.text
	session_rf = session.text
	vote_result_rf = vote_result.text
	document_name_rf = document_name.text
	amend_num_rf = amend_num.text
	vote_number_rf = vote_number.text
	vote_date_rf = vote_date.text   #extract text only from vote_date element string  
	vote_date_rf2 = vote_date_rf.replace(',',"")
	vote_date_rf3 = datetime.strptime(vote_date_rf2,'%B %d %Y  %I:%M %p') 


	if "Rejected" in vote_result_rf:
		result = "Rejected"
	elif "Agreed" in vote_result_rf:
		result = "Agreed"
	elif "Confirmed" in vote_result_rf:
		result ="Confirmed"
	elif "Passed" in vote_result_rf:
		result = "Passed"
	elif "Failed" in vote_result_rf:
		result = "Failed" 
	else:
		result = "Null"
		

	row_list = [vote_date_rf3, vote_number_rf, vote_title_rf, congress_rf, 
	session_rf, result, vote_result_rf, document_name_rf, amend_num_rf,
	vote_question_rf, vote_document_rf, yeas_rf, nays_rf, absent_rf, amend_num_todoc_rf, tie_breaker_rf, tie_breaker_vote_rf, '116_1_2019' ]


	with open('2019_legis.csv','a', newline='') as csv_file:
		thewriter = csv.writer(csv_file, delimiter ="," , quoting=csv.QUOTE_MINIMAL)
		#thewriter.writerow(['Vote Date','Vote Number', 'Vote Title', 'Congress', 'Session', 'Result', 'Vote Result Full', 'Document Name', 'Amendment_Number',
		#'Vote Question', 'Vote Document','Yeas','Nays' ,'Absent' ,'Amendment to Document Number'])
		thewriter.writerow(row_list)  




with open('2019_legis.csv','a', newline='') as csv_file:
		thewriter = csv.writer(csv_file, delimiter ="," , quoting=csv.QUOTE_MINIMAL)
		thewriter.writerow(['Vote Date','Vote Number', 'Vote Title', 'Congress', 'Session', 'Result', 'Vote Result Full', 'Document Name', 'Amendment Number',
		'Vote Question', 'Vote Document','Yeas','Nays' ,'Absent' ,'Amendment to Document Number', 'Tie Breaker', 'Tie Breaker Vote','Congress Session Year'])


roll_number= ["%.5d" % i for i in range(firstparam(),secondparam())]
base_xml = 'https://www.senate.gov/legislative/LIS/roll_call_votes/vote1161/vote_116_1_00000.xml'
all_xmls =[]
for x in range(0,lastparam()):
	all_xmls.append(base_xml.replace('00000',roll_number[x]))

for x in all_xmls:
	legislation(x) 




