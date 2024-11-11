from collections import deque

def bidirectional_search(start, goal, grid):
    def bfs_front(start, visited_from_start, paths_from_start):
        queue = deque([start])
        while queue:
            current_position = queue.popleft()
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (current_position[0] + direction[0], current_position[1] + direction[1])
                if is_valid(neighbor, grid) and neighbor not in visited_from_start:
                    visited_from_start.add(neighbor)
                    paths_from_start[neighbor] = paths_from_start[current_position] + [neighbor]
                    queue.append(neighbor)
                    if neighbor in visited_from_goal:
                        return paths_from_start[neighbor], paths_from_goal[neighbor]
        return None

    def bfs_back(goal, visited_from_goal, paths_from_goal):
        queue = deque([goal])
        while queue:
            current_position = queue.popleft()
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (current_position[0] + direction[0], current_position[1] + direction[1])
                if is_valid(neighbor, grid) and neighbor not in visited_from_goal:
                    visited_from_goal.add(neighbor)
                    paths_from_goal[neighbor] = paths_from_goal[current_position] + [neighbor]
                    queue.append(neighbor)
                    if neighbor in visited_from_start:
                        return paths_from_start[neighbor] + paths_from_goal[neighbor][::-1]
        return None

    visited_from_start = set([start])
    visited_from_goal = set([goal])
    paths_from_start = {start: [start]}
    paths_from_goal = {goal: [goal]}
    
    # Search from start side
    forward_path = bfs_front(start, visited_from_start, paths_from_start)
    if forward_path:
        return forward_path
    
    # Search from goal side
    backward_path = bfs_back(goal, visited_from_goal, paths_from_goal)
    if backward_path:
        return backward_path
    
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
path = bidirectional_search(start, goal, grid)
print("Bidirectional Search Path:", path)
