from collections import deque

def bfs(start, goal, grid):
    # Directions for movement: up, right, down, left
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Create a queue for BFS
    queue = deque([(start, [start])])  # Store tuples of (current_position, path_to_reach_here)
    visited = set()  # Set to track visited nodes
    visited.add(start)

    while queue:
        current_position, path = queue.popleft()

        # If we have reached the goal
        if current_position == goal:
            return path

        # Explore neighbors
        for direction in directions:
            neighbor = (current_position[0] + direction[0], current_position[1] + direction[1])

            # Check if neighbor is valid (within bounds and not blocked)
            if is_valid(neighbor, grid) and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # If no path found

def is_valid(position, grid):
    x, y = position
    # Check if within grid bounds and not blocked
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

path = bfs(start, goal, grid)
print("Path found:", path)
