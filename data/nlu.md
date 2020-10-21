## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hola

## intent:restaurant_search
- looking for restaurant
- i'm hungry. looking out for some good restaurants
- can you suggest some good restaurants in [Rishikesh](location)
- can you suggest some good restaurants in [Perumbavoor](location)
- can you suggest some good restaurants in [Thodupuzha](location)
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- I am looking for some restaurants in [Thodupuzha](location)
- I am looking for some restaurants in [Perumbavoor](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- I am looking for restaurant
- [pune](location)
- [Lesser than Rs. 300](budget)
- [Rs. 300 to 700](budget)
- [More than 700](budget)
- yes. Please send it to [adi007me@gmail.com](email)
- [abcd@xyz.com](email)
- [Thodupuzha](location)
- can you suggest some good restaurants in [New](location) [Delhi](location)
- I'll prefer [chines]{"entity": "cuisine", "value": "chinese"}
- [>700](budget)
- yes. please send it to [siva.cem@gmail.com](email)
- [iamrasa.x@gmail.com](email)
- [siva.cem@gmail.com](email)
- looking for a place to eat in [thodupuzha](location)
- can you find me a place to eat in [pala](location)

## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thanks

## intent:deny
- no
- not needed
- no need
- that is unnecessary
- no thank you
- not right now
- I don't want to
- I don't want to give it to you
- I don't want to say
- I dont want to tell
- I'm not giving you my email address
- I'm not going to give it to you
- Never
- Nevermind
- No
- No thank you
- No, not really.
- No, thank you
- No.
- Nopes
- Not really
- absolutely not
- n
- na
- nah
- nehi
- nein
- never
- no :(
- non
- noooooooooo
- noooooooooooooooooooooooooooooooooooooooo
- nop
- nope
- nope!

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## synonym:4
- four

## synonym:Delhi
- New Delhi
- delhi
- dilli
- Dilli
- new delhi
- newdelhi
- NewDelhi

## synonym:Bengaluru
- bangalore
- bengaluru
- banglore
- banglor

## synonym:chinese
- chines
- Chinese

## synonym:mid
- moderate

## regex:email
- [A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Za-z]{2,}

## regex:location
- (.+pur)|(.+pradesh)|(.+nagar)$

## regex:greet
- hey[.]*

## lookup: location
  data/lookups/location.txt

## lookup: cuisine
  data/lookups/cuisine.txt
