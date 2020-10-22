from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

from concurrent.futures import ThreadPoolExecutor

import sendemail

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
        
    def run(self, dispatcher, tracker, domain):
        try:            
            loc = tracker.get_slot('location')
            cuisine = tracker.get_slot('cuisine')    
            budget = tracker.get_slot('budget')

            cost_start, cost_end = getCosts(budget)

            results = get_all_restaurants(loc, cuisine, cost_start, cost_end)

            results = [r for r in results if r['restaurant']['average_cost_for_two'] > 0]

            results = sorted(results, key = lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)

            results = results[:5]

            response="Showing you top rated restaurants..\n"
            if len(results) == 0:
                response= "Sorry! No restaurants found"
                dispatcher.utter_message(response)
                return [SlotSet('location',loc), SlotSet('no_results', True)]
            else:
                for i, restaurant in enumerate(results):
                    response=response + str(i + 1) + ". " + restaurant['restaurant']['name'] + \
                        " in " + restaurant['restaurant']['location']['address'] + \
                        " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"

            response = response + "\n\n"

            dispatcher.utter_message(response)

            return [SlotSet('location',loc), SlotSet('error', False), SlotSet('no_results', False), SlotSet('budget', budget)]
        except Exception as ex:
            print(str(ex))
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
            budget = tracker.get_slot('budget')

            cost_start, cost_end = getCosts(budget)

            print('sending email')
            results = get_all_restaurants(loc, cuisine, cost_start, cost_end)

            results = sorted(results, key = lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)

            restaurants = results[:10]

            sendemail.send(receiver_address, restaurants, subject='Restaurant Search Bot')

            return [SlotSet('email', receiver_address)]
        except Exception as ex:
            print("Exception: ", str(ex))
            return [SlotSet('error', True)]


class ActionCheckCitySupport(Action):
    def name(self):
        return "action_check_city_support"
    
    def run(self, dispatcher, tracker, domain):
        try:
            loc = tracker.get_slot('location')

            config={ "user_key":"7a65e3c0d290c885f1754d52235da690"}
            zomato = zomatopy.initialize_app(config)

            # print("###", loc)
            isValid = zomato.is_city_valid(loc)
            if isValid:
                supported_cities = [line.rstrip().lower() for line in open(r'data\lookups\location.txt')]

                supported = loc.lower() in supported_cities

                return [SlotSet('city_support', supported), SlotSet('error', False)]
            else:
                return [SlotSet('city_support', False), SlotSet('error', False)]

        except Exception as ex:
            err = str(ex)

            if err == "InvalidCityName":
                return [SlotSet('city_support', False), SlotSet('error', False)]
            else:
                print("Exception: ", err)
                return [SlotSet('error', True)]

def get_all_restaurants(loc, cuisine, cost_start, cost_end):
    config={ "user_key":"7a65e3c0d290c885f1754d52235da690"}
    zomato = zomatopy.initialize_app(config)

    location_detail=zomato.get_location(loc, 1)

    d1 = json.loads(location_detail)
    lat=d1["location_suggestions"][0]["latitude"]
    lon=d1["location_suggestions"][0]["longitude"]
    
    restaurants = []
    executor = ThreadPoolExecutor(max_workers=5)
    for start in range(0, 99, 20):
        executor.submit(get_restaurants(lat, lon, cuisine, start, restaurants))
    executor.shutdown()

    restaurants = [r for r in restaurants if r['restaurant']['average_cost_for_two'] > cost_start and r['restaurant']['average_cost_for_two'] < cost_end]

    return restaurants

def get_restaurants(lat, lon, cuisine, start, restaurants):
    config={ "user_key":"7a65e3c0d290c885f1754d52235da690" }
    zomato = zomatopy.initialize_app(config)

    cuisines_dict={ 'chinese': 25,
                    'mexican' : 73,
                    'italian': 55,
                    'american': 1,
                    'north indian':50,
                    'south indian':85 }

    result = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine.lower())), start, limit = 20)

    restaurants.extend(json.loads(result)["restaurants"])

def getCosts(budget):
    cost_start = 0
    cost_end = 100000

    budget = budget.strip()

    if budget == "Lesser than Rs. 300":
        cost_start = 0
        cost_end = 299
    elif budget == "Rs. 300 to 700":
        cost_start = 300
        cost_end = 700
    elif budget == "More than 700":
        cost_start = 701
        cost_end = 100000

    return cost_start, cost_end
