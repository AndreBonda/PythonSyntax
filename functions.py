# Functions
a = 0

def myFunc(n,m):
    a = 1
    print(a) # -> 1
    return n*m

print(myFunc(3,4))
print(a) # -> 0

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

# Default agruments
def say_hello(name, age=18):
    print("Hi from ", name, "-", age)

say_hello("Andrea")
say_hello("Luca", 45)

# keyword arguments
def about_me(name, age, surname):
    print(name,surname,age)

about_me(name="Andrea", surname="Bondanini", age=18)

# *othername riceve tutti i parametri dopo quelli posizionali
def insert_names(firstname, *othernames):
    print("My first name is", firstname) # Andrea

    print("My secondary names are:")
    for name in othernames:
        print(name) # Luca, Giovanni, 1

insert_names("Andrea", "Luca", "Giovanni", 1)

# **othernames riceve un dictionary con tutti i keyword arguments eccetto quelli dichiarati esplicitamente
# nella firma della funzione ()
# othernames viene passato come dict
print("\n Keyword arguments ** -----")
def insert_names_v2(firstname, **othernames):
    print("My first name is", firstname) # Andrea

    for name_type in othernames:
        print(name_type, "-", othernames[name_type])

insert_names_v2(firstname="Andrea", second_name = "Luca", third_name = "Massimo")

# Function annotations
def func_with_annotations(firstname: str, age: int, adult: bool) -> None:
    print("Call func with annotations")

func_with_annotations("Andrea",20,True)