class Queue:
    '''This is an example of a queue'''
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


'''
QUEUES

A queue is a data structure that stores ordered items. 
It's like a list, but again, like a stack, its design is more restrictive. 
A queue only allows items to be added to the tail of the queue and removed from the head of the queue.

It's called a "queue" because it behaves like a queue of people waiting in line. 
The first person to get in line is the first person to get out of line. 
You'll often hear a queue referred to as a FIFO (first in, first out) data structure.
'''