import time
import threading
from collections import deque

class Queue:
	def __init__(self):
		self.orderQueue = deque()
		
	def enqueue(self, order):
		self.orderQueue.appendleft(order)
		
	def dequeue(self):
		while len(self.orderQueue) > 0:
			return self.orderQueue.pop()
			
	def lengthOfQueue(self):
		return len(self.orderQueue)
			
myQueue = Queue()		

def placeOrder(orderArray):
	for orders in orderArray:
		print("Order Placed: ", orders)
		myQueue.enqueue(orders)
		time.sleep(0.5)
	
def serveOrder():
	time.sleep(1)
	while myQueue.lengthOfQueue() > 0:
		item = myQueue.dequeue()
		print("Order Served: ", item)
		time.sleep(2)
		
		
	print("No more Orders in the Queue")

	
if __name__ == "__main__":
	orderArray = ['pizza','samosa','pasta','biryani','burger']
	
	t1 = threading.Thread(target = placeOrder, args = (orderArray,))
	t2 = threading.Thread(target = serveOrder)
	
	t1.start()
	t2.start()
	