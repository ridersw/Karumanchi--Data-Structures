class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedList:
	def __init__(self):
		self.head = None
	
	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end = "-->")
			temp = temp.next
			
		print("None")
	
if __name__ == "__main__":
	llist = linkedList()
	
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	
	llist.head.next = second
	second.next = third
	
	llist.printList()