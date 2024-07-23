cities = ['lviv', 'kyiv', 'odessa']

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
print(capitalized_cities)

list_of_cities = [city.title() for city in cities]
print(list_of_cities)

lower_city = [el.lower() for el in list_of_cities]
print(lower_city)

list_of_number = [2, 4, 5, 7 ,9]
after_multi = [num*3 for num in list_of_number if num < 20]
print(after_multi)

list_range = [num*5 for num in range(10)]
print(list_range)