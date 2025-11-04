# Αρχείο εμφάνισης αποτελεσμάτων με διαδρομές και στατιστικών αναζήτησης

# Επιστρέφουμε μια λίστα με όλα τα State αντικείμενα από την αρχική (Initial)
# κατάσταση έως την τελική (goal)
def reconstruct_path(goal_state): 
                                  
    path = []
    state = goal_state
    
    while state is not None:
        path.append(state) # ανεβαίνουμε προς τα πάνω (goal -> parent -> parent -> ... -> initial)
        state = state.parent
    
    path.reverse() # μετά αντιστρέφουμε την λίστα (initial -> parent -> ... -> goal)
    return path


# Mορφοποιούμε το όνομα της ενέργειας σε κεφαλαία, αν δεν είναι None
def format_action(action):
    
    if action is None:
        return "-"
    
    return action.strip().upper() 

# Συνάρτηση εκτύπωσης της διαδρομής της λύσης 
def print_solution(path_states):
    
    print("\n★ Λύση με τα Βήματα ★")
    step = 0
    
    for i in range(1, len(path_states)):
        prev = path_states[i - 1]
        curr = path_states[i]
        action = curr.action
        
        if action is None:
            continue
        
        step += 1
        name = format_action(action)
        print(f"Step {step:02} | Action={name:<11} | Pos={curr.position:<2} | Load={curr.load:<1}")
        
    print("-" * 60)
    print(f"Συνολικός αριθμός βημάτων: {step}\n")
    
# Συνάρτηση εκτύπωσης στατιστικών αναζήτησης    
def print_stats(stats, solution_depth=None):
    
    print("\n★ Στατιστικά Αναζήτησης ★")
    print(f"Expanded nodes    : {getattr(stats, 'expanded', 'N/A')}")
    print(f"Generated nodes   : {getattr(stats, 'generated', 'N/A')}")
    print(f"Max frontier size : {getattr(stats, 'max_frontier', 'N/A')}")
    
    if solution_depth is not None:
        print(f"Solution depth    : {solution_depth}")
    print("-" * 60)