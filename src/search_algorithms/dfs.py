from src.state import State, create_initial_state, is_goal
from src.findchildren import findchildren

def dfs(initial_state, depth=None):
    
    initial_state = create_initial_state()
    
    frontier = [initial_state]
    closed = set()
    
    while frontier:
        
        current = frontier.pop() # Παίρνουμε το τελευταίο στοιχείο της λίστας
        
        if current in closed:
            continue
            
        if is_goal(current):
            print("It's over!")
            return current
        
        children = findchildren(current)
        frontier.append(children)
        
        closed.add(current)
        