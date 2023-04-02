# Parentheses needed for multi-line conditions
n, m = 1, 2
if (n == 1 
    and m == 2):
    print('True')

n = 1
while n < 5:
    n+=1
print('\nn=',n)

for n in range(5):
    print(n)

# 6 non compreso
print('\n')
for n in range(2,6):
    print(n)

# Negative loops --> 2 non compreso
print('\n')
for i in range(5, 2, -1):
    print(i)

# Altri loop examples
nums = [1,2,3,4]

# Using index
print('\n')
for i in range(len(nums)):
    print(nums[i]) # 1 2 3 4

# Se non ci interessano gli index ma solo i valori
print('\n')
for n in nums:
    print(n)

# Se vogliamo sia valori che indici
print('\n')
nums = ['a','b','c','d']
for i,n in enumerate(nums):
    print(i,n) # 0a, 1b, 2c, 3d

# Ciclare su più array contemporaneamente (bah) --> se 2 array di lunghezza differente il ciclo
# si stoppa quando l'array più corto termina
print('\n')
nums1 = [1,2,3]
nums2 = [1,2,3,4]
for n1,n2 in zip(nums1, nums2):
    print(n1,n2)

# Reversing
print("reversing")
nums = [1,2,3,4]
nums2 = nums.copy()
nums2.reverse()
print(nums)
print(nums2)

# Sorting
nums = [5,4,7,3,8]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# Custom sorting. For example by string length
arr = ["ciao", "a", "pasta", "pera"]
arr.sort(key=lambda x: len(x)) # per ogni string assegniamo la lunghezza a key, la quale verrà utilizzata per il sort
print(arr)

# List comprehension
arr = [i+1000 for i in range(5)]
print(arr) # 1000, 1001, 1002, 1003, 1004

