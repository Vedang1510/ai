import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (x, y)
        self.parent = parent
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic estimate from current node to goal
        self.f = g + h  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f  # Compare based on f value

def a_star(start, goal, grid):
    open_set = []
    closed_set = set()

    # Create start and goal nodes
    start_node = Node(start, None, 0, heuristic(start, goal))
    goal_node = Node(goal, None, 0, 0)

    # Push the start node into the open set
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        # If the goal is reached, reconstruct the path
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_set.add(current_node.position)

        # Check neighbors
        for neighbor in get_neighbors(current_node.position, grid):
            if neighbor in closed_set:
                continue

            g_cost = current_node.g + 1  # Assuming cost to move to any neighbor is 1
            h_cost = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, current_node, g_cost, h_cost)

            # Check if the neighbor is already in open set
            if not any(open_node.position == neighbor and open_node.f <= neighbor_node.f for open_node in open_set):
                heapq.heappush(open_set, neighbor_node)

    return None  # No path found

def heuristic(a, b):
    # Using Manhattan distance as heuristic (works for grid-based problems)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(position, grid):
    neighbors = []
    x, y = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4 possible directions (up, down, left, right)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:  # 0 means walkable
            neighbors.append((nx, ny))
    
    return neighbors

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)  # Starting position
    goal = (4, 4)   # Goal position

    path = a_star(start, goal, grid)
    
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
