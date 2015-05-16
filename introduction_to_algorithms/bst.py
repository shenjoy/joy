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
			p.left = Node(value)
		else:
			p.right = Node(value)
	
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
	
	
		
		

def test():
    nums = [7, 5, 9, 4, -3, 1]
    a = BST()
    for i in nums:
        a.insert(i)
    a.display()
    a.insert(5)
    a.display()


if __name__ == '__main__':
	test()