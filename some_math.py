# Division is decimal by default
print(5 / 2) # --> 2.5

# Division with integer result
print(5 // 2) # --> 2

# La maggior parte dei linguaggi arrotonda verso lo 0, mentre python
# arrotonda verso lo zero.
print(-3 // 2) # --> -2

# Workaround per arrotondamento di un numero negativo verso lo 0
print(int(-3 / 2)) # -3 / 2 = -1.5 --> int(-1.5) --> -1

# Modding
print(10 % 3) # 1
print(-10 % 3) # 2

# Modding compliance with other programming languages
import math
print(math.fmod(-10, 3)) # -1.0

# Math helpers
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(9)) # 3.0
print(math.pow(2, 3)) # 8.0

# Max / Min Int
print(float("inf"))
print(float("-inf"))

# Python numbers are infinite so they never overflow

# Min between numbers
min = min(1,2,3, -5)
print(min)