class Graphs:
	def __init__(self, edges):
		self.edges = edges
		
		self.routeDict = {}
		
		for start, end in edges:
			if start in self.routeDict:
				self.routeDict[start].append(end)
			else:
				self.routeDict[start] = [end]
				
	def printGraph(self):
		print(self.routeDict)
		
	def findPaths(self, start, end, path = []):
		path = path + [start]
		
		if start == end:
			return [path]
			
		if start not in self.routeDict:
			return []
			
		paths = []
		
		for node in self.routeDict[start]:
			if node not in path:
				newPath = self.findPaths(node, end, path)
				for p in newPath:
					paths.append(p)
					
		return paths
		
	def getMinimumPath(self, start, end, path = []):
		
		path = path + [start]
		
		if start == end:
			return path
		
		if start not in self.routeDict:
			return None
			
		shortestPath = None
			
		for node in self.routeDict[start]:
			if node not in path:
				sp = self.getMinimumPath(node, end, path)
				if sp:
					if shortestPath is None or len(sp) < len(shortestPath):
						shortestPath = sp
						
		return sp
			

if __name__ == "__main__":
	routes = [
		("Mumbai", "Paris"),
		("Mumbai", "Dubai"),
		("Paris", "Dubai"),
		("Paris", "New York"),
		("Dubai", "New York"),
		("New York", "Toronto")
	]
	
	theRouteGraph = Graphs(routes)
	
	#theRouteGraph.printGraph()
	#{'Mumbai': ['Paris', 'Dubai'], 'Paris': ['Dubai', 'New York'], 'Dubai': ['New York'], 'New York': ['Toronto']}
	
	start = "Mumbai"
	end = "New York"
	
	print(f"Path between {start} and {end}: ",theRouteGraph.findPaths(start, end))
	print(f"Shortest Path between {start} and {end}: ",theRouteGraph.getMinimumPath(start, end))
	
	
	