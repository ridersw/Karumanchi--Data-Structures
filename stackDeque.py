#operations-

#append(x) - Add x to the right side of the deque.

#appendleft(x) - Add x to the left side of the deque.

#clear()- Remove all elements from the deque leaving it with length 0.

#copy() - Create a shallow copy of the deque.

#count(x) - Count the number of deque elements equal to x.

#extend(iterable) - Extend the right side of the deque by appending elements from the iterable argument.

#extendleft(iterable) Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.

#index(x[, start[, stop]])  Return the position of x in the deque (at or after index start and before index stop). Returns the first match or raises ValueError if not found.

#insert(i, x) - Insert x into the deque at position i. If the insertion would cause a bounded deque to grow beyond maxlen, an IndexError is raised.

#pop() - Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

#popleft() - Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

#remove(value) - Remove the first occurrence of value. If not found, raises a ValueError.

#reverse() - Reverse the elements of the deque in-place and then return None.

#rotate(n=1) - Rotate the deque n steps to the right. If n is negative, rotate to the left. When the deque is not empty, rotating one step to the right is equivalent to d.appendleft(d.pop()), and rotating one step to the left is equivalent to d.append(d.popleft()).

#maxlen - Maximum size of a deque or None if unbounded.

from collections import deque

class Stack:
	def __init__(self):
		self.container = deque()
		
	def push(self, data):
		self.container.append(data)
		
	def pop(self):
		if Stack.length(self):
			return self.container.pop()
		else:
			return "None, Stack is empty"
		
	def length(self):
		return len(self.container)
		
	def displayStack(self):
		return(self.container)
	
	def getLastElement(self):
		return self.container[-1]
	
if __name__ == "__main__":
	stk = Stack()
	
	stk.push("First")
	
	#print(stk.displayStack())
	
	stk.push("Second")
	
	#print(stk.getLastElement())
	
	print("Current Stack: ", stk.displayStack())
	
	print("Popped: ", stk.pop())
	
	print("Current Stack: ", stk.displayStack())
	
	print("Popped: ", stk.pop())
	
	print("Current Stack: ", stk.displayStack())
	
	print("Popped: ", stk.pop())
	print("Popped: ", stk.pop())
	print("Popped: ", stk.pop())
	
	
	
	