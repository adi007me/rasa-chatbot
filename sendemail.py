import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = '''Hello,
Here is the List of restaurants for you.

{0}

Thank You for using Foodie
'''

#The mail addresses and password
sender_address = "iamrasa.x@gmail.com"
sender_pass = 'x.asarmai!@#'

def send(receiver_address, input_restaurants, subject='Restaurant Search Bot'):
  if ((sender_address is None) or (sender_pass is None)):
    raise Exception('SENDER_ADDRESS and SENDER_PASSWORD is not configured')

  if (receiver_address is None):
    raise Exception('receiver_address is not provided')

  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = sender_address
  message['To'] = receiver_address
  message['Subject'] = subject

  restaurants = get_restaurant_list(input_restaurants)
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

def get_restaurant_list(restaurants):
  result = []
  for restaurant in restaurants:
    data = {
      "name": restaurant['restaurant']['name'],
      "address": restaurant['restaurant']['location']['address'],
      "average_budget": restaurant['restaurant']['average_cost_for_two'],
      "rating": restaurant['restaurant']['user_rating']['aggregate_rating']
    }
    result.append(data)

  result = sorted(result, key = lambda k: k['rating'], reverse=True)

  return result