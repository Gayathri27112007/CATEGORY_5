# Heuristic Search Techniques

## AI Course – II AIML

### Category 5 – Heuristic Search

This project implements two heuristic search techniques:

1. A* Search
2. AO* Search

The programs demonstrate how heuristic search techniques can be used to find an optimal solution.

---

# 1. A* Search

## Aim

To implement the **A* Search algorithm** for solving the **8-Puzzle problem**.

## What is A* Search?

A* is an informed search algorithm that uses both the actual cost and the estimated cost to find the best path.

It uses the formula:

**f(n) = g(n) + h(n)**

Where:

* **g(n)** = cost from the initial state to the current state
* **h(n)** = estimated cost from the current state to the goal
* **f(n)** = total estimated cost

The node with the lowest `f(n)` value is selected first.

## Heuristic Used

The program uses **Manhattan Distance** as the heuristic.

Manhattan Distance is calculated by finding how many rows and columns each tile is away from its correct position.

## 8-Puzzle

The puzzle contains:

* 8 numbered tiles
* 1 empty space represented by `0`
* A 3 × 3 board

Example:

```text
1 2 3
4 0 6
7 5 8
```

Goal state:

```text
1 2 3
4 5 6
7 8 0
```

## Working

1. Start with the initial puzzle state.
2. Find the position of the empty tile.
3. Generate possible neighboring states.
4. Calculate the heuristic value using Manhattan Distance.
5. Calculate:

```text
f(n) = g(n) + h(n)
```

6. Select the state with the lowest `f(n)`.
7. Continue until the goal state is reached.
8. Display all the steps from the initial state to the goal state.

## Example Output

```text
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
```

The final state is the goal state.

---

# 2. AO* Search

## Aim

To implement the **AO* Search algorithm** using an **AND-OR graph**.

## What is AO* Search?

AO* is a heuristic search algorithm used for solving problems represented as **AND-OR graphs**.

It finds the minimum-cost solution graph using heuristic values.

## AND-OR Graph

### OR Node

At an OR node, we can choose **one** of the available alternatives.

Example:

```text
       A
      / \
     B   D
```

We can choose either `B` or `D`.

### AND Node

At an AND node, **all required child nodes** must be solved.

Example:

```text
       A
      / \
     B   C
```

Both `B` and `C` are required.

## Working

1. Start from the root node.
2. Check the available alternatives.
3. Calculate the cost of each alternative.
4. For an OR choice, select the minimum-cost alternative.
5. For an AND choice, add the costs of all required child nodes.
6. Update the heuristic value.
7. Continue until the minimum-cost solution graph is obtained.

## Example Graph

The program uses an AND-OR graph such as:

```text
              A
            /   \
          AND    OR
         /  \     |
        B    C    D
       / \   |
      E   F  G
```

The algorithm evaluates the alternatives and selects the solution with minimum cost.

## Output

The program displays:

```text
AO* Search
Minimum Cost: 3

Solution Graph:
B -> ['E']
C -> G
D -> ['H', 'I']
A -> ['B', 'C']
```

The selected nodes represent the minimum-cost solution graph.

---

# Difference Between A* and AO*

| A* Search                  | AO* Search                                  |
| -------------------------- | ------------------------------------------- |
| Used for graph/path search | Used for AND-OR graphs                      |
| Finds an optimal path      | Finds an optimal solution graph             |
| Uses `f(n) = g(n) + h(n)`  | Uses heuristic cost for AND-OR alternatives |
| Usually selects one path   | AND branches may require multiple solutions |
| Example: 8-Puzzle          | Example: Problem decomposition              |

---

# Conclusion

A* and AO* are **heuristic search techniques**.

**A*** finds an optimal path by combining the actual cost and heuristic cost.

**AO*** finds an optimal solution graph in an AND-OR problem by evaluating different alternatives and required sub-problems.

These algorithms are useful in **Artificial Intelligence** for solving complex search and problem-solving tasks.
