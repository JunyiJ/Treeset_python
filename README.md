# Table of Contents
1. [Prerequisites](README.md#Prerequisites)
2. [Aim](README.md#Aim)
3. [How to use](README.md#How-to-use)
4. [Implementation details](README.md#Implementation-details)
5. [Directory structure](README.md#directory-structure)


## Prerequisites


Python 2

## Aim


A lot of real life problems require to keep and update certain record in an ordered way.
One example is to use a data structure to store stock names and stock prices coming as a stream.
Once in a while, we would like to get the top k stocks with highest prices.
TreeSet is a proper data structure to solve these kind of problems. Implemented as a red black tree,
TreeSet can achieve O(log(n)) time complexity for insertion/update and O(k) time complexity to get the top k stocks.


TreeSet is implemented and widely used in Java and C++, however, Python doesn't include the TreeSet structure in its 
standard library.

Here I implemented red black tree and TreeSet in python and provides the commonly used method as it is in Java.


## How-to-use


The TreeSet class has the following available methods:


`add(key, val)`: add specified (key, val) pair to TreeSet


`addAll(elements)`: add all (key, val) pairs in elements to TreeSet


`remove(key)`: remove key from TreeSet if exists


`clear()`: reset the TreeSet to be empty


`contains(key)`: return True if key is found in TreeSet


`first()`: return the (key, val) with key be the smallest of all keys is exists. Otherwise return None


`last()`: return the (key, val) with key be the largest of all keys is exists. Otherwise return None


`headSet(tokey)`: return (key, val) pairs which are less than tokey


`tailSet(fromkey)`: return (key, val) pairs which are greater or equal to fromkey


`subSet(self, fromkey, tokey)`: return (key, val) pairs within range [fromkey, tokey)


`print_tree()`: print the redblacktree in bfs for debug



## Implementation-details


coming soon.
Please refer the source code for now.



## Directory-structure


    ├── README.md 
    ├── src
    |   └── __init__.py
    |   └── Red_Black_Tree.py
    |   └── TreeSet.py	

	