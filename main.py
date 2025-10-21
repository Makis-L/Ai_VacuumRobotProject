from src.state import create_initial_state
from src.search_algorithms.dfs import dfs
from src.search_algorithms.bfs import bfs

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
        
                steps = []
                current = result_dfs
                while current is not None:
                    steps.append(current.action)
                    current = current.parent
                steps.reverse()
                print("\n★ Διαδρομή ενεργειών ★")
                print(steps)
                print(" " * 40)
                print("-" * 40)
                
        elif answer == "2" or answer == "B":    
            result_bfs = bfs(initial_state)
            
            if result_bfs is None:
                print("Δεν βρέθηκε λύση με τον αλγόριθμο BFS.")
            else:
                print(" " * 40)
                print("★ Τελική Κατάσταση ★")
                print(result_bfs)
                print("-" * 40)
        
            steps = []
            current = result_bfs
            while current is not None:
                steps.append(current.action)
                current = current.parent
                
            steps.reverse()
            print("★ Διαδρομή ενεργειών ★")
            print(steps)
            print(" " * 40)
            print("-" * 40)
                    
        elif answer == "3" or answer == "Q":
            print("Τα λέμε ξανά!")
            
        else:
            print("Παρακαλώ επέλεξε ξανά:")

if __name__ == "__main__":
    main()
    
