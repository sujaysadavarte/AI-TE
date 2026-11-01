"""A3: Adversarial Search with Alpha-Beta Pruning."""
nodes_visited = 0
 
 
def alpha_beta(depth, node_index, maximizing, values, alpha, beta, max_depth):
    global nodes_visited
    if depth == max_depth:
        nodes_visited += 1
        return values[node_index]
    if maximizing:
        best = float("-inf")
        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, False,
                               values, alpha, beta, max_depth)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                print("Pruning at MAX node")
                break
        return best
    else:
        best = float("inf")
        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, True,
                               values, alpha, beta, max_depth)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                print("Pruning at MIN node")
                break
        return best
 
 
def minimax(depth, node_index, maximizing, values, max_depth):
    if depth == max_depth:
        return values[node_index]
    results = [minimax(depth + 1, node_index * 2 + i, not maximizing,
                       values, max_depth) for i in range(2)]
    return max(results) if maximizing else min(results)
 
 
if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    max_depth = 3
    optimal_value = alpha_beta(0, 0, True, values,
                               float("-inf"), float("inf"), max_depth)
    print("Optimal value:", optimal_value)
    print("Leaf nodes evaluated with pruning:", nodes_visited, "of", len(values))
    print("Minimax result (for comparison):",
          minimax(0, 0, True, values, max_depth))

