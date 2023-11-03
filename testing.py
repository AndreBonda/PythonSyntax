class Foo:
    def __init__(self, val) -> None:
        self.val = val

def increase(val):
    print(id(val))

def change(foo):
    foo.val = 10

foo = 1
print(id(foo))

increase(foo)
