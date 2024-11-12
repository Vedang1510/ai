import heapq

# Define the grid and goal position
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)  # Starting position (row, col)
goal = (4, 4)   # Goal position (row, col)

# Heuristic function: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Get neighbors in 4 possible directions (up, down, left, right)
def get_neighbors(pos):
    row, col = pos
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    valid_neighbors = [(r, c) for r, c in neighbors if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0]
    return valid_neighbors

# Best-First Search algorithm
def best_first_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start))  # (priority, node)
    visited = set()
    visited.add(start)
    came_from = {start: None}  # To reconstruct the path
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        # Check if we reached the goal
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()  # Reverse the path from goal to start
            return path
        
        # Explore neighbors
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))
    
    return None  # No path found

# Run Best-First Search
path = best_first_search(start, goal)

# Display the result
if path:
    print("Path found:")
    for step in path:
        print(step)
else:
    print("No path found.")
