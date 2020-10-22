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
        try:
            config={ "user_key":"7a65e3c0d290c885f1754d52235da690"}
            zomato = zomatopy.initialize_app(config)
            loc = tracker.get_slot('location')
            cuisine = tracker.get_slot('cuisine')
            location_detail=zomato.get_location(loc, 1)

            d1 = json.loads(location_detail)
            lat=d1["location_suggestions"][0]["latitude"]
            lon=d1["location_suggestions"][0]["longitude"]
            cuisines_dict={ 'chinese': 25,
                            'mexican' : 73,
                            'italian': 55,
                            'american': 1,
                            'north indian':50,
                            'south indian':85 }

            results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine.lower())), 5)
            d = json.loads(results)

            response="Showing you top rated restaurants..\n"
            if d['results_found'] == 0:
                response= "Sorry! No restaurants found"
            else:
                for i, restaurant in enumerate(d['restaurants']):
                    response=response + str(i + 1) + ". " + restaurant['restaurant']['name'] + \
                        " in " + restaurant['restaurant']['location']['address'] + \
                        " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"

            response = response + "\n\n"

            dispatcher.utter_message(response)

            return [SlotSet('location',loc), SlotSet('error', False)]
        except:
            dispatcher.utter_message("Something went wrong. Please try again later.")
            return [SlotSet('error', True)]

class ActionSendEmail(Action):
    def name(self):
        return "action_send_email"
    
    def run(self, dispatcher, tracker, domain):
        try:
            receiver_address = tracker.get_slot('email')
            loc = tracker.get_slot('location')
            cuisine = tracker.get_slot('cuisine')

            print('sending email')

            sendemail.send(receiver_address, loc, cuisine, subject='Restaurant Search Bot')

            return [SlotSet('email', receiver_address)]
        except:
            return [SlotSet('error', True)]


class ActionCheckCitySupport(Action):
    def name(self):
        return "action_check_city_support"
    
    def run(self, dispatcher, tracker, domain):
        try:
            loc = tracker.get_slot('location')

            supported_cities = [line.rstrip().lower() for line in open(r'data\lookups\location.txt')]

            supported = loc.lower() in supported_cities

            return [SlotSet('city_support', supported), SlotSet('error', False)]
        except:
            return [SlotSet('error', True)]
