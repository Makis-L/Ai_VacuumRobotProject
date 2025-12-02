from src.state import create_initial_state, is_goal
from src.findchildren import findchildren

def bfs(initial_state):
    state = initial_state # Χρησιμοποιούμε το όρισμα, όχι δημιουργία νέου

    frontier = [state]
    closed = set()

    expanded = 0
    generated = 1
    max_frontier = 1

    while frontier:
        current = frontier.pop(0)

        if current in closed:
            continue
        
        closed.add(current)
        
        if is_goal(current):
            # Αποθηκεύουμε τα στατιστικά πάνω στο αντικείμενο state για την εκτύπωση
            current.expanded = expanded
            current.generated = generated
            current.max_frontier = max_frontier
            return current

        expanded += 1

        # Εδώ είναι η αλλαγή: unpack το tuple (action, child, cost)
        children = findchildren(current)
        
        for _, child, _ in children:
            if child not in closed and child not in frontier:
                frontier.append(child)
                generated += 1
            
        if len(frontier) > max_frontier:
            max_frontier = len(frontier)

    return None