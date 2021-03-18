class binarySearchTreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
	def addChild(self, data):
		if data == self.data:
			return
			
		if data < self.data:
			#data goes to left subtree
			if self.left:
				self.left.addChild(data)
			else:
				self.left = binarySearchTreeNode(data)
		else:
			#data goes to right subtree
			if self.right:
				self.right.addChild(data)
			else:
				self.right = binarySearchTreeNode(data)
				
	def inorderTraversal(self):
		elements = []
		
		#visit left tree first
		if self.left:
			#print("self.")
			elements += self.left.inorderTraversal()
		
		#visit base node
		elements.append(self.data)
		
		
		if self.right:
			elements += self.right.inorderTraversal()
		
		return elements
		
	def searchElement(self, val):
		if self.data == val:
			print("self.data == val")
			return True
		
		if val < self.data:
			if self.left:
				print("self.left:")
				return self.left.searchElement(val)
			else:
				return False	
		else:
			if self.right:
				print("self.right:")
				return self.right.searchElement(val)
			else:
				return False	

def buildTree(elements):
	root = binarySearchTreeNode(elements[0])
	
	for swi in range(1, len(elements)):
		root.addChild(elements[swi])
		
	return root
		
if __name__ == "__main__":
	numbers = [17, 4, 1, 20, 9, 23, 18, 34]
	
	numbersTree = buildTree(numbers)
	
	#print(numbersTree.inorderTraversal())
	
	toFind = 18
	
	print(numbersTree.searchElement(18)) 