# Υλοποίηση του αλγορίθμου Αναζήτησης Πρώτα σε Βάθος (Depth-First Search - DFS).
# Ο αλγόριθμος εξερευνά το δέντρο πηγαίνοντας όσο πιο βαθιά γίνεται πριν οπισθοδρομήσει.

from src.state import is_goal
from src.findchildren import findchildren

def dfs(initial_state):
    
    state = initial_state 

    # Το μέτωπο αναζήτησης (frontier). Στον DFS λειτουργεί ως Στοίβα (Stack).
    # LIFO (Last-In, First-Out).
    frontier = [state]
    
    # Σύνολο κλειστών κόμβων για να αποφεύγουμε κύκλους και επαναλήψεις.
    closed = set()

    # Αρχικοποίηση στατιστικών
    expanded = 0
    generated = 1
    max_frontier = 1

    while frontier:
        # Ενημέρωση του μέγιστου μεγέθους της στοίβας
        if len(frontier) > max_frontier:
            max_frontier = len(frontier)

        # Αφαιρούμε το ΤΕΛΕΥΤΑΙΟ στοιχείο που μπήκε (LIFO).
        # Η εντολή pop() χωρίς όρισμα βγάζει το τελευταίο στοιχείο της λίστας.
        current = frontier.pop()

        # Αν έχουμε ξαναπεράσει από αυτή την κατάσταση, την προσπερνάμε.
        if current in closed:
            continue
        
        # Μαρκάρουμε την κατάσταση ως "κλειστή" (επισκεφθείσα)
        closed.add(current)

        # Έλεγχος τερματισμού (Goal Test)
        if is_goal(current):
            # Αποθήκευση στατιστικών στο state για την εκτύπωση
            current.expanded = expanded
            current.generated = generated
            current.max_frontier = max_frontier
            return current

        expanded += 1

        # Παραγωγή παιδιών
        children = findchildren(current)
        
        # Διατρέχουμε τα παιδιά. 
        for _, child, _ in children:
            # Αν δεν το έχουμε επισκεφτεί ήδη, το βάζουμε στη στοίβα.
            # Δεν ελέγχουμε αν είναι στο frontier (όπως στο BFS) γιατί στο DFS 
            # επιτρέπεται να υπάρχουν πολλαπλά μονοπάτια προς τον ίδιο κόμβο στη στοίβα,
            # αρκεί να τα προλαβαίνει το closed set όταν βγουν.
            if child not in closed:
                frontier.append(child)
                generated += 1

    # Αν αδειάσει η στοίβα και δεν βρεθεί λύση
    return None