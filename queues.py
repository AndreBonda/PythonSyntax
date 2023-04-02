# Queues (double ended queue)
from collections import deque
queue = deque() # double linked list
queue.append(1)
queue.append(2)
queue.append(3)
queue.remove(2)
print(queue)
print("First element: ", queue[0])

queue.pop() // 3
print(queue) # 1 2
queue.popleft()
print(queue) # 2

queue.appendleft(0);
print(queue) # 02

print(queue[1])