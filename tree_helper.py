from src.state import create_initial_state
from src.findchildren import findchildren

def print_tree_structure():
    initial = create_initial_state()
    # Λίστα με (state, depth, parent_id)
    # parent_id είναι απλά για να ξέρεις ποιος είναι ο γονιός στο σχέδιο
    queue = [(initial, 0, "ROOT")] 
    
    print("--- ΔΕΔΟΜΕΝΑ ΓΙΑ ΤΗ ΣΧΕΔΙΑΣΗ ΤΟΥ ΔΕΝΤΡΟΥ (Βάθος 0 έως 3) ---")
    
    visited_count = 0
    
    while queue:
        current_state, depth, parent_name = queue.pop(0)
        
        if depth >= 3: # Σταματάμε να επεκτείνουμε αν είμαστε στο βάθος 3 (για να βρούμε τα παιδιά του 3 -> βάθος 4)
            # Απλώς τυπώνουμε τα παιδιά χωρίς να τα βάλουμε στην ουρά
            children = findchildren(current_state)
            if children:
                print(f"\n[Depth {depth}] Node {visited_count} (Parent: {parent_name})")
                print(f"  State: {current_state.position}, Trash: {current_state.trash}, Load: {current_state.load}")
                print(f"  --> Children (Depth {depth+1}):")
                for action, child, _ in children:
                     print(f"      -- {action} --> Pos={child.position}, Load={child.load}, Trash={child.trash}")
            visited_count += 1
            continue

        # Αν depth < 3, επεκτείνουμε κανονικά
        children = findchildren(current_state)
        print(f"\n[Depth {depth}] Node {visited_count} (Parent: {parent_name})")
        print(f"  State: Pos={current_state.position}, Trash={current_state.trash}, Load={current_state.load}")
        
        node_id = visited_count
        visited_count += 1
        
        if children:
            print(f"  --> Generates:")
            for action, child, _ in children:
                print(f"      Action: {action}")
                queue.append((child, depth + 1, f"Node {node_id}"))

if __name__ == "__main__":
    print_tree_structure()