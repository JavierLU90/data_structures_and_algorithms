class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        '''It takes a value as User class as input and adds it to a new node 
        if the value doesn't already exist in the tree.'''
        # if node does NOT have a value yet
        if not self.val:
            self.val = val
            return
        # if node's value is equal to the given value
        if self.val == val:
            return
        # if value is less than the node's value and the node does NOT have a left child
        if val < self.val and self.left is None:
            self.left = BSTNode(val)
        # if value is less than the node's value and the node DOES have a left child
        elif val < self.val and self.left is not None:
            self.left.insert(val)
        # if the node does NOT have a right child
        elif self.right is None:
            self.right = BSTNode(val)
        # if the node DOES have a right child
        else:
            self.right.insert(val)
        
    def get_min(self):
        '''Returns minimum value (the left-most node of the tree)'''
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        '''Returns maximum value (the right-most node of the tree)'''
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    
    def delete(self, val):
        '''It takes a value as an input and delete the node with that value if it exists. 
        In doing so, it will return the appropriate node.'''
        if self.val is None:
            # if value is None then it represents an empty tree or leaf node
            return None
        # check the left side of the tree for the value
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        # check the right side of the tree for the value
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        # value equal -> node to delete
        if val == self.val:
            if self.right is None:
                # if no right value, returns left value (bypasses it)
                return self.left
            elif self.left is None:
                # if no left value, returns right value (bypasses it)
                return self.right
            else:
                # find the minimum larger node
                min_larger_node = self.right
                while min_larger_node.left is not None:
                    min_larger_node = min_larger_node.left
                self.val = min_larger_node.val
                self.right = self.right.delete(min_larger_node.val)
                return self
    
    def preorder(self, visited):
        '''It returns a list of the values in the order they are visited, 
        and it takes as an argument the ordering of values we have visited so far.'''
        if self.val is not None:
            visited.append(self.val)
        if self.left is not None:
            self.left.preorder(visited)
        if self.right is not None:
            self.right.preorder(visited)
        return visited

    def postorder(self, visited):
        '''Same as preorder, but it visits the children before the parents'''
        if self.left is not None:
            self.left.postorder(visited)
        if self.right is not None:
            self.right.postorder(visited)
        if self.val is not None:
            visited.append(self.val)
        return visited
    
    def inorder(self, visited):
        ''' It's called "inorder" because the current node is visited between its children.
        It results in an ordered list of the nodes in the tree.'''
        if self.left is not None:
            self.left.inorder(visited)
        if self.val is not None:
            visited.append(self.val)
        if self.right is not None:
            self.right.inorder(visited)
        return visited
    
    def exists(self, val):
        ''' Takes a value as input and return True if the value exists in the tree, 
        and False if it doesn't.'''
        if val == self.val:
            return True
        # if value is less than current value -> check left side
        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)
        # check right side
        if self.right is None:
            return False
        return self.right.exists(val)
    
    def search_range(self, lower_bound, upper_bound):
        '''It takes two arguments, lower_bound and upper_bound (which are User nodes themselves), 
        and returns a list of nodes that fall within the specified range, inclusive.'''
        nodes_list = []
        if self.val is None:
            return nodes_list
        if lower_bound < self.val and self.left is not None:
            nodes_list.extend(self.left.search_range(lower_bound, upper_bound))
        if lower_bound <= self.val <= upper_bound:
            nodes_list.append(self.val)
        if self.val < upper_bound and self.right is not None:
            nodes_list.extend(self.right.search_range(lower_bound, upper_bound))
        return nodes_list
    
    def height(self):
        '''It returns the height of the tree rooted at the current node'''
        if self.val is None:
            return 0
        left_height = 0
        right_height = 0
        if self.left is not None:
            left_height = self.left.height()
        if self.right is not None:
            right_height = self.right.height()
        return max(left_height, right_height) + 1

'''
BINARY TREES

Trees are a widely used data structure that simulate a hierarchical... well... tree structure. 
That said, they're typically drawn upside down - the "root" node is at the top, and the "leaves" are at the bottom.

Trees are kind of like linked lists in the sense that the root node simply holds references to its child nodes, which in turn hold references to their children. 
The difference between a Linked List and a Tree is that a tree's nodes can have multiple children instead of just one.

A generic tree structure has the following rules:
    Each node has a value and a list of "children"
    Children can only have a single "parent"

Trees aren't particularly useful data structures unless they're ordered in some way. 
One of the most common types of ordered tree is a Binary Search Tree or BST. 
In addition to the properties we've already talked about, a BST has some additional constraints:

    Instead of an unbounded list of children, each node has at most 2 children
    The left child's value must be less than its parent's value
    The right child's value must be greater than its parent's value
    No two nodes in the BST can have the same value

By ordering the tree this way, we'll be able to add, remove, find, and update nodes much more quickly.

'''