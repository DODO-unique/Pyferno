# Tuple Internals

Tuples are faster than lists- not crazy fast, but faster in general. 
They are faster in iteration and creation, mainly because python has to deal with lists dynamically since they are mutable

Interestingly, tuples are also smaller than lists. They are stored as fixed-length C arrays.

That said, tuples don't have hashtables like sets or dictionaries. You can convert it into hashes though- but only if it dooes not contain any mutable objects:

```python
tup1 = 1,2,3
tup2 = 1,[2,0]

hash(tup1) # This hashes it into a numerical format (which allocates a index in memory)
hash(tup2) #TypeError: unhashable type: 'list'
```
What are hashtables? [read this](Dantes\Zero\hashtables.md)

We dive into: PyTupleObject

Here, basically, CPython adds each element of a tuple in a array like:

    ```c
    PyObject *ob_item[1];
    ```
So, each element in a tuple's body is 
    
    1. a python object
    2. not modifiable

