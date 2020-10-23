import os

from smtplib import SMTP
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

async def send(receiver_address, input_restaurants, subject='Restaurant Search Bot'):
  if ((sender_address is None) or (sender_pass is None)):
    raise Exception('SENDER_ADDRESS and SENDER_PASSWORD is not configured')

  if (receiver_address is None):
    raise Exception('receiver_address is not provided')

  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = sender_address
  message['To'] = receiver_address
  message['Subject'] = subject
    
  formatted = [get_restaurant(r) for _, r in enumerate(input_restaurants)]
  
  restaurant_list = '\r\n'.join(rs for rs in formatted)

  #The body and the attachments for the mail
  message.attach(MIMEText(mail_content.format(restaurant_list), 'plain'))
  
  #Create SMTP session for sending the mail
  with SMTP('smtp.gmail.com', 587) as session: 
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)

  return

def get_restaurant(restaurant):
  r = restaurant['restaurant']
  # print(r)
  return r["name"] + "\r\n\t-" + r['location']["address"] + "\r\n\t-Budget for two: " + str(r['average_cost_for_two']) + "\r\n\t-Rating: " + str(r['user_rating']['aggregate_rating'])
