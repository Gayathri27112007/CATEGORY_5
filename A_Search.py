# A* Search Algorithm

# Graph with path costs
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 3},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

# Heuristic values
h = {
    'A': 6,
    'B': 5,
    'C': 5,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}


def a_star(start, goal):

    open_list = [start]
    cost = {start: 0}
    parent = {start: None}

    while open_list:

        # Find node with lowest f(n)
        current = open_list[0]

        for node in open_list:
            f_current = cost[current] + h[current]
            f_node = cost[node] + h[node]

            if f_node < f_current:
                current = node

        # Goal reached
        if current == goal:
            break

        open_list.remove(current)

        # Check neighbouring nodes
        for neighbor in graph[current]:

            new_cost = cost[current] + graph[current][neighbor]

            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost
                parent[neighbor] = current

                if neighbor not in open_list:
                    open_list.append(neighbor)

    # Create path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, cost[goal]


# Run A*
path, total_cost = a_star('A', 'G')

print("A* SEARCH")
print("-------------------------")
print("Path:", " -> ".join(path))
print("Total Cost:", total_cost)

*OUTPUT*

A* SEARCH
-------------------------
Path: A -> B -> D -> G
Total Cost: 6


EXPLANATION:

A → B → D → G is the shortest path.

Cost = 1 + 2 + 3 = 6
