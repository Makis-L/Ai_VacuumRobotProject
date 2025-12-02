# Αρχείο που περιέχει βοηθητικές συναρτήσεις για την εμφάνιση των αποτελεσμάτων
# και την ανακατασκευή του μονοπατιού της λύσης.

def reconstruct_path(goal_state):
    
    # Ανακατασκευάζει το μονοπάτι από την αρχική κατάσταση μέχρι τον στόχο.
    # Ξεκινάει από την κατάσταση στόχο (goal_state) και ακολουθεί τους δείκτες 'parent'
    # προς τα πίσω μέχρι να φτάσει στην αρχή (όπου parent is None).
    
    path = []
    state = goal_state
    
    # Backtracking: Πηγαίνουμε προς τα πίσω
    while state is not None:
        path.append(state)
        state = state.parent
    
    # Η λίστα path τώρα είναι ανάποδα (Goal -> Start).
    # Την αντιστρέφουμε για να έχουμε (Start -> Goal).
    path.reverse()
    return path

def format_action(action):
    
    # Βοηθητική: Μορφοποιεί το string της ενέργειας για πιο όμορφη εκτύπωση.
    # π.χ. το "move_right" γίνεται "MOVE_RIGHT"
    
    if action is None:
        return "-"
    return action.strip().upper() 

# Εκτυπώνει βήμα-προς-βήμα τη λύση που βρέθηκε.
def print_solution(path_states):
    
    if not path_states:
        print("Δεν βρέθηκε λύση.")
        return

    print("\n★ Λύση με τα Βήματα ★")
    print("-" * 60)
    step = 0
    
    # Ξεκινάμε από το 1 (το 0 είναι η αρχική κατάσταση χωρίς ενέργεια)
    for i in range(1, len(path_states)):
        curr = path_states[i]
        action = curr.action
        
        if action is None:
            continue
        
        step += 1
        name = format_action(action)
        # Format: Step XX | Action | Pos | Load
        print(f"Step {step:02} | Action={name:<11} | Pos={curr.position:<2} | Load={curr.load:<1}")
        
    print("-" * 60)
    print(f"Συνολικός αριθμός βημάτων: {step}\n")
    
def print_stats(stats):
    
    # Εκτυπώνει τα στατιστικά της αναζήτησης (Nodes Expanded, Generated, Memory).
    # Χειρίζεται διαφορετικά τα stats ανάλογα με το αν προέρχονται από A* (dictionary)
    # ή από DFS/BFS (attributes στο state object).
    
    print("\n★ Στατιστικά Αναζήτησης ★")
    
    # Περίπτωση A*: Τα στατιστικά επιστρέφονται ως Dictionary
    if isinstance(stats, dict):
        expanded = stats.get('expanded', 'N/A')
        generated = stats.get('generated', 'N/A')
        max_frontier = stats.get('max_frontier', 'N/A')
        cost = stats.get('solution_cost', 'N/A')
        
    # Περίπτωση BFS/DFS: Τα στατιστικά είναι αποθηκευμένα στο ίδιο το State object
    else:
        expanded = getattr(stats, 'expanded', 'N/A')
        generated = getattr(stats, 'generated', 'N/A')
        max_frontier = getattr(stats, 'max_frontier', 'N/A')
        # Στα BFS/DFS το κόστος λύσης είναι το βάθος του δέντρου
        cost = getattr(stats, 'depth', 'N/A') 
        
    print(f"Expanded nodes    : {expanded}")
    print(f"Generated nodes   : {generated}")
    print(f"Max frontier size : {max_frontier}")
    print(f"Solution cost     : {cost}")
    print("-" * 30)