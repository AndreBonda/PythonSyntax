from functools import reduce
from operator import itemgetter, mul, attrgetter

# Factorial implemented with reduce and an anonymous function
def factorial(n):
    return reduce(lambda a, b: a*b, range(1, n+1)) # under the hood it executes a factorial without recursion --> ((((1*2)*3)*4)*5)

print(factorial(5)) # 120

# The operator module provides function equivalents fro dozens of operators so you don't have to code trivial functions like multiplication
# Factorial implemented with reduce and mul
def factorial_2(n):
    return reduce(mul, range(1,n+1))

print(factorial_2(5)) # 120

# itemgetter function
metro_data = [
    ('Tokyo', 'JP', (35.43343, 139.2433253)),
    ('Rome', 'IT', (12.43343, 23.2433253)),
    ('Mexico City', 'MX', (7.65464, -67.45454)),
    ('New York', 'US', (12.43343, -1.2433253)),]

sorted_data = sorted(metro_data, key=lambda i: i[0]) # sort by first element using a lambda: [('Mexico City', 'MX', (7.65464, -67.45454)), ('New York', 'US', (12.43343, -1.2433253)), ('Rome', 'IT', (12.43343, 23.2433253)), ('Tokyo', 'JP', (35.43343, 139.2433253))]

# i can write the same function using 'itemgetter' function
sorted_data = sorted(metro_data,key=itemgetter(0)) # [('Mexico City', 'MX', (7.65464, -67.45454)), ('New York', 'US', (12.43343, -1.2433253)), ('Rome', 'IT', (12.43343, 23.2433253)), ('Tokyo', 'JP', (35.43343, 139.2433253))]
print(sorted_data)

# if you pass multplie values to itemgetter it will return a tuple with the extracted values. It is useful for sorting on multiple keys
people = [
    ("Luca", 25),
    ("Andrea", 18),
    ("Andrea", 30)
]
sorted_data = sorted(people, key=itemgetter(0,1))
print(sorted_data) # [('Andrea', 18), ('Andrea', 30), ('Luca', 25)]

# attrgetter function
from collections import namedtuple

metro_data = [
    ('Tokyo', 'JP', 36, (35.43343, 139.2433253)),
    ('Rome', 'IT', 45, (12.43343, 23.2433253)),
    ('Mexico City', 'MX', 19, (7.65464, -67.45454)),
    ('New York', 'US', 12, (12.43343, -1.2433253)),
]

LatLon = namedtuple('LatLon', 'lat lon')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')

metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon)) for name, cc, pop, (lat, lon) in metro_data]
print(metro_areas) # [Metropolis(name='Tokyo', cc='JP', pop=36, coord=LatLon(lat=35.43343, lon=139.2433253)), Metropolis(name='Rome', cc='IT', pop=45, coord=LatLon(lat=12.43343, lon=23.2433253)), Metropolis(name='Mexico City', cc='MX', pop=19, coord=LatLon(lat=7.65464, lon=-67.45454)), Metropolis(name='New York', cc='US', pop=12, coord=LatLon(lat=12.43343, lon=-1.2433253))]

# taking names and lats
name_and_lat_getter = attrgetter('name', 'coord.lat')
names_and_lats = [name_and_lat_getter(area) for area in metro_areas]
print(names_and_lats) # [('Tokyo', 35.43343), ('Rome', 12.43343), ('Mexico City', 7.65464), ('New York', 12.43343)]

