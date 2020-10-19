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
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
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
- [mumbai](location)
- [North Indian](cuisine)
- [pune](location)
- [Lesser than Rs. 300](budget)
- [Rs. 300 to 700](budget)
- [More than 700](budget)
-  yes. Please send it to [adi007me@gmail.com](email)
- [abcd@xyz.com](email)

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
- yes. please

## intent:deny
- no
- not needed
- no need
- that is unnecessary
- no thank you
- - not right now
- - I don't want to
- I don't want to give it to you
- I don't want to say
- I dont want to tell
- I'm not giving you my email address
- I'm not going to give it to you
- NEIN
- NO
- NO DON"T WANT THIS!
- Nah
- Neither
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
- decline
- definitely not
- deny
- i decline
- i don not like this
- i don't think so
- i don't want either of those
- i don't want to
- i don't want to give you my email
- i dont want to
- i dont want to accept :P lol
- i guess it means - no
- i'm afraid not
- i'm not sure
- it is going pretty badly
- it sucks
- it sux
- n
- na
- nah
- nah I'm good
- nah not for me
- nah, first time
- nah, i'm good
- nehi
- nein
- neither
- never
- never mind
- no
- no :(
- no I dont want
- no I haven't decided yet if I want to sign up
- no and no again
- no bots at all
- no go
- no i can't
- no i don't accept
- no i dont want to
- no i dont want to accept :P lol
- no i won't
- no ma'am
- no sir
- no sorry
- no thank s
- no thank you
- no thanks
- no way
- no you did it wrong
- no!!!!
- no, i hate it
- no, my frst time
- no, thank you
- no, thanks
- no, thankyou
- no. u r idiot
- non
- noooooooooo
- noooooooooooooooooooooooooooooooooooooooo
- nop
- nope
- nope!
- nope. i am good
- not going well at all
- not really
- not right now
- not yet
- nö
- sorry not right now
- still dont want to tell
- thanks but no thanks
- this sucks
- very bad
- I do not need help installing
- I don't wanna tell the name of my company
- no stop
- stop it, i do not care!!!
- none of them
- I don't agree

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

## synonym:chinese
- chines
- Chinese

## synonym:mid
- moderate

## regex:greet
- hey[.]*

## regex:email
- [A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Za-z]{2,}

## lookup: location
data/lookups/location.txt

## lookup: cuisine
data/lookups/cuisine.txt
