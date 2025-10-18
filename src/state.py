# Αρχείο αναπαράστασης και δημιουργίας στιγμιοτύπων του κόσμου.

class State:
    # Βασικός Constructor για την δημιουργία του state
    # State: Το στιγμιότυπο του κόσμου μια συγκεκριμένη χρονική στιγμή
    def __init__(self, position, trash, load, base, parent=None, action=None, depth=0):
        self.position = position
        self.trash = trash
        self.load = load
        self.base = base
        self.parent = parent
        self.action = action
        self.depth = depth
    
    # Συνάρτηση που εξετάζει αν δύο state είναι ίσα    
    def __eq__(self, other):
        return (
            self.position == other.position and
            self.trash == other.trash and
            self.load == other.load
        ) # Επιστρέφει True αν είναι ίσα και False αν δεν είναι
        
    # Συνάρτηση που δημιουργεί ένα "αποτύπωμα" για κάθε state για γρήγορη αναγνώριση    
    def __hash__(self):
        return hash((self.position, tuple(self.trash), self.load))
    
    # Συνάρτηση που επιστρέφει μια αναγνώσιμη αναπαράσταση του state
    def __str__(self):
        return f"Position= {self.position}, Trash= {self.trash}, Load= {self.load}"

# Συνάρτηση που δημιουργεί το αρχίκο state που παρουσιάζεται στην εκφώνηση της άσκησης
def create_initial_state():
    trash_distribution = [2, 3, 0, 0, 2, 0, 1, 2]
    base_position = 2
    return State (
        position = base_position,
        trash = trash_distribution,
        load = 0,
        base = base_position,
        parent = None,
        action = None,
        depth = 0
    )
 
# Συνάρτηση που επιστρέφει αν έχουν μαζευτεί επιτυχώς όλα τα σκουπίδια   
def is_goal(state):
    return all(t == 0 for t in state.trash)
        
        