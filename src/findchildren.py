# Αρχείο συνάρτησης διαδόχων (succesor function)
# Πρακτικά η findchildren() παίρνει ένα state και επιστρέφει όλα τα "νόμιμα"
# επόμενα states που μπορούν να προκύψουν άν εφαρμόσουμε κάθε διαθέσιμο operator.

from src.state import State
from src.operators import move_left, move_right, clean, dump

ops = [
    ("move_left",  move_left, 1),
    ("move_right", move_right, 1),
    ("clean",      clean,     1),
    ("dump",       dump,      1)
]

def findchildren(state):
    children = []
    
    for action_name, op, cost in ops:
        new_state = op(state)
        
        if new_state is not None:
            # Επιστρέφουμε: (Όνομα Ενέργειας, Νέα Κατάσταση, Κόστος)
            children.append((action_name, new_state, cost))
            
    return children