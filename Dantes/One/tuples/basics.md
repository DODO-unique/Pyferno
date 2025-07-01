# Basics of tuples.

Tuples:

1. Are immutable
2. Are indexed
3. Can be sliced
4. Allow duplicates
5. Can contain any elements

## Creation:

Tuples are created as:

```python
t = () #Empty tuple
t = (42, ) #Signleton tuple
t = (1, 2, 3) # general tuple
```

> Note the sigleton tuple

## packing and unpacking

Tuples can be packed and unpacked efficiently:

```python
t = 1,2,3 # packs them into a tuple t
a, b, c = t # assigns a = 1, b = 2, c = 3
```

Tuple can hold mutable elements; mutable elements are mutable inside a tuple.

```python
t = (1,[2,0])
t[1][1] #gives 0 from the list, this is mutable
t[1][1] = 41 # now t = (1,[2,41]) and no new object was created in this process

# Extended unpacking:
a, *b, c, d = (1,2,3,4,5) # so a=1, b=[2,3], c=4, d=5
```

## What is the deal with tuple() constructor?
```python
tuple("abc") # ('a', 'b', 'c')
```
