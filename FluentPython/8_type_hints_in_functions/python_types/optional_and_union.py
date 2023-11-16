
# 'text: str | None = None' is the new syntax since python 3.10 and we can write this over the old one 'text: Optional[str] = None'
def print_text(text: str | None = None) -> str:
    if text is None:
        return "No text passed"
    
    return f'text passed is: {text}'

print(print_text('hello'))

def parse_token(token: str) -> str | float:
    try:
        return float(token)
    except ValueError:
        return token

result = parse_token('1')
print(result) # 1.0

result = parse_token('Andrea')
print(result) # Andrea