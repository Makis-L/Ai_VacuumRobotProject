from src.state import create_initial_state, is_goal
from src.findchildren import findchildren
from src.search_algorithms.dfs import dfs
from src.search_algorithms.bfs import bfs
from src.search_algorithms.a_star import astar_search
from src.heuristics import h2   # μπορείς να αλλάξεις σε h1, h2, ή να ζητήσεις από τον χρήστη
from src.printing import reconstruct_path, print_solution, print_stats

def main():
    initial_state = create_initial_state()
    print("★ Αρχική Κατάσταση ★")
    print(initial_state)
    print("-" * 40)
    answer = "A"
    
    print("Διάλεξε με ποιόν αλγόριθμο θες να καθαρίσεις τα πλακάκια.")
    print("1 ή D → DFS")
    print("2 ή B → BFS")
    print("3 ή A → A* (Ευριστική Αναζήτηση)")
    print("4 ή Q → Έξοδος")
    print("(↓)(↓)(↓)")
        
    answer = input().strip().upper()
        
    if answer == "1" or answer == "D":
        result_dfs = dfs(initial_state)
            
        if result_dfs is None:
            print("Δεν βρέθηκε λύση με τον αλγόριθμο DFS.")
        else:
            print(" " * 40)
            print("★ Τελική Κατάσταση ★")
            print(result_dfs)
            print("-" * 40)
            path = reconstruct_path(result_dfs)
            print_solution(path)
            print_stats(result_dfs, solution_depth=result_dfs.depth)

                
    elif answer == "2" or answer == "B":    
        result_bfs = bfs(initial_state)
            
        if result_bfs is None:
            print("Δεν βρέθηκε λύση με τον αλγόριθμο BFS.")
        else:
            print(" " * 40)
            print("★ Τελική Κατάσταση ★")
            print(result_bfs)
            print("-" * 40)
            path = reconstruct_path(result_bfs)
            print_solution(path)
            print_stats(result_bfs, solution_depth=result_bfs.depth)

    elif answer == "3" or answer == "A":

        print("\n★ Τρέχει ο A* με heuristic h2 ★")
        path, stats = astar_search(initial_state, is_goal, findchildren, heuristic_fn=h2)


        if path is None:
            print("Δεν βρέθηκε λύση με A*.")
        else:
            print("\n★ Τελική Κατάσταση (A*) ★")
            print(path[-1])
            print("-" * 40)

            print_solution(path)
            print_stats(stats)

                    
    elif answer == "4" or answer == "Q":
        print("Τα λέμε ξανά!")

if __name__ == "__main__":
    main()
    
