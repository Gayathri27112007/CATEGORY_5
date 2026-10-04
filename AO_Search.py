# AO* Search Algorithm

# Each node contains different choices.
# Each choice can contain one or more nodes.
#
# One choice = OR
# Nodes inside one choice = AND

graph = {
    'A': [
        [('B', 1)],
        [('C', 2)]
    ],

    'B': [
        [('D', 2), ('E', 2)]
    ],

    'C': [
        [('F', 3)],
        [('G', 5)]
    ],

    'D': [],
    'E': [],
    'F': [],
    'G': []
}


# Heuristic values
h = {
    'A': 0,
    'B': 1,
    'C': 1,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0
}


def ao_star(node):

    # If node is a goal/leaf node
    if len(graph[node]) == 0:
        return h[node]

    best_cost = float('inf')
    best_choice = None

    # OR: choose the cheapest option
    for choice in graph[node]:

        total_cost = 0

        # AND: all nodes in this choice must be solved
        for child, edge_cost in choice:

            child_cost = ao_star(child)

            total_cost = total_cost + edge_cost + child_cost

        # Select minimum cost
        if total_cost < best_cost:
            best_cost = total_cost
            best_choice = choice

    print(node, "->", [child for child, cost in best_choice],
          "Cost =", best_cost)

    return best_cost


print("AO* SEARCH")
print("-------------------------")

minimum_cost = ao_star('A')

print("-------------------------")
print("Minimum Cost:", minimum_cost)



*OUTPUT*
AO* SEARCH
-------------------------
B -> ['D', 'E'] Cost = 4
C -> ['F'] Cost = 3
A -> ['B'] Cost = 5
-------------------------
Minimum Cost: 5
