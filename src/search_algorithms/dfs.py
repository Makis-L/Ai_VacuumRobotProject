from src.state import create_initial_state, is_goal
from src.findchildren import findchildren

def dfs(initial_state):
    state = initial_state 

    frontier = [state]
    closed = set()

    expanded = 0
    generated = 1
    max_frontier = 1

    while frontier:
        current = frontier.pop()

        if current in closed:
            continue
        
        closed.add(current)

        if is_goal(current):
            current.expanded = expanded
            current.generated = generated
            current.max_frontier = max_frontier
            return current

        expanded += 1

        children = findchildren(current)
        
        # Unpack το tuple
        for _, child, _ in children:
            if child not in closed: # Στο DFS συνήθως ελέγχουμε το closed
                frontier.append(child)
                generated += 1

        if len(frontier) > max_frontier:
            max_frontier = len(frontier)

    return None