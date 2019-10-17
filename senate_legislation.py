import urllib.request
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest
from datetime import datetime 
import requests


def senate_scrape(poll_page): 
    #poll_page = 'https://www.senate.gov/legislative/LIS/roll_call_votes/vote1161/vote_116_1_00001.xml'
	#page = urllib.request.urlopen(poll_page)
	page1 =requests.get(poll_page)
	page = page1.text #extracting the text only from webpage (required for requests library) 

	soup = BeautifulSoup(page, 'xml') #parsing the extracted xml text page through bs4

	vote_cast = soup.find_all('vote_cast')      #parses through xml to find all vote_cast tag names. "vote_cast" can literally be found within the xml  
	member_full = soup.find_all('member_full')
	vote_date = soup.find('vote_date')   
	vote_number = soup.find('vote_number')
	
	member_full_rf = [elem.get_text() for elem in member_full]  
	vote_cast_rf = [elem.get_text() for elem in vote_cast]  #loops through vote_cast object to extract the text only and stores it as a list 
	
	vote_number_rf = vote_number.text
	
	vote_date_rf = vote_date.text #extract text only from vote_date element string  
	vote_date_rf2 = vote_date_rf.replace(',',"")
	vote_date_rf3 = datetime.strptime(vote_date_rf2,'%B %d %Y  %I:%M %p') #putting vote date into correct timestamp format 

	name_length = len(member_full_rf)    #finding length of member full list to instruct how many times to append vote date to a list 
	vote_date_list  =[] #declaring empty list for vote date
	vote_number_list =[] #declaring empty list for vote number 
	congress_session_year =[]


	#last_name_rf2 =[] 
	#first_name_rf2=[] 
	#last_name_rf2 = [x.strip(' ') for x in last_name_rf]  #strips the whitespace from the names 
	#first_name_rf2 = [x.strip(' ') for x in first_name_rf]



	for rows in range(name_length):   #looping through the length (100) of member full list 100 times to append vote date 100 times 
		vote_date_list.append(vote_date_rf3) #final list is vote_date listed 100 times in list structure 
		vote_number_list.append(vote_number_rf)
		congress_session_year.append('116_1_2019')
	
	
	d = [member_full_rf,vote_cast_rf,vote_number_list,vote_date_list,congress_session_year]
	export_data = zip_longest(*d, fillvalue = '')

	with open('2019_votes1.csv','a', newline='') as csv_file:
		thewriter = csv.writer(csv_file, delimiter ="," , quoting=csv.QUOTE_MINIMAL)
		#thewriter.writerow(['Member Full','First Name','Last Name', 'Vote','Party','State','Vote Date'])
		thewriter.writerows(export_data) 


#senate_scrape('https://www.senate.gov/legislative/LIS/roll_call_votes/vote1161/vote_116_1_00001.xml') 



	
roll_number = ["%.5d" % i for i in range(27,34)] #creating an array with roll numbers that insert into the xml below. Change range params based on last vote and last vote appended into RDS table 
#for instance, if vote 1 throgh 5 is present in RDS table already but the last senate vote was vote#10, then we should enter (6,11) as params. This would give us votes 6-10. 
base_xml = 'https://www.senate.gov/legislative/LIS/roll_call_votes/vote1161/vote_116_1_00000.xml'
all_xmls =[]

for x in range(0,7): #for loop to append the roll numbers x amount of times based on which votes we haven't plugged into RDS yet. ONLY change x (0,x) to the difference of the above params. x = 11-6
	 
	all_xmls.append(base_xml.replace('00000',roll_number[x]))

with open('2019_votes1.csv','a', newline='') as csv_file:
	thewriter = csv.writer(csv_file, delimiter ="," , quoting=csv.QUOTE_MINIMAL)
	thewriter.writerow(['Senator Name','Vote', 'Vote Number','Vote Date','Congress Session Year'])
	
for x in all_xmls:
	senate_scrape(x)


