travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#TODO: Write the function that will allow new countries
#to be added to the travel_log.

def add_new_country(country,num_visits,cities):
    new_country = {}
    new_country['country'] = country
    new_country['visits'] = num_visits
    new_country['cities'] = cities
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
