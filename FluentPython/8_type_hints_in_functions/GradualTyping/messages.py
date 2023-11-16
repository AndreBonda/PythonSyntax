from typing import Optional


def show_count(count: int, word: str, plural: Optional[str] = None) -> str:
    if count == 1:
        return f'1 {word}'
    
    count_str = str(count) if count else 'no'
    plural_word = plural if plural else f'{word}s'
    return f'{count_str} {plural_word}'

output = show_count(1, 'bird')
print(output) # 1 bird

output = show_count(2, 'bird')
print(output) # 2 birds

output = show_count(0, 'bird')
print(output) # no birds