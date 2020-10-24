from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import logging

from concurrent.futures import ThreadPoolExecutor
import asyncio

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

            results = sorted(results, key = lambda k: float(k['restaurant']['user_rating']['aggregate_rating']), reverse=True)

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
        except Exception:
            logging.exception("message")
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

            results = sorted(results, key = lambda k: float(k['restaurant']['user_rating']['aggregate_rating']), reverse=True)

            restaurants = results[:10]

            asyncio.ensure_future(sendemail.send(receiver_address, restaurants, subject='Restaurant Search Bot'))

            return [SlotSet('email', receiver_address)]
        except:
            logging.exception("message")
            return [SlotSet('error', True)]


class ActionCheckCitySupport(Action):
    def name(self):
        return "action_check_city_support"
    
    def run(self, dispatcher, tracker, domain):
        try:
            loc = tracker.get_slot('location')

            config={ "user_key":"7a65e3c0d290c885f1754d52235da690"}
            zomato = zomatopy.initialize_app(config)

            isValid = zomato.is_city_valid(loc)
            if isValid:
                supported_cities = [line.rstrip().lower() for line in open(r'data\lookups\location.txt')]

                supported = loc.lower() in supported_cities

                return [SlotSet('city_support', str(supported)), SlotSet('error', False)]
            else:
                return [SlotSet('city_support', "Invalid"), SlotSet('error', False)]

        except Exception as ex:
            err = str(ex)

            if err == "InvalidCityName":
                return [SlotSet('city_support', "Invalid"), SlotSet('error', False)]
            else:
                logging.exception("message")
                return [SlotSet('error', True)]

def get_all_restaurants(loc, cuisine, cost_start, cost_end):
    config={ "user_key":"7a65e3c0d290c885f1754d52235da690"}
    zomato = zomatopy.initialize_app(config)

    location_detail=zomato.get_location(loc, 1)

    d1 = json.loads(location_detail)

    lat=d1["location_suggestions"][0]["latitude"]
    lon=d1["location_suggestions"][0]["longitude"]

    cuisines_dict={ 'chinese': 25,
                    'mexican' : 73,
                    'italian': 55,
                    'american': 1,
                    'north indian':50,
                    'south indian':85,
                    'african': 152,
                    'afghan': 1035,
                    'andhra': 2,
                    'arabian': 4,
                    'armenian': 175,
                    'asian': 3,
                    'assamese': 165,
                    'australian': 131,
                    'awadhi': 292,
                    'bbq': 193,
                    'bakery': 5,
                    'bar food': 227,
                    'belgian': 132,
                    'bengali': 10,
                    'beverages': 270,
                    'bihari': 1013,
                    'biryani': 7,
                    'bohri': 1032,
                    'brazilian': 159,
                    'british': 133,
                    'bubble tea': 247,
                    'burger': 168,
                    'burmese': 22,
                    'cafe': 30,
                    'cantonese': 121,
                    'charcoal chicken': 994,
                    'chettinad': 18,
                    'coffee': 1040,
                    'coffee and tea': 161,
                    'continental': 35,
                    'cuisine varies': 1014,
                    'desserts': 100,
                    'egyptian': 146,
                    'european': 38,
                    'fast food': 40,
                    'finger food': 271,
                    'french': 45,
                    'frozen yogurt': 501,
                    'fusion': 274,
                    'german': 134,
                    'goan': 47,
                    'greek': 156,
                    'grocery': 1059,
                    'gujarati': 48,
                    'healthy food': 143,
                    'hot dogs': 1026,
                    'hyderabadi': 49,
                    'ice cream': 233,
                    'indian': 148,
                    'indonesian': 114,
                    'iranian': 140,
                    'japanese': 60,
                    'juices': 164,
                    'kashmiri': 65,
                    'kebab': 178,
                    'kerala': 62,
                    'konkan': 63,
                    'korean': 67,
                    'lebanese': 66,
                    'lucknowi': 157,
                    'maharashtrian': 102,
                    'malaysian': 69,
                    'malwani': 71,
                    'mangalorean': 72,
                    'mediterranean': 70,
                    'middle eastern': 137,
                    'mishti': 1041,
                    'mithai': 1015,
                    'modern indian': 1018,
                    'momos': 1051,
                    'mongolian': 74,
                    'moroccan': 147,
                    'mughlai': 75,
                    'naga': 166,
                    'nepalese': 117,
                    'north eastern': 231,
                    'odia': 1057,
                    'paan': 1048,
                    'panini': 989,
                    'parsi': 290,
                    'peruvian': 162,
                    'pizza': 82,
                    'portuguese': 87,
                    'rajasthani': 88,
                    'raw meats': 27,
                    'relief fund': 1060,
                    'roast chicken': 1005,
                    'rolls': 1023,
                    'salad': 998,
                    'sandwich': 304,
                    'seafood': 83,
                    'sindhi': 993,
                    'singaporean': 119,
                    'south american': 972,
                    'spanish': 89,
                    'sri lankan': 86,
                    'steak': 141,
                    'street food': 90,
                    'sushi': 177,
                    'tamil': 1054,
                    'tea': 163,
                    'tex-mex': 150,
                    'thai': 95,
                    'tibetan': 93,
                    'turkish': 142,
                    'vietnamese': 99,
                    'wraps': 1024 }

    cuisine_code = str(cuisines_dict.get(cuisine.lower()))
    
    restaurants = []

    with ThreadPoolExecutor(max_workers=5) as e:
        for start in range(0, 99, 20):
            e.submit(get_restaurants, zomato, lat, lon, cuisine_code, start, restaurants)

    restaurants = [r for r in restaurants if r['restaurant']['average_cost_for_two'] > cost_start and r['restaurant']['average_cost_for_two'] < cost_end]
    
    return restaurants

def get_restaurants(zomato, lat, lon, cuisine_code, start, restaurants):
    result = zomato.restaurant_search("", lat, lon, cuisine_code, start, limit = 20)

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
