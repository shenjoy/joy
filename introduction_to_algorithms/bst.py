# shennian
class Node():
    def __init__(self, value = 0, left = None,
                    right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        p = None
        node = self.root
        while node is not None:
            p = node
            if value < node.value:
                node = node.left
            else:
                node = node.right

        if value < p.value:
            node = Node(value)
            p.left = node
            node.parent = p
        else:
            node = Node(value)
            p.right = node
            node.parent = p

    def display(self):
        node = self.root

        def show(node):
            if node is None:
                return
            show(node.left)
            print node.value,
            show(node.right)

        show(node)
        print ""


    def search(self, k):
        node = self.root
        while node is not None:
            if k < node.value:
                node = node.left
            elif k > node.value:
                node = node.right
            else:
                break
        return node

    def find_min(self, node):
         while node.left is not None:
             node = node.left
         return node

    def find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def next_larger(self, node):
         if node.right is not None:
             return self.find_min(node.right)

         p = node.parent
         while p is not None and node is p.right:
             node = p
             p = p.parent
         return p

    def next_smaller(self, node):
        if node.left is not None:
            return self.find_max(node.left)

        p = node.parent
        while p is not None and p.left is node:
            node = p
            p = p.parent
        return p

    def delete(self, node):
        if node.left is None and node.right is None:
            if node.parent.left is node:
                node.parent.left = None
            else:
                node.parent.right = None
            del node

        elif node.left is None:
            p = node.parent
            if p.left is node:
                p.left = node.right
            else:
                p.right = node.right
            del node

        elif node.right is None:
            p = node.parent
            if p.left is node:
                p.left = node.left
            else:
                p.right = node.right
            del node

        else:
            _node = self.next_larger(node)
            _node.parent.left = _node.right
            if node.parent is None:
                self.root = _node
            elif node.parent.left is node:
                node.parent.left = _node
            else:
                node.parent.right = _node
            _node.parent = node.parent
            _node.left = node.left
            _node.right = node.right
            del node







def test():
    nums = [7, 2, 11, -3, 0, 1, 13, 8, 12, 16, 17, 19]
    a = BST()
    for i in nums:
        a.insert(i)
    a.display()
    #a.insert(11)
    #a.display()
    n = a.search(16)
    m = a.next_larger(n)
    #print m.value
    #print a.find_max(n).value
    #print a.next_smaller(n).value
    a.delete(n)
    a.display()


if __name__ == '__main__':
    test()
