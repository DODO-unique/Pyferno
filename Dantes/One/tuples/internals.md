# Tuple Internals

Tuples are faster than lists- not crazy fast, but faster in general. 
They are faster in iteration and creation, mainly because python has to deal with lists dynamically since they are mutable

Interestingly, tuples are also smaller than lists. They are stored as fixed-length C array of pointers.

That said, tuples don't have hashtables like sets or dictionaries. You can convert it into hashes though- but only if it dooes not contain any mutable objects:

```python
tup1 = 1,2,3
tup2 = 1,[2,0]

hash(tup1) # This hashes it into a numerical format (which allocates a index in memory)
hash(tup2) #TypeError: unhashable type: 'list'
```
What are hashtables? [read this](..\..\universal\low-level\hashtables.md)

We dive into: PyTupleObject

Here, basically, CPython adds each element of a tuple in an array like:

```c
PyObject *ob_item[1];
```
So, each element in a tuple's body is 
    
    1. a python object
    2. not modifiable

Tuples are smaller than lists because they don't have the spare slots that list keeps (list keeps spare slots to append- this depends on a growth factor)
Tuples can also be interned/cached, so the address of a singleton (or, any small constant tuples) remains the same.

```py
import sys

t1 = (1,2, 3)
t2 = (1,2, 3)
l0 = [1,2, 3]

print(t1 is t2)
print(sys.getsizeof(l0), sys.getsizeof(t2))

s1 = ""
s2 = ""

print(s1 is s2)

l1 = []
l2 = []

print(l1 is l2)
```

```output
True
88 64
True
False
```

Notice how strings and tuples (both are immutables), intern smaller values of themselves, while list does not do it since it is mutable- appending one list could affect everything.

So, technically, immutables = interned, mutables = not interned.
So, monkey-wise, immutables = 🍌 storange, mutables = no 🍌 storage.
So, raccoon-wise - you get the point.

About iterations, tuples don't have over-allocation spaces, and they are prebuild (made during compilation).
Lists, instead, have extra spaces which make iteration take longer. Also, they are not prebuild, the objects inside it load at runtime.
**but**, and this is interesting, after python 3.12, even lists (if no mutation is seen) are prebuild 👀 


Nature of Tuple internal pointers:

```py
t = ([0],) * 3 # this makes the tuple be ([0], [0], [0])
t[0].append(1) # this should append to the first list.
```

```output
([0, 1], [0, 1], [0, 1])
```

This happens because when multiplying the same pointers are multipled (and remember, tuple is basically just an array of pointers in low-levels)


So, now, how would you define a tuple in advanced? 
“A Python tuple is a fixed-length PyTupleObject that stores only pointers to its elements in a contiguous C array (ob_item[]). It doesn’t own the elements’ memory, only references them. Lists work similarly but keep extra space for resizing, while sets and dicts use hash tables.” 
