"""B1: BFS shortest path for a robot in a grid with obstacles."""
from collections import deque
 
 
def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
    if goal not in parent:
        return None
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path
 
 
def draw(grid, path, start, goal):
    on_path = set(path or [])
    for r, row in enumerate(grid):
        line = []
        for c, cell in enumerate(row):
            if (r, c) == start:
                line.append("S")
            elif (r, c) == goal:
                line.append("G")
            elif cell == 1:
                line.append("#")
            elif (r, c) in on_path:
                line.append("*")
            else:
                line.append(".")
        print(" ".join(line))
 
 
if __name__ == "__main__":
    # 0 = free cell, 1 = obstacle
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    start, goal = (0, 0), (4, 4)
    path = bfs(grid, start, goal)
    if path:
        print("Shortest Path:")
        print(path)
        print("\nNumber of moves:", len(path) - 1)
        print()
        draw(grid, path, start, goal)
    else:
        print("No path exists.")
