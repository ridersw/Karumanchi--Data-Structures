class binarySearchTree:
	def __init__(self, data):
		#creating a node with data and no left/ right node
		self.data = data
		self.left = None
		self.right = None
		
	def addChild(self, data):
		
		if self.data == data:
			#to avoid duplicate
			return
			
		if self.data < data:
			#the data will go in right subtree
			if self.right:
				#if the tree already has right element, implement the function again
				return self.right.addChild(data)
			else:
				#node has no right node so add data as binarySearchTree Node with no left and right 
				self.right = binarySearchTree(data)
		
		if self.data > data:
			#the data will go in left subtree
			if self.left:
				return self.left.addChild(data)
			else:
				self.left = binarySearchTree(data)
				
	def inorderTraversal(self):
		#format : <left Sub tree> <Root Node> <Right Sub Tree>
		elementsInorder = []
		
		if self.left:
			elementsInorder += self.left.inorderTraversal()
			
		elementsInorder.append(self.data)
		
		if self.right:
			elementsInorder += self.right.inorderTraversal()
			
		return elementsInorder
		
	def preorderTraversal(self):
		#format: <Root Node> <Left Subtree> <Right Subtree>
		elementsPreorder = []
		
		elementsPreorder.append(self.data)
		
		if self.left:
			elementsPreorder += self.left.preorderTraversal()
			
		if self.right:
			elementsPreorder += self.right.preorderTraversal()
			
		return elementsPreorder
		
	def postorderTraversal(self):
		#format: <right subtree> <left subtree> <root node>
		elementsPostorder = []
		
		if self.left:
			elementsPostorder += self.left.postorderTraversal()
		
		if self.right:
			elementsPostorder += self.right.postorderTraversal()
			
		
			
		elementsPostorder.append(self.data)
		
		return elementsPostorder
		
	def searchElement(self, element):
		if self.data == element:
			return True
		
			
		if self.data < element:
			if self.right:
				return self.right.searchElement(element)
			else:
				return False
				
		else:# self.data > element:
			if self.left:
				return self.left.searchElement(element)
			else:
				return False
		
	def findMin(self):
		if self.left:
			return self.left.findMin()
		else:
			return self.data
		
	def findMax(self):
		if self.right:
			return self.right.findMax()
		else:
			return self.data

def buildTree(numbers):
	root = binarySearchTree(numbers[0])
	
	for swi in range(1, len(numbers)):
		root.addChild(numbers[swi])
		
	return root

if __name__ == "__main__":
	numbers = [15,12,27,7,14,20,88,23]
	
	numbersTree = buildTree(numbers)
	
	#print("numbersTree: ", numbersTree.right.left.data)
	
	InorderTraversalTree = numbersTree.inorderTraversal()
	
	print("InorderTraversalTree: ", InorderTraversalTree)
	
	preorderTraversalTree = numbersTree.preorderTraversal()
	
	print("PreOrderTraversal: ", preorderTraversalTree)
	
	postorderTraversalTree = numbersTree.postorderTraversal()
	
	print("PostOrderTraversal: ", postorderTraversalTree)
	
	print("Max Value in Tree: ", numbersTree.findMax())
	
	print("Min Value in Tree: ", numbersTree.findMin()) 
	
	#InorderTraversalTree.buildPostOrderTree(preorderTraversalTree)
	
	print("Is 20 Present in Tree?: ", numbersTree.searchElement(20))