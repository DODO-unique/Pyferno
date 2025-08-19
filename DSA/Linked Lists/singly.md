The concept of singly linked list is pretty simple—this image tells what it is quite clearly:

![Singly Linked List](image.png)

### Notice: 
1. How there are two parts of each 'node', one contains the data, the other points to the 'next' node (thus, here, called a 'pointer' container); this creates an unidirectonal flow, one node pointing to the next.
2. The first element is a 'Head' but that is not a node, just the initial pointer we will keep with ourselves
3. the end of a linked list is imagined with a Null pointer (`None`, you pricky bastard).
4. This is unidirectional, one pointer can't point to two addresses.

Here's a typical Singly Linked Lists code:

```python
class Node:

    def __init__(self, data):
        self.data = data      # store the data
        self.next = None      # pointer to the next node

    def __repr__(self):
        # note that you can't print non-string values here, also !r shows __str__ as __repr__ so you know when a string is being passed. Good practice to use that.
        return f'{self.data!r}'
    
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# and

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# They are functionally different.
the former is dynamic, it means, you can directly assign values as:
n1 = Node(1)
n2 = Node(2, next=n1)

the latter always sets next to None, so you have to manually change it each time like:
n1 = Node(1) # so here n1.data is 1, and n1.next is None
n2 = Node(2) # again, here n2.data is 2, and n2.next is None
# To point, you have to make a pointer, of course, so you go:
n2.next = n1 # now, n2 points to n1
'''

'''
About __repr__, it is object representation- note that down- it represents an object for us in developer redable format, by simply giving us a hint of what the object instance stands as in which class. 
You can use it with !r flag, which basically makes it true developer readable
for example:
    without !r:
        output: Node(Victor)
    with !r:
        output: Node('Victor')
So, though it is a string, it is shown that it is a string (and not just an object file or some sneaky, sussy generator expression 👀)
'''

'''
Memory and Performance
Python by default stores it's objects as __dict__, so when accessing attributes (baby raccoons read: an instance's variables 🧍‍♂️) they store values dynamically even if not defined in the __init__ (other static OOPs languages hiss at you if you do that)
This naturally increases the space consumed; to avoid this, and create actual C arrays (so faster lookups, saved space), we use __slots__ = ('data', 'next')
'''

'''
Mutability: 
Linked Lists are mutable, and if you think abuot it, a link list could be this: 3 -> [2,3,4] -> (3,5)
Here, the elements on the edge are immutable, so changing their values would mean rebinding; the middle element is mutable, so it does not really matter if you change it
The real understanding here is, that though you are changing each data type by changing Node.data, you are still changing *within* the same data structure which itself is mutable, even though their elements are mutable. This is a important understanding since it kind of aligns with what we learn in lists since they work similarly.
In a list, you'd change a immutable element but that does not mean a new instance of a list is created.

Thus, __eq__ (equality) is identity-based (through `is`), not content-based
'''


'''
Garbage Collection:
Simply, GC works when refcount drops to 0. 
The issue is when there are cyclic processes (refer to each other but no one points at them) are never noticed since their refcount never hits 0.
Theoretically, such processes are garbage since nothing points at them (they are hard to reach until you refer them from their own address).
You can have similar cyclic processes in linked lists, when you make the Null pointer point to the head of the list- this creates a cyclic process.
This also makes for a classic CS problem, 'Check if a linked list is cyclic' (simply checking for a Null pointer won't work since it would keep iterating)
As for Cyclic GC, these kill such cyclic processes periodically 
also, a rabbit hole here 👀
A CGC (cyclic garbage collecter) breaks when you use __del__ inside the cycle because python does not know in what order the destructor should be used without side-effects (because cyclic processes can be pretty subjective, if you think abou it)
'''

'''
Typing:
Python types dynamically (so the data types are resolved on runtime), this means if Linked Lists contain heterogenous objects, some actions won't work (like doing a sum) because let's be real, why should they, logically?
To avoid any caveats, you can add typing discipline from the typing library.
'''
'''
A big one:
I would add this in the main folders but hear me our carefully: __new__ comes first when a function is called- this is the true constructor, the second function is __init__ which initializes by assigning attributes.
so you can do this in your code:
class Trickster:
    def __new__(cls):
        print("haha nope, you get a dict")
        return {}
    def __init__(self):
        print("you’ll never see this")

This gives output of:
t = Trickster()
print(type(t))  # dict 
'''

```

```python
class LinkedList:
    def __init__(self):
        self.head = None
    '''
    here, self.head is declared dynamically here, so you can call obj.head (and it gives None until you don't define it)
    you define it by obj.head = nomnom, like that
    also, note that self means the object name and it all gets synonymous, and you no more have to define it during the instance definition
    '''

    def append(self, data):
        # if you are appending the first element? Head would still be None
        if not self.head:
            # we will add head as a Node, so it is not None anymore (if you are wondering if the class would retain this self.head(and not reset it to None), then know that this would be in an instance's schema, it is saved for the instance, and the init won't be called anymore again until you explicitly create a new instance of the same class 👀)
            self.head = Node(data)
            # since we are done creating a node, return and end this function right here 
            return
        
        # no? Then we will have to do two things: one, add a node, then give the node's address to the Null pointer
        # note how here, the node itself, by default, has new_node.next to None as we are defining a new instance, meaning the init runs over again once.
        new_node = Node(data)
        # now for step two, we have to go to the last pointer (Null Pointer) which we can go to by iteration
        # let's decide what is the current- naturally, the current would have to start from the head
        current = self.head
        # we iterate till current.next becomes None. The moment it hits None, it become falsey and while ends- so we are at the last element
        while current.next:
            # see how we are changing the current itself, so when the while ends, the current is spiritually the last node
            current = current.next
        # now, we just modify the next of the current node to point at the new node.
        current.next = new_node

    def print_traverse(self):
        # this is easy, you just have to iterate till you hit the Null pointer
        current = self.head

        while current.next:
            # note that here, repr prints non-human readable objects, you'd have to have a __repr__ class in your relevant class
            print(repr(current), end=' -> ')
            current = current.next
        print(repr(current))
    
    def insert(self, data, index):
        # if no list?
        if not self.head:
            self.head = Node(data)
            print("No list, made one for you 🦝")
            return
        
        # let's add a node first
        new_node = Node(data)

        # we move to the index now
        current = self.head
        for _ in range(index-1):
            current = current.next
            # if current.next is None, then we have reached the end of the list
            if not current.next:
                print('Reached the end of the list')
                return
        # copy the pointer to the new node's
        new_node.next = current.next
        # then assign the new value to the node
        current.next = new_node
        

    def delete(self, data):
        """This node deletes the first occurrence by value"""
        current = self.head
        # while current.next:
        #     prev = current.next
        #     # print('prev: ', current.prev)
        #     # print('of this', self.print_traverse())
        #     current = current.next
        #     if current.data == data:
        #         # print('stopped here', current.data, current.prev, current.next)
        #         prev.next = current
        #         # current.next = None
        #         # print('stopped here', current.data, current.prev, current.next)
        #         return
        if current and current.data == data:
            # if the first element is 
            self.head = current.next
            return

        # we are avoiding current being None so we can avoid AttributeErrors
        while current and current.data != data:
            prev = current
            current = current.next

        prev.next = current.next
```