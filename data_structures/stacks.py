class Stack:
    '''This is an example of a stack'''
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item

'''
STACKS

A stack is a data structure that stores ordered items. 
It's like a list, but its design is more restrictive.
It only allows items to be added or removed from the top of the stack.
It's called a "stack" because it behaves just like a stack of physical items. 
Imagine a stack of plates: it's easy to take an item off the top of the stack, but you can't really get to the items in the middle or at the bottom without removing the items on top first. 
You'll often hear a stack referred to as a LIFO (last in, first out) data structure.

You might be wondering, "why would I use a stack instead of a list?". 
"Isn't this just a list with fewer features?".

And you'd be right! A stack is a list with fewer features, but that's the point. 
By restricting the ways we can interact with the data, we guarantee that certain operations are blazingly fast. 
Here are all the operations a typical stack supports, along with their Big O time complexity:

Operation	Big O	Description
push	    O(1)	Add an item to the top of the stack
pop	        O(1)	Remove and return the top item from the stack
peek	    O(1)	Return the top item from the stack without modifying the stack
size	    O(1)	Return the number of items in the stack

It's all O(1)! 
That means no matter how many items are in the stack, these operations will always take the same amount of time. 
Stacks are really fast and are usually the best choice when the behavior of a stack is all you need.
'''