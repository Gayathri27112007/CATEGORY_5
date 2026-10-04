def ao_star(graph, heuristic, start):
    solved = {}
    solution = {}

    def solve(node):
        if node not in graph:
            return heuristic[node]

        if node in solved:
            return heuristic[node]

        best_cost = float('inf')
        best_option = None

        for option in graph[node]:
            # OR choice
            if isinstance(option, list):
                cost = 0

                # AND: all nodes must be solved
                for child in option:
                    cost += solve(child)

                if cost < best_cost:
                    best_cost = cost
                    best_option = option

            else:
                cost = solve(option)

                if cost < best_cost:
                    best_cost = cost
                    best_option = option

        heuristic[node] = best_cost
        solution[node] = best_option
        solved[node] = True

        return best_cost

    cost = solve(start)

    return cost, solution


# AO* Graph
graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E'], ['F']],
    'C': ['G'],
    'D': ['H', 'I']
}

# Initial heuristic values
heuristic = {
    'A': 10,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 5,
    'G': 1,
    'H': 2,
    'I': 2
}

cost, solution = ao_star(graph, heuristic, 'A')

print("AO* Search")
print("Minimum Cost:", cost)

print("\nSolution Graph:")

for node, choice in solution.items():
    print(node, "->", choice)




*OUTPUT*
AO* Search
Minimum Cost: 3

Solution Graph:
B -> ['E']
C -> G
D -> ['H', 'I']
A -> ['B', 'C']
