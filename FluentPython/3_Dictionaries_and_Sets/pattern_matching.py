# l'esempio successivo mostra l'utilità del pattern matching nel caso in cui ricevessimo dati da JSON APIs o database con schemi semi-strutturati come MongoDB, EdgeDB o PostgreSQL.

def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book', 'pages': pages}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')
        
b1 = dict(api=1, author='Andrea', type='book')
print(get_creators(b1)) # ['Andrea']

b2 = dict(api=2, authors=['Andrea', 'Luca'], type='book')
print(get_creators(b2)) # ['Andrea', 'Luca']

b3 = dict(type='book', pages=770)
# print(get_creators(b3)) # Invalid 'book' record

b4 = dict(type='manga')
# print(get_creators(b4)) # Invalid record