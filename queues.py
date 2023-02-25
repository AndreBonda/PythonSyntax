# Queues (double ended queue)
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.pop()
print(queue) # 1 2
queue.popleft()
print(queue) # 2

queue.appendleft(0);
print(queue) # 02