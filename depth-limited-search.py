def dls(start, goal, grid, depth_limit):
    def explore(node, path, depth):
        if node == goal:
            return path
        if depth == depth_limit:
            return None

        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (node[0] + direction[0], node[1] + direction[1])
            if is_valid(neighbor, grid) and neighbor not in path:
                new_path = path + [neighbor]
                result = explore(neighbor, new_path, depth + 1)
                if result:
                    return result
        return None
    
    return explore(start, [start], 0)

def is_valid(position, grid):
    x, y = position
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1:
        return True
    return False

# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
depth_limit = 3
path = dls(start, goal, grid, depth_limit)
print("DLS Path:", path)
