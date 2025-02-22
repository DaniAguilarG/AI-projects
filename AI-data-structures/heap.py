# Heaps (priority queues)
# Used in: Graph algorithms like shortest path 
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap) if self.heap else None

    def peek(self):
        return self.heap[0] if self.heap else None

    def __repr__(self):
        return str(self.heap)

# Example Usage
heap = MinHeap()
heap.push(10)
heap.push(5)
heap.push(20)
print(heap.pop())  # Output: 5 (smallest element)
print(heap)        # Output: [10, 20]
