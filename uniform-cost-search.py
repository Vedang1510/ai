import heapq

def ucs(start, goal, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    priority_queue = [(0, start, [start])]  # (cost, position, path)
    visited = set()

    while priority_queue:
        cost, current_position, path = heapq.heappop(priority_queue)
        
        if current_position == goal:
            return path

        if current_position in visited:
            continue
        visited.add(current_position)

        for direction in directions:
            neighbor = (current_position[0] + direction[0], current_position[1] + direction[1])
            if is_valid(neighbor, grid):
                new_cost = cost + 1  # Assuming uniform cost of 1 for each move
                heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))
    
    return None

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
path = ucs(start, goal, grid)
print("UCS Path:", path)
