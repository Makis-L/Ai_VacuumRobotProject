def reconstruct_path(goal_state): 
    path = []
    state = goal_state
    
    while state is not None:
        path.append(state)
        state = state.parent
    
    path.reverse()
    return path

def format_action(action):
    if action is None:
        return "-"
    return action.strip().upper() 

def print_solution(path_states):
    if not path_states:
        return

    print("\n★ Λύση με τα Βήματα ★")
    print("-" * 60)
    step = 0
    
    for i in range(1, len(path_states)):
        curr = path_states[i]
        action = curr.action
        
        if action is None:
            continue
        
        step += 1
        name = format_action(action)
        print(f"Step {step:02} | Action={name:<11} | Pos={curr.position:<2} | Load={curr.load:<1}")
        
    print("-" * 60)
    print(f"Συνολικός αριθμός βημάτων: {step}\n")
    
def print_stats(stats, solution_depth=None):
    print("\n★ Στατιστικά Αναζήτησης ★")
    
    # Χειρισμός αν το stats είναι Dictionary (A*)
    if isinstance(stats, dict):
        expanded = stats.get('expanded', 'N/A')
        generated = stats.get('generated', 'N/A')
        max_frontier = stats.get('max_frontier', 'N/A')
        cost = stats.get('solution_cost', 'N/A')
    # Χειρισμός αν το stats είναι Object State (BFS/DFS)
    else:
        expanded = getattr(stats, 'expanded', 'N/A')
        generated = getattr(stats, 'generated', 'N/A')
        max_frontier = getattr(stats, 'max_frontier', 'N/A')
        cost = getattr(stats, 'depth', 'N/A') # Στο BFS/DFS το κόστος είναι το βάθος

    print(f"Expanded nodes    : {expanded}")
    print(f"Generated nodes   : {generated}")
    print(f"Max frontier size : {max_frontier}")
    print(f"Solution cost     : {cost}")
    
    print("-" * 60)