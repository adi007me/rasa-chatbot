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
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "delhi"}
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

## lookup: location
  data/lookups/location.txt

## lookup: cuisine
  data/lookups/cuisine.txt

## synonym:chinese
- Chinese
- Chines
- chines

## synonym:mexican
- Mexicn
- Mexican
- mxican

## synonym:italian
- Italian
- Italin
- Itlian

## synonym:american
- American
- americn
- amrican

## synonym:south indian
- South Indian
- South indian
- south Indian

## synonym:north indian
- North Indian
- North indian
- north Indian

## synonym:ahmedabad
- Ahmedabad
- Ahmedbad
- Ahmeadbad

## synonym:Bengaluru
- bengaluru
- bangalore
- Bangalur
- banglore
- banglor
- Bangalore

## synonym:chennai
- chenai
- chenni
- madras

## synonym:delhi
- New Delhi
- Delli
- Dilli
- delhi
- dilli
- new delhi
- newdelhi
- NewDelhi

## synonym:hyderabad
- Hyderabad
- hyderbad
- hyderabd

## synonym:kolkata
- Kolkata
- Calcutta
- Kolkatta

## synonym:mumbai
- Mumbai
- Bombai
- Bombay

## synonym:pune
- Pne
- Puna
- puna

## synonym:agra
- Agra
- Agra
- Agra

## synonym:ajmer
- Ajmer
- ajmr
- ajmer

## synonym:aligarh
- alligarh
- Aligarh
- Aligadh

## synonym:allahabad
- Allahbad
- Alahabad
- Illahabad
- Prayagraj

## synonym:amravati
- Amrvati
- Amravatti
- Amaravati

## synonym:amritsar
- amratsar
- amaritsar
- amrtsar

## synonym:asansol
- asnsol
- asansole
- asansol

## synonym:aurangabad
- aurangabad
- arangbad
- aurangabd

## synonym:bareilly
- barelly
- barelly
- bareilly

## synonym:belgaum
- Belgam
- Belegaum
- Belegam

## synonym:bhavnagar
- bhavanagar
- Bhavnagar
- bhaavnagar

## synonym:bhiwandi
- bhiwaandi
- biwandi
- bhiwandi

## synonym:bhopal
- Bhopa
- Bhopl
- Bhopal

## synonym:bhubaneswar
- bhubaneswar
- Bhuvaneswar
- Bhubaneshwar

## synonym:bikaner
- Bikaner
- Bikanair
- Bekaner

## synonym:Bokaro Steel City
- Bokaro
- Bokaro Steel City
- Bokaro Steel city

## synonym:chandigarh
- Chandigarh
- Chandigadh
- Chandigar

## synonym:coimbatore
- Coimbatore
- cbe
- Coimbator

## synonym:Cuttack
- Cuttck
- Cuttak
- Cuttack

## synonym:dehradun
- Dehradun
- Deharadun
- Dehradun

## synonym:dhanbad
- Dhanabad
- Dhanbd
- Dhanbad

## synonym:Durg-Bhilai Nagar
- Durg Nagar
- Bhilai Nagar
- Durg-Bhilai

## synonym:durgapur
- Duragapur
- Durgapure
- Durgapur

## synonym:erode
- Erode
- Erod
- erodey

## synonym:faridabad
- Faridabd
- Fardabad
- Faridabad

## synonym:Firozabad
- Firozbad
- Firzabad
- Firozabad

## synonym:ghaziabad
- Gaziabad
- Ghazibad
- Ghaziabad

## synonym:gorakhpur
- Gorakpur
- Gorkhpur
- Gorakhpur

## synonym:gulbarga
- Gulbrga
- Gulbarg
- Gulbarga

## synonym:guntur
- Guntr
- Gantur
- Guntoor

## synonym:gurgaon
- Gurugaon
- Gurugram
- Gurgao

## synonym:guwahati
- Gowahati
- Guwahathi
- Guwahati

## synonym:gwalior
- Gwaliar
- Ghwaliar
- Gwalior

## synonym:Hubli-Dharwad
- Hubli
- Dharwad
- Hubli-Darwad

## synonym:indore
- Indor
- Indore
- Indoor

## synonym:jabalpur
- jabalpur
- Jablpur
- Jabalpur

## synonym:jaipur
- Jaipure
- Jaypur
- Jaipur

## synonym:jalandhar
- Jalandhr
- Jalanadhar
- Jalandar

## synonym:jammu
- Jammu
- Jamu

## synonym:jamnagar
- Jamanagar
- Jamnagr
- Jamnagar

