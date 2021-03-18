from collections import deque

class Stack:
	def __init__(self):
		self.stringContainer = deque()
		
	def reverseString(self, string):
		tempText = ""
		for text in string:
			if text != " ":
				tempText += text
			else:
				Stack.push(self, tempText)
				tempText = ""
				
				
		print("Stack: ", self.stringContainer)
		
		returnString = ""
		
		while len(self.stringContainer) > 0:
			returnString += self.pop() + " "
			
		#length = len(returnString)-1
		return returnString
		
	def push(self, str):
		self.stringContainer.append(str)
		return
		
	def pop(self):
		return self.stringContainer.pop()
		
if __name__ == "__main__":
	stk = Stack()
	string = "My Name Is Shashiraj"
	string += " "
	result = stk.reverseString(string)
	print("Reverse String: ", len(result))
	print("Origina String: ", len(string))
	
	