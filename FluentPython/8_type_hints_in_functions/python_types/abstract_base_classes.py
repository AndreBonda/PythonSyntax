# Postel's law: 'Be conservative in what you send, be liberal in what you accept'

# Ideally a function should accept arguments of abstract type - this gives more flexibility to the caller - and returns a value of a concrete class.

from typing import Mapping

# in this case a user can pass as argument any type that is a subtype of Mapping
def name2hex(name: str, color_map: Mapping[str, int]) -> str:
    return '... calculate ...'

# in this case it accepts only dict - too restricive design.
def name2hex_too_restrictive(name: str, color_map: dict[str, int]) -> str:
    return '... calculate ...'

