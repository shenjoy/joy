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
     
    def next_larger(self, node):
         if node.right is not None:
             return self.find_min(node.right)
         
         p = node.parent
         while p is not None and node is p.right:
             node = p
             p = p.parent
         return p
					
					
def test():
    nums = [7, 5, 9, 4, -3, 1]
    a = BST()
    for i in nums:
        a.insert(i)
    a.display()
    a.insert(11)
    a.display()
    n = a.search(4)
    m = a.next_larger(n)
    print m.value


if __name__ == '__main__':
    test()