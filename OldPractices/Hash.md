## Hash

### Overview
Hashing is implemented in two steps:

An element is converted into an integer by using a hash function. This element can be used as an index to store the original element, which falls into the hash table.
The element is stored in the hash table where it can be quickly retrieved using hashed key.

hash = hashfunc(key)
index = hash % array_size

![b98001f0.png](attachments/b98001f0.png)


### Time Complexity
- Search: O(1)

### Simplist Case
- Given a list of (key, value) mapping
- `key mod length` to find the #slot of the value, then the operator "mod" is the Hash function.

### Hash Collision

### Reference
- [Basics of Hash Tables Tutorials & Notes \| Data Structures | HackerEarth](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)
- [数据结构之哈希表HashTable实例讲解_青山师-CSDN博客_哈希表例题讲解](https://blog.csdn.net/zixiao217/article/details/80593649)
