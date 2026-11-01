"""A2: A* Search for the 8-Puzzle using Manhattan Distance."""
import heapq
 
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
 
 
def manhattan(state):
    distance = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            goal_index = GOAL.index(tile)
            cr, cc = divmod(i, 3)
            gr, gc = divmod(goal_index, 3)
            distance += abs(cr - gr) + abs(cc - gc)
    return distance
 
 
def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nb = nr * 3 + nc
            new_state = list(state)
            new_state[blank], new_state[nb] = new_state[nb], new_state[blank]
            neighbors.append(tuple(new_state))
    return neighbors
 
 
def is_solvable(state):
    tiles = [t for t in state if t != 0]
    inversions = sum(1 for i in range(len(tiles))
                     for j in range(i + 1, len(tiles)) if tiles[i] > tiles[j])
    return inversions % 2 == 0
 
 
def a_star(start):
    counter = 0  # tie-breaker so heap never compares paths
    open_list = [(manhattan(start), 0, counter, start, [start])]
    best_g = {start: 0}
    visited = set()
    while open_list:
        f, g, _, current, path = heapq.heappop(open_list)
        if current == GOAL:
            return path
        if current in visited:
            continue
        visited.add(current)
        for nb in get_neighbors(current):
            new_g = g + 1
            if nb not in visited and new_g < best_g.get(nb, float("inf")):
                best_g[nb] = new_g
                counter += 1
                heapq.heappush(open_list,
                               (new_g + manhattan(nb), new_g, counter,
                                nb, path + [nb]))
    return None
 
 
def show(start):
    print("Initial state:", start, "| h =", manhattan(start))
    if not is_solvable(start):
        print("This puzzle is not solvable.\n")
        return
    solution = a_star(start)
    print("Solution found in", len(solution) - 1, "moves:")
    for state in solution:
        print()
        for i in range(0, 9, 3):
            print(state[i:i + 3])
    print()
 
 
if __name__ == "__main__":
    show((1, 2, 3,
          4, 0, 6,
          7, 5, 8))
    show((1, 2, 3,
          0, 4, 6,
          7, 5, 8))
    show((8, 1, 3,
          4, 0, 2,
          7, 6, 5))
