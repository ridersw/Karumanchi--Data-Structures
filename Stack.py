from collections import deque

class stacksImplementation:
	def __init__(self):
		self.theStack = []
		
	def add(self, data):
		self.theStack.append(data)
		
	def show(self):
		print("Stack: ", theStack)
		
if __name__ == "__main__":
	stack = stacksImplementation
	
	stack.add('1')
	stack.show()