# A decorator is a function or another callable.
# A decorator may replace the decorated function with a different one.
# Decorators are executed immediately when a module is loaded.

# it hold references to functions decorated by @register
registry = []

def register(func):
    print(f'running register ({func})')
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()

# Program output

# running register (<function f1 at 0x102da1800>)
# running register (<function f2 at 0x102da18a0>)
# running main()
# registry -> [<function f1 at 0x102da1800>, <function f2 at 0x102da18a0>]
# running f1()
# running f2()
# running f3()