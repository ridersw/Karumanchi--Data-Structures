class Stack(object):
	def __init__(self, items=[]):
		self.stack = items
		
	def isEmpty(self):
		return not self.stack
		
	def pop(self):
		return self.stack.pop()
		
	def push(self, data):
		return self.stack.append(data)
		
	def __repr__(self):
		return "Stack{0}".format(self.stack)
		
	def reverseStack(stack):
		def reverseStackRecursive(stack, newStack=Stack()):
			if not stack.isEmpty():
				newStack.push(stack.pop())
				reverseStackRecursive(stack, newStack)
			return newStack
		return reverseStackRecursive(stack)
stk = stack(range(10))
	
print(stk)
print(reverseStack(stk))