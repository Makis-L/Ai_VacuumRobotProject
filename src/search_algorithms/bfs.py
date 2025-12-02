# Υλοποίηση του αλγορίθμου Αναζήτησης Πρώτα σε Πλάτος (Breadth-First Search - BFS).
# Ο αλγόριθμος εξερευνά το δέντρο καταστάσεων κατά επίπεδα (level-by-level).

from src.state import is_goal
from src.findchildren import findchildren

def bfs(initial_state):
    state = initial_state 
    
    # Το μέτωπο αναζήτησης (frontier). Στον BFS λειτουργεί ως Ουρά (Queue).
    # Αρχικοποιείται περιέχοντας μόνο την αρχική κατάσταση.
    frontier = [state]
    
    # Το σύνολο κλειστών κόμβων (closed set) για να θυμόμαστε ποιες καταστάσεις 
    # έχουμε ήδη επεκτείνει και να αποφεύγουμε κύκλους.
    closed = set()

    # Αρχικοποίηση μετρητών για τα στατιστικά της αναζήτησης
    expanded = 0       # Κόμβοι που επεκτάθηκαν (βγήκαν από το μέτωπο)
    generated = 1      # Κόμβοι που δημιουργήθηκαν συνολικά (μπήκαν στο μέτωπο)
    max_frontier = 1   # Μέγιστο πλήθος κόμβων που υπήρξαν ταυτόχρονα στο μέτωπο

    while frontier: # Όσο το μέτωπο δεν είναι άδειο, συνεχίζουμε την αναζήτηση
        
        current = frontier.pop(0)

        # Ενημερώνουμε το στατιστικό για το μέγιστο μέγεθος του μετώπου
        if len(frontier) > max_frontier:
            max_frontier = len(frontier)
        
        # Αν η κατάσταση έχει εξερευνηθεί ήδη, την αγνοούμε
        if current in closed:
            continue
        
        # Προσθέτουμε την κατάσταση στις κλειστές
        closed.add(current)
        
        # Έλεγχος αν η τρέχουσα κατάσταση είναι ο στόχος
        if is_goal(current):
            # Αποθηκεύουμε τα στατιστικά πάνω στο αντικείμενο state για την εκτύπωση
            current.expanded = expanded
            current.generated = generated
            current.max_frontier = max_frontier
            return current

        # Αυξάνουμε τον μετρητή επεκταμένων κόμβων
        expanded += 1

        # Βρίσκουμε τα παιδιά (επόμενες καταστάσεις) της τρέχουσας κατάστασης
        # Η findchildren επιστρέφει λίστα από tuples: (όνομα_ενέργειας, νέα_κατάσταση, κόστος)
        children = findchildren(current)
        
        for _, child, _ in children:
            # Ελέγχουμε αν το παιδί δεν είναι ούτε στις κλειστές ούτε στο μέτωπο
            # για να αποφύγουμε διπλές εγγραφές και άσκοπη επεξεργασία.
            if child not in closed and child not in frontier:
                frontier.append(child) # Προσθήκη στο τέλος της ουράς
                generated += 1
            
    return None