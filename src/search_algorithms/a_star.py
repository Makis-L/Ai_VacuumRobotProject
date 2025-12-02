# Υλοποίηση του αλγορίθμου A* (A-Star) Search.
# Χρησιμοποιεί ευριστική συνάρτηση h(n) για να κατευθύνει την αναζήτηση.
# f(n) = g(n) + h(n) 

import heapq
from src.printing import reconstruct_path
from src.state import State

def state_to_key(state):
    
    # Μετατρέπει μια κατάσταση σε μοναδικό κλειδί (tuple).
    # Χρησιμοποιείται για την αποθήκευση στο λεξικό g_cost και στο closed set.
    # Περιλαμβάνει: (Θέση Ρομπότ, Διάταξη Σκουπιδιών, Φορτίο).
    return (state.position, tuple(state.trash), state.load)

def astar_search(initial_state, is_goal, findchildren, heuristic_fn):
    
    # Το Open Set υλοποιείται ως Ουρά Προτεραιότητας (Binary Heap).
    # Αποθηκεύει tuples μορφής: (f_score, tie_breaker, state).
    # Το tie_breaker είναι ένας μετρητής που αυξάνεται συνεχώς. Εξασφαλίζει ότι αν δύο
    # καταστάσεις έχουν το ίδιο f_score, θα επιλεγεί αυτή που μπήκε πρώτη (FIFO)
    # και δεν θα χρειαστεί να συγκριθούν τα αντικείμενα State μεταξύ τους.
    tie = 0
    open_heap = []
    
    # Λεξικό που κρατάει το ελάχιστο κόστος μετάβασης (g-cost) από την αρχή
    # μέχρι την τρέχουσα κατάσταση. Αν βρούμε νέο μονοπάτι για μια κατάσταση
    # με μικρότερο g, ενημερώνουμε αυτό το λεξικό.
    g_cost = {}
    
    # Αρχικοποίηση για την πρώτη κατάσταση
    start_key = state_to_key(initial_state)
    g_cost[start_key] = 0
    
    # Υπολογισμός ευριστικής για την αρχή
    h_val = heuristic_fn(initial_state)
    
    # Προσθήκη στο σωρό (f = g + h = 0 + h)
    heapq.heappush(open_heap, (h_val, tie, initial_state))
    tie += 1
    
    # Σύνολο κλειστών κόμβων (για να μην επεκτείνουμε ξανά τα ίδια)
    closed = set()
    
    # Στατιστικά εκτέλεσης
    expanded = 0
    generated = 1
    max_open_size = 1
    
    while open_heap:
        # Ενημέρωση μέγιστου μεγέθους μετώπου (μνήμη)
        if len(open_heap) > max_open_size:
            max_open_size = len(open_heap)

        # Εξαγωγή της κατάστασης με το μικρότερο f_score από το σωρό
        f, _, current = heapq.heappop(open_heap)
        current_key = state_to_key(current)
        
        # Αν έχουμε ήδη κλείσει αυτή την κατάσταση (βρήκαμε ήδη το βέλτιστο δρόμο γι' αυτήν), προχωράμε
        if current_key in closed:
            continue
            
        # Έλεγχος αν φτάσαμε στο στόχο
        if is_goal(current):
            stats = {
                "expanded": expanded,
                "generated": generated,
                "max_frontier": max_open_size,
                "solution_cost": g_cost[current_key]
            }
            # Επιστροφή του μονοπατιού (λίστα καταστάσεων) και των στατιστικών
            return reconstruct_path(current), stats
        
        # Προσθήκη στα κλειστά
        closed.add(current_key)
        expanded += 1
        
        # Παραγωγή παιδιών (επόμενες πιθανές καταστάσεις)
        children = findchildren(current)
        
        for action, child, cost in children:
            child_key = state_to_key(child)
            
            # Υπολογισμός του νέου g-cost για το παιδί
            tentative_g = g_cost[current_key] + cost
            
            # Αν συναντάμε αυτή την κατάσταση για πρώτη φορά 
            # Ή αν βρήκαμε ένα νέο μονοπάτι με μικρότερο κόστος (tentative_g < g_cost)
            if child_key not in g_cost or tentative_g < g_cost[child_key]:
                
                # Ενημέρωση του κόστους
                g_cost[child_key] = tentative_g
                
                # Το parent και το action έχουν ήδη τεθεί από την findchildren/operators,
                # οπότε το path reconstruct θα δουλέψει σωστά.
                
                # Υπολογισμός f_score = g + h
                f_child = tentative_g + heuristic_fn(child)
                
                # Προσθήκη στο Open Heap
                heapq.heappush(open_heap, (f_child, tie, child))
                tie += 1
                generated += 1
                
    # Αν αδειάσει η λίστα και δεν βρεθεί λύση
    return None, None