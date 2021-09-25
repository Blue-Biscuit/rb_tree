# IMPORTS

from enum import Enum

# CLASSES

class Color(Enum):
    RED = 0,
    BLACK = 1

class RBNode:
    def __init__(self, val, color, parent = None, leftChild = None, rightChild = None):
        self.Val = val
        self.Color = color
        self.Parent = parent
        self.LeftChild = leftChild
        self.RightChild = rightChild

class RBTree:
    def __init__(self):
        self.Root = None
        self.Count = 0
    
    def _fix_tree(self, loc):
        pass
    
    def insert(self, val):
        if (self.Root == None):
            self.Root = RBNode(val, Color.BLACK)
        else:
            next = self.Root
            inserted = False

            while (not inserted):
                if (val > next.Val):
                    if (next.RightChild == None):
                        next.RightChild = RBNode(val, Color.RED, next)
                        inserted = True
                    else:
                        next = next.RightChild
                else:
                    if (next.LeftChild == None):
                        next.LeftChild = RBNode(val, Color.RED, next)
                        inserted = True
                    else:
                        next = next.LeftChild

            self._fix_tree(next)




# FUNCTIONS

def main():
    pass

# STARTUP CODE

if (__name__ == "__main__"):
    main()