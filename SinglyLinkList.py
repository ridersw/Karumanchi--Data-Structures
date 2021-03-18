class Node:
	#to create a node without any connections
	def __init__(self, data, next = None):
		self.data = data
		self.next = next
		
class LinkedList:
	#to create an empty link list
	def __init__(self):
		self.head = None
		
	#to print the link list
	#First --> Second --> None
	def printLinkedList(self):
		temp = self.head
		while temp:
			print(temp.data, end = " --> ")
			temp = temp.next
			
		print("None")
		
	#add node at beginning
	#output: Third --> First --> Second --> None
	def addNewNodeAtBeginning(self, data):
		node = Node(data, self.head)
		self.head = node
	
	#add node at end if last element is unknown
	def addNewNodeAtEnd(self, data):
		temp = self.head
		while temp:
			if temp.next != None:
				temp = temp.next
			else:
				break
		
		temp.next = Node(data)
		
	#delete node
	def deleteNode(self, deleteData):
		temp = self.head
		
		totalLength = llist.lengthOfLinkList()
		
		elementAt = llist.findElementIndex(deleteData)
		
		swi = 0
		
		print("Removing element at Index: ", elementAt)
		print("Total Length: ", totalLength)
		
		while swi < totalLength:
			if swi == (elementAt-1):
				temp1 = temp.next
				temp2 = temp1.next
				
				temp.next = temp2
				break
			
			temp = temp.next
			swi += 1
		
		llist.printLinkedList()
		
		#if length > 0 
		
	def lengthOfLinkList(self):
		length = 0
		
		temp = self.head
		
		while temp.next != None:
			length += 1
			temp = temp.next
		
		return length+1
		
		
	def findElementIndex(self, deleteData):
		temp = self.head
		tempIndex = 0
		while temp.data != deleteData:
			tempIndex += 1
			temp = temp.next
		
		#print("Element to delete: ", temp.data)
		return tempIndex
	
if __name__ == "__main__":
	#creating emply link list
	llist = LinkedList()
	
	#defining head Node and one another node
	llist.head = Node("First")
	second = Node("Second")
	
	#connecting second node to first's tail
	llist.head.next = second
	
	llist.printLinkedList()
	
	#adding another node at beginning
	llist.addNewNodeAtBeginning("Third")
	
	llist.printLinkedList()
	
	#adding another node to 
	fourth = Node("Fourth")
	second.next = fourth
	
	llist.printLinkedList()
	
	llist.addNewNodeAtBeginning("Fifth")
	
	llist.printLinkedList()
	
	#adding node at end when last element is not known
	llist.addNewNodeAtEnd("Sixth")
	
	llist.printLinkedList()
	
	#delete node
	llist.deleteNode("Fourth")
	
	