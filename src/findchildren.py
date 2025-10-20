# Αρχείο συνάρτησης διαδόχων (succesor function)
# Πρακτικά η findchildren() παίρνει ένα state και επιστρέφει όλα τα "νόμιμα"
# επόμενα states που μπορούν να προκύψουν άν εφαρμόσουμε κάθε διαθέσιμο operator.

from src.state import State
from src.operators import move_left, move_right, clean, dump

def findchildren(state):
    
    children = []
    ops = [move_left, move_right, clean, dump]
    
    for x in ops:
        new_state = x(state)
        
        if new_state is not None:
            children.append(new_state)
    
    return children # Επιστρέφουμε λίστα με κινήσεις που μπορούν να προκύψουν (δηλαδή παιδία του κόμβου)