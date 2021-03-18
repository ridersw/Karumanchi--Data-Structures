class TreeNode:
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None
		
	def addChild(self, child):
		child.parent = self
		self.children.append(child)
		
	def getLevel(self):
		level = 0
		p = self.parent
		while p:
			level += 1
			p = p.parent
		
		return level
		
	def printTree(self):
		spaces = ' ' * self.getLevel() * 3
		prefix = spaces + '|--' if self.parent else ""
		print(prefix + self.data)
		if self.children:
			for child in self.children:
				child.printTree()
	
def buildProductTree():
	root = TreeNode("Electronics")
	
	laptop = TreeNode("Laptop")
	laptop.addChild(TreeNode("Asus"))
	laptop.addChild(TreeNode("Macbook Pro"))
	laptop.addChild(TreeNode("Macbook Air"))
	
	mobile = TreeNode("Mobile")
	mobile.addChild(TreeNode("OnePlus"))
	mobile.addChild(TreeNode("iPhone"))
	mobile.addChild(TreeNode("Samsung"))
	
	headphones = TreeNode("Head Phones")
	headphones.addChild(TreeNode("Jabra"))
	headphones.addChild(TreeNode("Airpods"))
	headphones.addChild(TreeNode("Xaomi"))
	
	root.addChild(laptop)
	root.addChild(mobile)
	root.addChild(headphones)
	
	return root

if __name__ == "__main__":
	root = buildProductTree()
	root.printTree()
	
	#print("Tree: ", root.data)