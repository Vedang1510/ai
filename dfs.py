def dfs(start, goal, grid):
    def explore(node, path):
        if node == goal:
            return path
        
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (node[0] + direction[0], node[1] + direction[1])
            if is_valid(neighbor, grid) and neighbor not in path:
                new_path = path + [neighbor]
                result = explore(neighbor, new_path)
                if result:
                    return result
        return None
    
    return explore(start, [start])

def is_valid(position, grid):
    x, y = position
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1:
        return True
    return False

# Example grid (0 is free space, 1 is blocked)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Example: Start at (0, 0), goal at (4, 4)
start = (0, 0)
goal = (4, 4)

path = dfs(start, goal, grid)
print("Path found:", path)