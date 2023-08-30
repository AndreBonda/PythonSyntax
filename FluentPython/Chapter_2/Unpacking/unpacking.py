# Unpacking from list
a, b, c = [1, 2, 3]
print(a, b, c)

# tuple unpacking
t = 1995, "Andrea", "Bondanini"
year, firstname, surname = t
print(year)
print(firstname)
print(surname)

# Unpacking for swapping without using temporary variables
a = 1
b = 2

a, b = b, a

print(a) # 2
print(b) # 1

# Unpacking to get the last part of a string
import os

path = "/Users/jhon/study/file.txt"
*_, folder, filename = path.split("/")
print(folder) # folder
print(filename) # filename
print(_) # ['', 'Users', 'jhon']