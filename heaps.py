import heapq

# under the hood heaps are built with arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

print(minHeap)

# Min value is always at index 0
print(minHeap[0])

print()
while len(minHeap):
    print(heapq.heappop(minHeap))

# Non esistono max heap, ma si possono implementare con un work around, utilizzando un min heap e
# moltiplicando per -1 quando invochiamo push & pop
print()
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])

# build heap from initial values in O(N)
print()
arr = [2,1,7,4,6,8]
heapq.heapify(arr)
print(arr)