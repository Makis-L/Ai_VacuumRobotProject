from src.state import create_initial_state, create_random_state, is_goal
from src.findchildren import findchildren
from src.search_algorithms.dfs import dfs
from src.search_algorithms.bfs import bfs
from src.search_algorithms.a_star import astar_search
from src.heuristics import h2 
from src.printing import reconstruct_path, print_solution, print_stats

def run_algorithm(algo_name, initial_state):
    # Βοηθητική συνάρτηση για να τρέχει έναν αλγόριθμο και να τυπώνει συνοπτικά.
    print(f"\n{'='*20} {algo_name} {'='*20}")
    
    path, stats = None, None
    
    if algo_name == "DFS":
        goal_state = dfs(initial_state)
        if goal_state:
            path = reconstruct_path(goal_state)
            stats = goal_state # Το DFS επιστρέφει το state με τα stats μέσα
            
    elif algo_name == "BFS":
        goal_state = bfs(initial_state)
        if goal_state:
            path = reconstruct_path(goal_state)
            stats = goal_state
            
    elif algo_name == "A*":
        path, stats = astar_search(initial_state, is_goal, findchildren, heuristic_fn=h2)

    if path:
        print_solution(path)
        print_stats(stats)
    else:
        print("Δεν βρέθηκε λύση.")

def main():
    # Αρχική default κατάσταση
    current_initial_state = create_initial_state()
    
    answer = "" 

    while answer != "Q" and answer != "6":
        
        print("\n" + "★" * 10 + " MENU " + "★" * 10)
        print("Τρέχουσα Αρχική Κατάσταση:")
        print(current_initial_state)
        print("-" * 40)
        print("1. DFS (Απλή εκτέλεση)")
        print("2. BFS (Απλή εκτέλεση)")
        print("3. A* (Απλή εκτέλεση)")
        print("4. Αλλαγή σε ΤΥΧΑΙΑ αρχική κατάσταση (New Random State)")
        print("5. ★ ΣΥΓΚΡΙΤΙΚΗ ΜΕΛΕΤΗ (Τρέχει και τους 3 στην τρέχουσα κατάσταση) ★")
        print("6. Έξοδος")
        print("(↓)(↓)(↓)")
        
        try:
            answer = input().strip().upper()
        except KeyboardInterrupt:
            print("\nΕλήφθη σήμα διακοπής. Έξοδος...")
            break
        except EOFError:
            break
        
        if answer == "1":
            run_algorithm("DFS", current_initial_state)

        elif answer == "2":    
            run_algorithm("BFS", current_initial_state)

        elif answer == "3":
            run_algorithm("A*", current_initial_state)

        elif answer == "4":
            current_initial_state = create_random_state()
            print("\n--> Δημιουργήθηκε νέα τυχαία κατάσταση!")

        elif answer == "5":
            print("\n" + "█" * 60)
            print("   ΕΝΑΡΞΗ ΣΥΓΚΡΙΤΙΚΗΣ ΜΕΛΕΤΗΣ  ")
            print("█" * 60)
            run_algorithm("DFS", current_initial_state)
            run_algorithm("BFS", current_initial_state)
            run_algorithm("A*", current_initial_state)
            print("\n" + "█" * 60)
            print("   ΤΕΛΟΣ ΣΥΓΚΡΙΤΙΚΗΣ ΜΕΛΕΤΗΣ  ")
            print("█" * 60)

        elif answer == "6" or answer == "Q":
            print("Τα λέμε ξανά!")
            break
        else:
            print("Παρακαλώ επέλεξε ξανά.")

if __name__ == "__main__":
    main()