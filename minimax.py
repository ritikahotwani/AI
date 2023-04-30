nodes = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': None,
    'D': ['G', 'H'],
    'E': None,
    'F': None,
    'G': ['I'],
    'H': None,
    'I': None,
}

costs = {
    'A': None,
    'B': None,
    'C': 1,
    'D': None,
    'E': -1,
    'F': -1,
    'G': None,
    'H': -1,
    'I': 1,
}

minmax = {
    'A': 'max',
    'B': 'min',
    'C': 'min',
    'D': 'min',
    'E': 'max',
    'F': 'max',
    'G': 'max',
    'H': 'max',
    'I': 'min',
}


def get_child_cost(x):
    ans = []
    if nodes[x] == None:
        print(f'{x} -> {costs[x]}')
        return costs[x]
    else:
        for i in nodes[x]:
            ans.append(get_child_cost(i))
        if minmax[x] == 'min':
            ans = min(ans)
            costs[x] = ans
        else:
            ans = max(ans)
            costs[x] = ans
        print(f'{x} -> {costs[x]}')
        return ans
temp = get_child_cost(list(nodes.keys())[0])