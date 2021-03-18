from collections import deque

class Queue:
	def __init__(self):
		self.container = deque()
		
	def insert(self, data):
		self.container.appendleft(data)
		return
		
	def pop(self):
		self.container.pop()
		return
		
	def displayQueue(self):
		print("Queue: ", self.container)
		
		
if __name__ == "__main__":
	myQueue = Queue()
	
	myQueue.insert(5)
	
	myQueue.displayQueue()
	
	myQueue.insert(10)
	myQueue.insert(15)
	myQueue.insert(20)
	
	myQueue.displayQueue()
	
	myQueue.pop()
	
	myQueue.displayQueue()