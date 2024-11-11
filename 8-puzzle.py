from collections import deque

# Define the goal state
goal_state = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

# Function to print the board
def print_board(state):
    for row in state:
        print(row)
    print()

# Function to get the possible moves from the current state
def get_possible_moves(state):
    moves = []
    # Convert tuple to list to find index of empty space (0)
    state_list = [list(row) for row in state]  # Convert each row to a list
    empty_pos = next((r * 3 + c for r in range(3) for c in range(3) if state_list[r][c] == 0), None)
    row, col = divmod(empty_pos, 3)
    
    # Directions for possible moves (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for direction in directions:
        new_row, new_col = row + direction[0], col + direction[1]
        
        # Check if the new position is within bounds
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            # Swap the empty space with the tile at the new position
            state_list[row][col], state_list[new_row][new_col] = state_list[new_row][new_col], state_list[row][col]
            # Convert the list back to a tuple
            new_state = tuple(tuple(row) for row in state_list)
            moves.append(new_state)
            # Swap back to restore the state
            state_list[row][col], state_list[new_row][new_col] = state_list[new_row][new_col], state_list[row][col]
    
    return moves

# Function to perform BFS to solve the 8-puzzle
def bfs(start_state):
    visited = set()  # To avoid revisiting the same state
    queue = deque([(start_state, [])])  # Queue to store states and the path to reach them
    visited.add(start_state)
    
    while queue:
        state, path = queue.popleft()
        
        # If the goal state is reached, return the path
        if state == goal_state:
            return path
        
        # Get possible moves from the current state
        for next_state in get_possible_moves(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    
    return None  # If no solution is found

# Start the game with an initial state
start_state = (
    (1, 2, 3),
    (4, 0, 5),
    (7, 8, 6)
)

# Print the initial board
print("Initial Board:")
print_board(start_state)

# Solve the 8-puzzle using BFS
solution_path = bfs(start_state)

if solution_path:
    print("Solution found!")
    for step, state in enumerate(solution_path, start=1):
        print(f"Step {step}:")
        print_board(state)
else:
    print("No solution found.")
