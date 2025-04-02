class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            parent = new_node.parent
            grandparent = parent.parent
            if parent == grandparent.right:
                uncle = grandparent.left
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    if new_node == parent.left:
                        new_node = parent
                        self.rotate_right(new_node)
                        parent = new_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)
            else:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    if new_node == parent.right:
                        new_node = parent
                        self.rotate_left(new_node)
                        parent = new_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot


'''
RED-BLACK TREES

A red-black tree is a kind of binary search tree that solves the "balancing" problem. 
It contains a bit of extra logic to ensure that as nodes are inserted and deleted, the tree remains relatively balanced.

How It Works

Each node in an RB Tree stores an extra bit, called the "color": either red or black. 
The "color" ensures that the tree remains approximately balanced during insertions and deletions. 
When the tree is modified, the new tree is rearranged and repainted to restore the coloring properties that constrain how unbalanced the tree can become in the worst case.

In a normal BST, the child nodes don't need to know about, or carry a reference to their parent. 
The same is not true for Red-Black trees.


Rules:

In addition to all the rules of a Binary Search Tree, a red-black tree must follow some additional ones:

    Each node is either red or black
    The root is black. 
        This rule is sometimes omitted. 
        Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
    All Nil leaf nodes are black.
    If a node is red, then both its children are black.
    All paths from a single node go through the same number of black nodes to reach any of its descendant NIL nodes.

The re-balancing of a red-black tree does not result in a perfectly balanced tree. 
However, its insertion and deletion operations, along with the tree rearrangement and recoloring, are always performed in O(log(n)) time.


Rotations:

"Rotations" are what actually keep a red-black tree balanced. 
Every time one branch of the tree starts to get too long, we will "rotate" those branches to keep the tree shallow. A shallow tree is a healthy (fast) tree!

    A properly-ordered tree pre-rotation remains a properly-ordered tree post-rotation
    Rotations are O(1) operations
    When rotating left:
        The "pivot" node's initial parent becomes its left child
        The "pivot" node's old left child becomes its initial parent's new right child
'''