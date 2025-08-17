class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        # note that you can't print non-string values here, also !r shows __str__ as __repr__ so you know when a string is being passed. Good practice to use that.
        return f'{self.data!r}'
    
class LinkedList:
    
    def __init__(self):
        self.head = None
    
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

    def reverse(self):
        perv = None
        current = self.head
        
        while current:
            nxt = current.next
            current.next = perv
            perv = current
            current = nxt
        self.head = perv
    
    def is_cyclic(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
           if fast == slow:
               print('cyclic')
               return 
        print('Not cyclic')

    def make_cylci(self):
        current = self.head
        while current.next:
            current = current.next
        current.next = self.head


nomnom = LinkedList()

nomnom.append(3)
nomnom.append(4)
nomnom.append(5)
nomnom.append(10)
nomnom.append(0)
nomnom.append(110)
nomnom.append(120)

nomnom.insert(1234, 5)
# nomnom.print_traverse()
nomnom.delete(1234)
nomnom.print_traverse()
nomnom.reverse()
nomnom.make_cylci()
nomnom.is_cyclic()
nomnom.print_traverse()