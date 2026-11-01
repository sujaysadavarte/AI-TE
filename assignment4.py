"""A4: Tower of Hanoi using State Space Search (BFS)."""
from collections import deque
 
PEG_NAMES = ["A", "B", "C"]
 
 
def get_successors(state):
    successors = []
    pegs = [list(peg) for peg in state]
    for source in range(3):
        if not pegs[source]:
            continue
        disk = pegs[source][-1]
        for destination in range(3):
            if source == destination:
                continue
            if not pegs[destination] or pegs[destination][-1] > disk:
                new_pegs = [peg[:] for peg in pegs]
                new_pegs[source].pop()
                new_pegs[destination].append(disk)
                new_state = tuple(tuple(p) for p in new_pegs)
                successors.append((new_state, source, destination, disk))
    return successors
 
 
def state_space_search(n):
    start = (tuple(range(n, 0, -1)), (), ())
    goal = ((), (), tuple(range(n, 0, -1)))
    queue = deque([(start, [])])
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for new_state, s, d, disk in get_successors(state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state,
                              path + [(disk, PEG_NAMES[s], PEG_NAMES[d], new_state)]))
    return None
 
 
if __name__ == "__main__":
    n = 3
    solution = state_space_search(n)
    if solution:
        print("Solution found in", len(solution), "moves:")
        for step, (disk, src, dst, state) in enumerate(solution, 1):
            print(f"Step {step}: Move Disk {disk} from {src} to {dst}")
            print("State:", state)
        print("Minimum moves formula 2^n - 1 =", 2 ** n - 1)
    else:
        print("No solution found.")
