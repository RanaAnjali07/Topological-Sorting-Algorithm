
class Graph:
	def __init__(self, edges, V):

	    
		self.adjList = [[] for _ in range(V)]

		self.indegree = [0] * V

		for (src, dest) in edges:

			self.adjList[src].append(dest)

			self.indegree[dest] = self.indegree[dest] + 1

def findAllTopologicalOrders(graph, path, discovered, V):

	for v in range(V):

		if graph.indegree[v] == 0 and not discovered[v]:

		
			for u in graph.adjList[v]:
				graph.indegree[u] = graph.indegree[u] - 1

			path.append(v)
			discovered[v] = True

		
			findAllTopologicalOrders(graph, path, discovered, V)

			for u in graph.adjList[v]:
				graph.indegree[u] = graph.indegree[u] + 1

			path.pop()
			discovered[v] = False

	if len(path) == V:
		print(path)

def printAllTopologicalOrders(graph):

	V = len(graph.adjList)

	discovered = [False] * V

	path = []

	findAllTopologicalOrders(graph, path, discovered, V)


if __name__ == '__main__':


	edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

	print("All Topological sorts")

	
	N = 6

	
	graph = Graph(edges, V)

	printAllTopologicalOrders(graph)

