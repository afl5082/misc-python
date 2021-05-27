
from requests import get
from bs4 import BeautifulSoup
from sms import send


url = 'https://www.contebikes.com/product-list/bikes-1000/mountain-bikes-1006/?sort=priceasc&rb_pr=500%2D749%2E99'
url1 = 'https://www.contebikes.com/product-list/bikes-1000/mountain-bikes-1006/?sort=priceasc&rb_pr=750%2D999%2E99'

def get_bike_items(url,price_range):
    response = get(url)
    #print(response.text[:500])


    html_soup = BeautifulSoup(response.text, 'html.parser')
    all_bikes = html_soup.find_all('div', class_ = 'seProductTitle')

    #print(len(all_bikes))

    #mms doesn't like colons!! - sent as blank text with a colon in a string
    bike_names ="Price Range " + price_range
    for bikes in all_bikes:
        text = bikes.a.text
        biken = text.replace("\n","")

        bike_names+= " " + biken + "||"

    

    send(bike_names)
    #send(bike_names)

def lambda_function(event,context):
    get_bike_items(url1,"$750-$999")
    get_bike_items(url,"$500-$749")



