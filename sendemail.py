import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import zomatopy
import json

mail_content = '''Hello,
Here is the List of restaurants for you.

{0}

Thank You for using Foodie
'''

#The mail addresses and password
sender_address = "iamrasa.x@gmail.com"
sender_pass = 'x.asarmai!@#'

def send(receiver_address, loc, cuisine, subject='Restaurant Search Bot'):
  if ((sender_address is None) or (sender_pass is None)):
    raise Exception('SENDER_ADDRESS and SENDER_PASSWORD is not configured')

  if (receiver_address is None):
    raise Exception('receiver_address is not provided')

  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = sender_address
  message['To'] = receiver_address
  message['Subject'] = subject

  restaurants = get_restaurant_list(loc, cuisine)
  formatted = []

  for _, r in enumerate(restaurants):
    restaurant = r["name"] + "\r\n\t-" + r["address"] + "\r\n\t-Budget for two: " + str(r["average_budget"]) + "\r\n\t-Rating: " + str(r["rating"])

    formatted.append(restaurant)
    
  restaurant_list = '\r\n'.join(rs for rs in formatted)

  #The body and the attachments for the mail
  message.attach(MIMEText(mail_content.format(restaurant_list), 'plain'))
  
  #Create SMTP session for sending the mail
  session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
  session.starttls() #enable security
  session.login(sender_address, sender_pass) #login with mail_id and password
  text = message.as_string()
  session.sendmail(sender_address, receiver_address, text)
  session.quit()

  return

def get_restaurant_list(loc, cuisine):
  config={ "user_key":"7a65e3c0d290c885f1754d52235da690"}
  zomato = zomatopy.initialize_app(config)

  location_detail=zomato.get_location(loc, 1)

  d1 = json.loads(location_detail)
  lat=d1["location_suggestions"][0]["latitude"]
  lon=d1["location_suggestions"][0]["longitude"]
  
  cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
  
  results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 10)
  
  d = json.loads(results)
  
  result = []
  if d['results_found'] == 0:
    result = ["no results"]
  else:
    for restaurant in d['restaurants']:
      data = {
        "name": restaurant['restaurant']['name'],
        "address": restaurant['restaurant']['location']['address'],
        "average_budget": restaurant['restaurant']['average_cost_for_two'],
        "rating": restaurant['restaurant']['user_rating']['aggregate_rating']
      }
      result.append(data)

  result = sorted(result, key = lambda k: k['rating'], reverse=True)

  return result