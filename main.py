from src.state import create_initial_state
from src.search_algorithms.dfs import dfs
from src.search_algorithms.bfs import bfs
from src.printing import reconstruct_path, print_solution, print_stats

def main():
    initial_state = create_initial_state()
    print("★ Αρχική Κατάσταση ★")
    print(initial_state)
    print("-" * 40)
    answer = "A"

    while answer != "Q" and answer != "3" :
        
        print("Διάλεξε με ποιόν αλγόριθμο θες να καθαρίσεις τα πλακάκια.")
        print("Αν επιθυμείς με τον αλγόριθμο DFS, επέλεξε 1 ή D, αν επιθυμείς με τον BFS, επέλεξε 2 ή B")
        print("Αν επιθυμείς να τερματίσεις την εφαρμογή, επέλεξε 3 ή Q")
        print("(↓)(↓)(↓)")
        
        answer = input()
        
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

                    
        elif answer == "3" or answer == "Q":
            print("Τα λέμε ξανά!")
            
        else:
            print("Παρακαλώ επέλεξε ξανά:")

if __name__ == "__main__":
    main()
    
