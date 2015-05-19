class Colors():
    RED = 0
    BLACK = 1



class Node():
    def __init__(self):
        self.key = None
        self.p = None
        self.left = None
        self.right = None
        self.color = None


class RBTree():
    def __init__(self):
        self.root = None
        self.nil = Node()
        self.nil.color =\
                Colors.BLACK

    def re_insert_fixup(self, z):
        while z.p.color == Colors.RED:
            pass
        
    def insert(self, z):
        if self.root is None:
            self.root = z
            return
        y = None
        x = self.root
        while x is not self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = Colors.RED




print Colors.RED
