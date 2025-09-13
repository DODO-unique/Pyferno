Deque = Double-ended queues

* These data structs are basically queues that can be popped from left and right
* Lists, on the other hand, can be treated as a stack- where you can insert from one end only, and remove from the same, otherwise you get O(n) complexity
* In Deque, you have can simply do these:
  * deq.append()
  * deq.appendleft()
  * deq.pop()
  * deq.popleft()

So for Queue/sliding window/deque, use collection.deque