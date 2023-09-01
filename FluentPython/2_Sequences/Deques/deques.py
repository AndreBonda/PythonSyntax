from collections import deque

dq = deque(range(10))
print(dq) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dq.rotate(2)
print(dq) # deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
dq.appendleft(30)
print(dq) # deque([30, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
dq.extend([77,88])
print(dq) # deque([30, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 77, 88])
dq.extendleft([200])
print(dq) # deque([200, 30, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 77, 88])

# max-length
dq = deque(range(10), maxlen=10)
print(dq) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.append(50) # poiché è full scarta l'elemento in posizione opposta (a sinistra in questo caso)
print(dq) # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 50], maxlen=10)
dq.appendleft(80)
print(dq) # deque([80, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
