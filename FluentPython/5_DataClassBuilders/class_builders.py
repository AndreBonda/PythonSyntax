class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Per le classi che sono semplicemente una collezione di dati, utilizzare le "classi standard" non è molto funzionale.
# Tanto codice boilerplate. Inoltre è molto probabile che con questo tipo di istanze vorremmo stamparle in modo leggibile e fare comparazioni.
# Quindi dovremmo eseguire l'override di __repr__ e __eq__

# Soluzione: utilizzare Class Builders. Ci sono 3 modalità per dichiarare i class builder

# 1) collections.nametuple è il modo più semplice, disponibile da Python 2.6
print("----- collections.namedtuple")
from collections import namedtuple
Coordinate = namedtuple('Coordinate', 'lat lon')
print(issubclass(Coordinate, tuple)) # True

moscow = Coordinate(lat=55.756, lon=37.617)
print(moscow) # Coordinate(lat=55.756, lon=37.617)
print(moscow == Coordinate(lat=55.756, lon=37.617)) # True

# 2) typing.NamedTuple
import typing

# Defining a NameTuple adding a type annotation to each field
Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])

# Defining a NameTuple given a keyword arguments
Coordinate = typing.NamedTuple('Coordinate', lat=float, lon=float)

print(issubclass(Coordinate, tuple)) # True
print(typing.get_type_hints(Coordinate)) # {'lat': <class 'float'>, 'lon': <class 'float'>}

# Se abbiamo necessità di eseguire l'override di una NamedTuple
class Coordinate(typing.NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

moscow = Coordinate(lat=55.756, lon=37.617)
print(moscow) # 55.8°N, 37.6°E

# 3) dataclass decorator
from dataclasses import dataclass

class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

moscow = Coordinate()
moscow.lat = 55.756
moscow.lon = 37.617
print(moscow) # 55.8°N, 37.6°E