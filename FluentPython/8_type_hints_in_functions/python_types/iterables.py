# You should accepts Sequence and Iterable as parameters

from typing import Iterable

def elements_to_int(elements: Iterable[str]) -> list[int]:
    result = []

    for e in elements:
        result.append(int(e))
    
    return result

print(elements_to_int(['1', '2'])) # [1, 2]