"""
Bynary Search Tree in Python

Algorithm:

    1. Create a node with the value of the root
    2. If the value of the root is less than the value of the node,
         then the node is inserted to the left of the root
    3. If the value of the root is greater than the value of the node,
            then the node is inserted to the right of the root
    4. If the value of the root is equal to the value of the node,
            then the node is inserted to the left of the root
"""


class Node:# Create a node class
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree: # Create a binary search tree class
    def __init__(self):
        self.root = None # Initialize the root to None

    def insert(self, value): # Insert a value to the tree
        if self.root is None:   # If the tree is empty
            self.root = Node(value) # Create a node with the value of the root
        else: # If the tree is not empty
            self._insert(value, self.root) # Insert the value to the tree

    def _insert(self, value, node): # Insert a value to the tree
        if value < node.value: # If the value is less than the value of the node
            if node.left is None: # If the left node is empty
                node.left = Node(value) # Create a node with the value of the node
            else: # If the left node is not empty
                self._insert(value, node.left) # Insert the value to the left node
        else: # If the value is greater than the value of the node
            if node.right is None: # If the right node is empty
                node.right = Node(value) # Create a node with the value of the node
            else:   # If the right node is not empty
                self._insert(value, node.right) # Insert the value to the right node

    def search(self, value): # Search for a value in the tree
        if self.root is None: # If the tree is empty
            return False # Return False
        else: # If the tree is not empty
            return self._search(value, self.root) # Search for the value in the tree

    def _search(self, value, node): # Search for a value in the tree
        if value == node.value: # If the value is equal to the value of the node
            return True # Return True
        elif value < node.value: # If the value is less than the value of the node
            if node.left is None: # If the left node is empty
                return False # Return False
            else:   # If the left node is not empty
                return self._search(value, node.left) # Search for the value in the left node
        else: # If the value is greater than the value of the node
            if node.right is None: # If the right node is empty
                return False # Return False
            else:  # If the right node is not empty
                return self._search(value, node.right) # Search for the value in the right node

    def print_tree(self): # Print the tree
        if self.root is None:   # If the tree is empty
            print("Tree is empty")   # Print the tree is empty
        else: # If the tree is not empty 
            self._print_tree(self.root) # Print the tree

    def _print_tree(self, node): # Print the tree
        if node is not None:  # If the node is not empty
            self._print_tree(node.left) # Print the left node
            print(str(node.value)) # Print the value of the node
            self._print_tree(node.right) # Print the right node


# Test 
tree = BinarySearchTree() # Create a binary search tree
tree.insert(10) # Insert 10 to the tree
tree.insert(5)  # Insert 5 to the tree
tree.insert(15) # Insert 15 to the tree
tree.insert(3) # Insert 3 to the tree
tree.insert(7)  # Insert 7 to the tree
tree.insert(13)  # Insert 13 to the tree
tree.insert(17) # Insert 17 to the tree
tree.insert(2)  # Insert 2 to the tree


tree.print_tree() # Print the tree
print(tree.search(10)) # Search for 10 in the tree