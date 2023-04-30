class Node:
	def __init__(self, value):
		self.value = value
		self.children = []

def bfs(start_node, goal_node):
	visited = set()
	queue = [(start_node, [start_node.value], 0)]  # add path cost to the queue
	while queue:
		(node, path, cost) = queue.pop(0)
		if node.value == goal_node:
			return (path, cost)  # return both path and cost
		visited.add(node)
		for child in node.children:
			if child not in visited:
				queue.append((child, path + [child.value], cost + 1))  # update path cost
	return (None, None)

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')

a.children = [b, c]
b.children = [d, e]
c.children = [f, g]
g.children = [h]

optimal_path, path_cost = bfs(a, 'H')  # unpack both path and cost
if optimal_path is not None:
    print(f'Optimal path: {optimal_path}')
    print(f'Path cost: {path_cost}')
else:
    print('Path not found')