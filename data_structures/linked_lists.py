class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


class LLQueue:
    def add_to_head(self, node):
        if self.head is None:
            self.tail = node
        node.set_next(self.head)
        self.head = node
    
    def remove_from_head(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return temp

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)


'''
LINKED LISTS

To be able to build our faster queue, we're going to need to use a Linked List instead of an array under the hood. 
A linked list is a linear data structure where elements are not stored next to each other in memory. 
The elements in a linked list are linked using references to each other.

A linked list is a collection of ordered items. In that way, it's similar to a "normal" list (also called an "array" or "slice" in other languages).

The difference is that Items in a "normal" list are stored next to each other in memory, and to get an item from a List we use a numbered index:

    car = cars[1]

You can think of the "index" as simply an offset from the start. 
With a normal list, all the data is stored in the same place in memory and the index is just a way to find the right spot.

In a linked list, there are no indexes. 
Each node contains the data itself as well as a reference to the next node in the list. 
Iterating over a linked list requires starting at the head node and following the next references until you reach the end.

    current_car_node = head_car_node
    while current_car_node is not None:
        print(current_car_node.val)
        current_car_node = current_car_node.next

This kind of iteration is annoying, and has more overhead, so why use a linked list? 
We use them sometimes because linked lists are much faster to make updates to, particularly when inserting or deleting items from the middle.

In a normal list, if you insert an item in the middle, you have to shift all the items after it down one spot (O(n)).

In a linked list, once you've traversed to a given node, insertion is (O(1)) because you can simply update two references.

'''