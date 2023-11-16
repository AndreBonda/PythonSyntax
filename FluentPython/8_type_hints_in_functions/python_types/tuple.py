# There are three ways to annotate tuple types

# 1 - Tuples as records

from typing import NamedTuple


def geo(lat_lon: tuple[float, float]) -> str:
    lat, lon = lat_lon
    return f'lat: {lat}, lon: {lon}'

print(geo((10,20)))

# 2 - Tuples as records with named fields
class Coordinate(NamedTuple):
    lat: float
    lon: float

def geo2(lat_lon: Coordinate) -> str:
    lat, lon = lat_lon
    return f'lat: {lat}, lon: {lon}'

cc = Coordinate(25, 35)
result = geo2(cc)
print(result) # lat: 25, lon: 35

# 3 - Tuples as immutable sequences

def print_all_numbers(numbers: tuple[int, ...]) -> None:
    for n in numbers:
        print(n)

print_all_numbers((1,2,3))
