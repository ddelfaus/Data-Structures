import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
#Day 1 plan
#insert value
#if there is no node at root insert this as root
#Compare value to the root
#if value is smaller:
    #look left if node, repeat steps
    #if no node make new one with this value
#this value
#if value is greater or equal
    #look right, if node repeat steps
    #if no node: make new one with value

#contains
#if no node at root, return false
#compare value to root 
#if smaller:
    #go left. look at node there
#if greater or ==:
    #go right

#Get Max:
#if no right child, return this value
#otherwise,go right

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #base case is when it insert something
        #left
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        #right
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right= BinarySearchTree(value)
    

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #base case when it matches the target
        if self.value == target:
            return True

        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        
        if  target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
