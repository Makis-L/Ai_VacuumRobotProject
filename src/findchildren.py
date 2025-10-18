from src.state import State
from src.operators import move_left, move_right, clean, dump

def findchildren(state):
    
    children = []
    ops = [move_left, move_right, clean, dump]
    
    for x in ops:
        new_state = x(state)
        
        if new_state is not None:
            children.append(new_state)
    
    return children