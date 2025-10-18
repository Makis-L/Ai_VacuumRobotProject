# Αρχείο Τελεστών Μετάβασης.
# Το ρομπότ μπορεί να κάνει 4 κινήσεις:
# 1. Να κινηθεί αριστερά
# 2. Να κινηθεί δεξία
# 3. Να μαζέψει σκουπίδι (1 την φορά)
# 4. Να πετάξει τα σκουπίδια στην βάση του

from src.state import State

def move_left(state):
    if state.position > 0:
        new_position = state.position - 1
        
        new_state = State(
            position = new_position,
            trash = state.tras.copy(),
            load = state.load,
            base = state.base,
            parent = state,
            action = "move_left",
            depth = state.depth + 1
        )
        return new_state
    return None

def move_right(state):
    if state.position < 7:
        new_position = state.position + 1
        
        new_state = State(
            position = new_position,
            trash = state.trash.copy(),
            load = state.load,
            base = state.base,
            parent = state,
            action = "move_right",
            depth = state.depth + 1
        )
        return new_state
    return None

def clean(state):
    pos = state.position
    
    if state.trash[pos] > 0 and state.load < 3:
        new_trash = state.trash.copy()
        new_trash[pos] -= 1
        
        new_state = State(
            position = pos,
            trash = new_trash,
            load = state.load + 1,
            base = state.base,
            parent = state,
            action = "clean",
            depth = state.depth + 1
        )
        return new_state
    return None        

def dump(state):
    if state.position == state.base and state.load > 0:
        new_load = 0
        
        new_state = State(
            position = state.position,
            trash = state.trash.copy(),
            load = new_load,
            base = state.base,
            parent = state,
            action = "dump",
            depth = state.depth + 1
        )
        return new_state
    return None

