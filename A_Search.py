import heapq

def heuristic(state, goal):
    # Manhattan distance
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(goal_pos, 3)
            distance += abs(r1 - r2) + abs(c1 - c2)
    return distance


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = list(state)
            new_zero = nr * 3 + nc

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (0, start))

    cost = {start: 0}
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for neighbor in get_neighbors(current):
            new_cost = cost[current] + 1

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost

                f = new_cost + heuristic(neighbor, goal)

                heapq.heappush(pq, (f, neighbor))
                parent[neighbor] = current

    return None


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

path = a_star(start, goal)

print("A* Search Solution:\n")

for step, state in enumerate(path):
    print("Step", step)
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()



*OUTPUT*
A* Search Solution:

Step 0
(1, 2, 3)
(4, 0, 6)
(7, 5, 8)

Step 1
(1, 2, 3)
(4, 5, 6)
(7, 0, 8)

Step 2
(1, 2, 3)
(4, 5, 6)
(7, 8, 0)

