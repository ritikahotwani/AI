class Node:
	def __init__(self, value):
		self.value = value
		self.children = []

def dfs(start_node, goal_node):
	visited = set()
	stack = [(start_node, [start_node.value], 0)]
	while stack:
		(node, path, cost) = stack.pop()
		if node.value == goal_node:
			return (path, cost)
		visited.add(node)
		for child in node.children:
			if child not in visited:
				stack.append((child, path + [child.value], cost + 1))
	return None

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

optimal_path, path_cost = dfs(a, 'H')
print('Optimal Path:', optimal_path)
print('Path Cost:', path_cost)