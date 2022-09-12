## Heap

### Background
In many computer science applications, we only need to access the largest or smallest element in the dataset. We do not care about the order of other data in the data set. How do we efficiently access the largest or smallest element in the current dataset? The answer would be Heap.

**PriorityQueue**: Wikipedia: a priority queue is an abstract data type similar to a regular queue or stack data structure in which each element additionally has a "priority" associated with it. In a priority queue, an element with high priority is served before an element with low priority.

### Definition
A Heap is a special type of binary tree. A heap is a binary tree that meets the following criteria:
- Is a complete binary tree;
- The value of each node must be no greater than (or no less than) the value of its child nodes.

### Complexity
- Insertion of an element into the Heap has a time complexity of O(logN);
- Deletion of an element from the Heap has a time complexity of O(logN);
- The maximum/minimum value in the Heap can be obtained with O(1) time complexity.

### Classification of Heap
There are two kinds of heaps: Max Heap and Min Heap.

- Max Heap: Each node in the Heap has a value no less than its child nodes. Therefore, the top element (root node) has the largest value in the Heap.

- Min Heap: Each node in the Heap has a value no larger than its child nodes. Therefore, the top element (root node) has the smallest value in the Heap.

### Python Heap
Python heapq can only heapify the list into a Min-heap, so to implement a Max-heap, we need to negative all the numbers in the list. 
```Python
# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", end="")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))
```