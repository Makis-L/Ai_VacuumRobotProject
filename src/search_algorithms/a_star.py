import heapq
from src.printing import reconstruct_path
from src.state import State

def state_to_key(state):
    # Χρησιμοποιούμε τα ίδια στοιχεία με το __hash__ του State για μοναδικότητα
    return (state.position, tuple(state.trash), state.load)

def astar_search(initial_state, is_goal, findchildren, heuristic_fn):
    
    # Το heap αποθηκεύει tuples: (f_score, tie_breaker, state)
    # tie_breaker: απλός μετρητής για να αποφεύγουμε συγκρίσεις μεταξύ State αντικειμένων σε ισοπαλίες f
    tie = 0
    open_heap = []
    
    # Λεξικό για να κρατάμε το ελάχιστο g-cost για κάθε κατάσταση που συναντάμε
    g_cost = {}
    
    start_key = state_to_key(initial_state)
    g_cost[start_key] = 0
    
    h_val = heuristic_fn(initial_state)
    heapq.heappush(open_heap, (h_val, tie, initial_state))
    tie += 1
    
    closed = set()
    
    expanded = 0
    generated = 1
    max_open_size = 1
    
    while open_heap:
        f, _, current = heapq.heappop(open_heap)
        current_key = state_to_key(current)
        
        if current_key in closed:
            continue
            
        # Έλεγχος στόχου
        if is_goal(current):
            stats = {
                "expanded": expanded,
                "generated": generated,
                "max_frontier": max_open_size, # Το ονομάζουμε max_frontier για συμβατότητα
                "solution_cost": g_cost[current_key]
            }
            # Επιστρέφουμε τη διαδρομή και τα στατιστικά
            return reconstruct_path(current), stats
        
        closed.add(current_key)
        expanded += 1
        
        # Επέκταση παιδιών
        children = findchildren(current)
        
        for action, child, cost in children:
            child_key = state_to_key(child)
            tentative_g = g_cost[current_key] + cost
            
            # Αν το βρήκαμε πρώτη φορά ή βρήκαμε καλύτερο μονοπάτι
            if child_key not in g_cost or tentative_g < g_cost[child_key]:
                
                g_cost[child_key] = tentative_g
                
                # Οι γονείς έχουν ήδη τεθεί από τον operator, αλλά ενημερώνουμε τα g/h
                # Σημείωση: Το αντικείμενο child είναι νέο, οπότε το parent του είναι το current
                
                f_child = tentative_g + heuristic_fn(child)
                
                heapq.heappush(open_heap, (f_child, tie, child))
                tie += 1
                generated += 1
                
        if len(open_heap) > max_open_size:
            max_open_size = len(open_heap)
            
    return None, None