## story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* restaurant_search{"email": "abc@xyz.com"}
    - slot{"email": "abc@xyz.com"}
    - action_send_email
    - slot{"email": "abc@xyz.com"}
* affirm
    - utter_goodbye

