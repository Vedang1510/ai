from collections import deque

# Define the problem state
class State:
    def __init__(self, monkey_pos, box_pos, has_banana):
        self.monkey_pos = monkey_pos  # Monkey's position (True = on box, False = off box)
        self.box_pos = box_pos        # Box position (True = under the monkey, False = not)
        self.has_banana = has_banana  # Whether the monkey has the banana or not
    
    def __repr__(self):
        return f"Monkey Position: {self.monkey_pos}, Box Position: {self.box_pos}, Has Banana: {self.has_banana}"

# BFS to find the solution
def bfs(start_state, goal_state):
    queue = deque([start_state])  # Initialize the queue with the start state
    visited = set()               # Keep track of visited states
    visited.add((start_state.monkey_pos, start_state.box_pos))  # Add start state to visited
    
    while queue:
        current_state = queue.popleft()
        
        # If the monkey has the banana, we're done
        if current_state.has_banana:
            return True
        
        # List possible moves and add them to the queue if not visited
        possible_moves = generate_possible_moves(current_state)
        for move in possible_moves:
            if (move.monkey_pos, move.box_pos) not in visited:
                visited.add((move.monkey_pos, move.box_pos))
                queue.append(move)
    
    return False  # No solution found

# Generate all possible moves from the current state
def generate_possible_moves(state):
    moves = []
    
    # Case 1: Monkey moves left or right
    if state.monkey_pos:  # If the monkey is on the box
        moves.append(State(False, state.box_pos, state.has_banana))  # Move the monkey off the box
    else:
        moves.append(State(True, state.box_pos, state.has_banana))  # Move the monkey on the box
    
    # Case 2: Monkey pushes the box if it's not on it
    if not state.monkey_pos and state.box_pos:
        moves.append(State(state.monkey_pos, False, state.has_banana))  # Push the box away
    
    # Case 3: Monkey climbs the box if it's under the monkey
    if state.box_pos and not state.has_banana:
        moves.append(State(True, state.box_pos, True))  # Monkey climbs on the box and grabs the banana
    
    return moves

# Initialize the start and goal states
start_state = State(False, True, False)  # Monkey is off the box, box is under the monkey, no banana
goal_state = State(True, True, True)    # Monkey on the box, box is under it, has the banana

# Run BFS to find the solution
solution_found = bfs(start_state, goal_state)

# Output the result
if solution_found:
    print("The monkey can grab the banana!")
else:
    print("The monkey cannot grab the banana.")
