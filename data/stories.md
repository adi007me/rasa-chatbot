## Story: Example 1
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

## story_3
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

## story_3.1
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

## story_email_denied
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

## story_action_error
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


## Story - Example 2
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
