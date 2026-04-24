# Graph definition
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

# BFS Algorithm
def bfs(graph, start, goal):
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbors = graph.get(node, [])  # safer access

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path

            visited.append(node)

    return "No Path Found"


# DFS Algorithm
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []

    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path)
            if new_path:
                return new_path

    return None


# User Input (converted to uppercase to match graph keys)
start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

# Input validation
if start not in graph:
    print(f"Start node '{start}' not found in graph")
elif goal not in graph:
    print(f"Goal node '{goal}' not found in graph")
else:
    # Run Algorithms
    bfs_path = bfs(graph, start, goal)
    dfs_path = dfs(graph, start, goal)

    # Output
    print("\nBFS Path:", bfs_path)
    print("DFS Path:", dfs_path)