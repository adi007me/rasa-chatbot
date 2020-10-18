from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

import sendemail

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)

		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}

		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)

		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response + restaurant['restaurant']['name'] + \
					" in " + restaurant['restaurant']['location']['address'] + \
					" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"

		response = response + "\n"

		dispatcher.utter_message(response)

		return [SlotSet('location',loc)]

class ActionSendEmail(Action):
	def name(self):
		return "action_send_email"
	
	def run(self, dispatcher, tracker, domain):
		receiver_address = tracker.get_slot('email')
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')

		print('sending email')

		sendemail.send(receiver_address, loc, cuisine, subject='Restaurant Search Bot')

		dispatcher.utter_message("Sent")

		return [SlotSet('email', receiver_address)]
