# Functions

def myFunc(n,m):
    return n*m

print(myFunc(3,4))

# Nested functions have access to outer variables
print()
def outer(a,b):
    c = 'c'

    def inner():
        return a+b+c
    return inner()

print(outer('a', 'b'))

def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # val *= 2 --> will only modify val in the helper scope (è un value type)

        # se volessi modificare val fuori dallo scope utilizzare la keyword val
        nonlocal val
        val *= 2

    helper()

nums = [1,2]
val = 3
double(nums, val)
print()
print(nums) # [2,4]
print(val) # 6