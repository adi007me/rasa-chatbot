## Happy path 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_city_support
    - slot{"city_support": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"no_results": false}
    - slot{"error": false}
    - slot{"budget": "Lesser than Rs. 300"}
    - utter_ask_email
* restaurant_search{"email": "abc@xyz.com"}
    - slot{"email": "abc@xyz.com"}
    - action_send_email
    - slot{"email": "abc@xyz.com"}
    - slot{"error": false}
    - utter_inform_email_sent

## All entities specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "mumbai", "budget": " More than 700"}
    - slot{"budget": " More than 700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "mumbai"}
    - action_check_city_support
    - slot{"city_support": true}
    - slot{"error": false}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"error": false}
    - slot{"no_results": false}
    - slot{"budget": " More than 700"}
    - utter_ask_email
* restaurant_search{"email": "adi007me@gmail.com"}
    - slot{"email": "adi007me@gmail.com"}
    - action_send_email
    - slot{"email": "adi007me@gmail.com"}
    - utter_inform_email_sent

## Happy path 2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_city_support
    - slot{"city_support": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"no_results": false}
    - slot{"error": false}
    - slot{"budget": "Lesser than Rs. 300"}
    - utter_ask_email
* restaurant_search{"email": "abc@xyz.com"}
    - slot{"email": "abc@xyz.com"}
    - action_send_email
    - slot{"email": "abc@xyz.com"}
    - slot{"error": false}
    - utter_inform_email_sent

## Happy path 3
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_city_support
    - slot{"city_support": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"no_results": false}
    - slot{"error": false}
    - slot{"budget": "Lesser than Rs. 300"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "abc@xyz.com"}
    - slot{"email": "abc@xyz.com"}
    - action_send_email
    - slot{"email": "abc@xyz.com"}
    - slot{"error": false}
    - utter_inform_email_sent
* affirm
    - utter_goodbye

## Happy path - email denied
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_city_support
    - slot{"city_support": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"no_results": false}
    - slot{"error": false}
    - slot{"budget": "Rs. 300 to 700"}
    - utter_ask_email
* deny
    - utter_goodbye

## Action error
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_city_support
    - slot{"city_support": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"no_results": false}
    - slot{"budget": "Lesser than Rs. 300"}
    - slot{"error": true}


## Happy path 4
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_city_support
    - slot{"city_support": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"no_results": false}
    - slot{"budget": "More than 700"}
    - slot{"error": false}
    - utter_ask_email
* restaurant_search{"email": "siva.cem@gmail.com"}
    - slot{"email": "siva.cem@gmail.com"}
    - action_send_email
    - slot{"email": "siva.cem@gmail.com"}
    - slot{"error": false}
    - utter_inform_email_sent

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "delhi"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "delhi"}
    - action_check_city_support
    - slot{"city_support": true}
    - slot{"error": false}
    - utter_ask_budget
* restaurant_search{"budget": " More than 700"}
    - slot{"budget": " More than 700"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"error": false}
    - slot{"no_results": false}
    - slot{"budget": " More than 700"}
    - utter_ask_email
* deny
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Chennai", "budget": " Lesser than Rs. 300"}
    - slot{"budget": " Lesser than Rs. 300"}
    - slot{"location": "Chennai"}
    - action_check_city_support
    - slot{"city_support": true}
    - slot{"error": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"error": false}
    - slot{"no_results": false}
    - slot{"budget": " Lesser than Rs. 300"}
    - utter_ask_email
* deny
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"budget": " Lesser than Rs. 300"}
    - slot{"budget": " Lesser than Rs. 300"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_city_support
    - slot{"city_support": true}
    - slot{"error": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"error": false}
    - slot{"no_results": false}
    - slot{"budget": " Lesser than Rs. 300"}
    - utter_ask_email
* restaurant_search{"email": "adi007me@gmail.com"}
    - slot{"email": "adi007me@gmail.com"}
    - action_send_email
    - slot{"email": "adi007me@gmail.com"}
    - utter_inform_email_sent
* goodbye
    - utter_goodbye

## interactive_story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_city_support
    - slot{"city_support": true}
    - slot{"error": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": " More than 700"}
    - slot{"budget": " More than 700"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "Bengaluru"}
    - slot{"error": false}
    - slot{"no_results": false}
    - slot{"budget": " More than 700"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* restaurant_search
    - utter_ask_email_id
* restaurant_search{"email": "adi007me@gmail.com"}
    - slot{"email": "adi007me@gmail.com"}
    - action_send_email
    - slot{"email": "adi007me@gmail.com"}
    - utter_inform_email_sent

## Story for out of service city 1
* greet
    - utter_greet
* restaurant_search{"location": "thodupuzha"}
    - slot{"location": "thodupuzha"}
    - action_check_city_support
    - slot{"city_support": false}
    - slot{"error": false}
    - utter_city_out_of_service

## Story for out of service city 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Thodupuzha"}
    - slot{"location": "Thodupuzha"}
    - action_check_city_support
    - slot{"city_support": false}
    - utter_city_out_of_service

## Story for out of service city error
* greet
    - utter_greet
* restaurant_search{"location": "thodupuzha"}
    - slot{"location": "thodupuzha"}
    - action_check_city_support
    - slot{"error": true}
    - utter_something_wrong

## Story - Email error
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_city_support
    - slot{"city_support": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"no_results": false}
    - slot{"budget": "More than 700"}
    - slot{"error": false}
    - utter_ask_email
* restaurant_search{"email": "siva.cem@gmail.com"}
    - slot{"email": "siva.cem@gmail.com"}
    - action_send_email
    - slot{"error": true}
    - utter_something_wrong

## Story: No results found
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_city_support
    - slot{"city_support": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"no_results": true}
    - slot{"location": "mumbai"}
    - slot{"budget": "Lesser than Rs. 300"}
    - slot{"error": false}

## Story - Example 5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_city_support
    - slot{"city_support": true}
    - slot{"error": false}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - utter_search_in_progress
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"error": false}
    - slot{"no_results": false}
    - slot{"budget": "Rs. 300 to 700"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "iamshiv.tr@gmail.com"}
    - slot{"email": "iamshiv.tr@gmail.com"}
    - action_send_email
    - slot{"email": "iamshiv.tr@gmail.com"}
    - utter_inform_email_sent