## synonym:jamshedpur
- jamshedpure
- Jamshedpur
- Jamshedpur

## synonym:jhansi
- Jansi
- Jhanasi
- Jhansi

## synonym:jodhpur
- Jodpur
- Jodhpure
- Jodhpur

## synonym:Kannur
- Kanur
- Kannur
- Kannur

## synonym:kanpur
- cawnpur
- Kaanpur
- Kanpur

## synonym:kakinada
- Kakinda
- Kakinad
- Kakinada

## synonym:Kochi
- Cochi
- cochin
- kochi

## synonym:Kottayam
- Kotayam
- Kottyam
- kottayam
- kotayam

## synonym:kolhapur
- Kolapur
- Kohlapur
- Kolhapur

## synonym:kollam
- Kolam
- Kollam
- Kollam

## synonym:kota
- Kota

## synonym:kozhikode
- Kozhikod
- Kozhikode
- kozhikod
- calicut
- Calicut

## synonym:kurnool
- Kurnol
- Koornool
- Kurnool

## synonym:lucknow
- Lucknow
- Lko
- Luknow

## synonym:ludhiana
- Ludiana
- Ludhiana
- Ludhiana

## synonym:madurai
- Madurai

## synonym:malappuram
- Malapuram
- Mallappuram
- Malappuram

## synonym:mathura
- Matura
- Mathura
- Mathura

## synonym:mangalore
- Mangalor
- Manglore
- Mangalore
- mangaluru
- Mangaluru

## synonym:meerut
- Merut
- Meerut
- Meerut

## synonym:moradabad
- Muradabad
- Moradbad
- Moradabad

## synonym:mysore
- mysore
- Mysor
- Mysure
- mysuru
- Mysuru

## synonym:nagpur
- Nagpure
- Nagpor
- Nagpur

## synonym:nanded
- Nanded

## synonym:nashik
- Nasik
- Nashik
- Naseek

## synonym:nellore
- Nellor
- Nelore
- Nellore

## synonym:noida
- greater Noida
- G. Noida
- Noida

## synonym:palakkad
- Palakad
- Pallakkad
- Pallakad

## synonym:patna
- Patna

## synonym:pondicherry
- Puducherry
- Puducherri
- Pondi

## synonym:raipur
- Raipur
- Raipoor

## synonym:rajkot
- Rjakot
- Raajkot
- Rajkot

## synonym:rajahmundry
- Rajamundry
- Rajhmundry
- Rajmundry

## synonym:ranchi
- Rancih
- Ranchi

## synonym:rourkela
- Rourkel
- Rorkela
- Rourekla

## synonym:salem
- Selam
- Salem

## synonym:sangli
- sangli
- Sangil
- Sangli

## synonym:siliguri
- Siligur
- Siligudi
- Silguri

## synonym:solapur
- Sholapur
- Solpur
- Solapur

## synonym:srinagar
- Srinagr
- Sirinagar
- Sirnagar

## synonym:sultanpur
- Sultanapur
- Sulatanpur
- Sultanpur

## synonym:surat
- Surat
- Soorat

## synonym:thiruvananthapuram
- Trivandram
- Thiruvanantapuram
- Thiruvanthapuram
- trivandram

## synonym:thrissur
- Thirissur
- Thrisur
- Thirisur
- thrichur
- Thrichur

## synonym:Tiruchirappalli
- Tiruchirapalli
- Tiruchirappali
- Tiruchirapali

## synonym:tirunelveli
- Trunelveli
- Thirunelveli
- Tirnelveli

## synonym:tiruppur
- Tirupur
- Tiruppor
- Tiruppur

## synonym:ujjain
- Ujain
- Ujjan
- Ujjain

## synonym:bijapur
- Bijpur
- Bijapur
- Bijapur

## synonym:vadodara
- Baroda
- Vadodra
- Vadodara

## synonym:varanasi
- Varansi
- Banaras
- Varanasi

## synonym:Vasai-Virar City
- Vasai City
- Virar City
- Vasai-Virar City

## synonym:vijayawada
- Vijaywada
- Vijayawada
- Vijaiawada

## synonym:Visakhapatnam
- Visakapatnam
- Vishakhapatnam
- Vishakapatnam
- vizag
- Vizag

## synonym:warangal
- Warangal

## synonym:mid
- moderate

## regex:email
- [A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Za-z]{2,}

## regex:location
- (.+pur)|(.+pradesh)|(.+nagar)$

## regex:greet
- hey[.]*
