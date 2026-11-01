#Code (B2_dfs_water_jug.py)
"""B2: DFS for the Water Jug Problem (4 L and 3 L jugs, goal = 2 L)."""
CAP_A, CAP_B, TARGET = 4, 3, 2
 
 
def get_successors(state):
    a, b = state
    successors = [
        (CAP_A, b),  # Fill A
        (a, CAP_B),  # Fill B
        (0, b),      # Empty A
        (a, 0),      # Empty B
    ]
    t = min(a, CAP_B - b)  # Pour A -> B
    successors.append((a - t, b + t))
    t = min(b, CAP_A - a)  # Pour B -> A
    successors.append((a + t, b - t))
    return successors
 
 
def dfs(state, visited, path):
    path.append(state)
    if state[0] == TARGET or state[1] == TARGET:
        return True
    visited.add(state)
    for nxt in get_successors(state):
        if nxt not in visited:
            if dfs(nxt, visited, path):
                return True
    path.pop()  # backtrack
    return False
 
 
if __name__ == "__main__":
    path = []
    if dfs((0, 0), set(), path):
        print("Solution Path (DFS):")
        for step, state in enumerate(path):
            print(f"Step {step}: {state}")
        print("\nFinal state:", path[-1],
              f"-> Jug A = {path[-1][0]} L, Jug B = {path[-1][1]} L")
    else:
        print("No solution found.")
