# Αρχείο αναπαράστασης και δημιουργίας στιγμιοτύπων του κόσμου.

import random
class State:
    # Βασικός Constructor για την δημιουργία του state
    # State: Το στιγμιότυπο του κόσμου σε μια συγκεκριμένη στιγμή
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
        return f"Position Of Robot (0-7)= {self.position}, Trash in Floor= {self.trash}, Robot's Trash Load= {self.load}"
    
    # Χρειάζεται για το σωρό (heap) του A* σε περίπτωση ισοπαλίας κόστους
    def __lt__(self, other):
        return self.depth < other.depth

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
    return all(t == 0 for t in state.trash) and state.position == state.base and state.load == 0
        
def create_random_state():
    
    # Δημιουργεί μια τυχαία αρχική κατάσταση:
    # 1. Τυχαία θέση ρομπότ (0-7).
    # 2. Βάση του ρομπότ είναι η θέση εκκίνησης.
    # 3. Συνολικά 10 σκουπίδια μοιρασμένα τυχαία στα πλακάκια.
    # 4. Κανένα σκουπίδι στη θέση εκκίνησης του ρομπότ (βάση).
    
    # 1. Τυχαία θέση ρομπότ
    pos = random.randint(0, 7)
    
    # 2. Αρχικοποίηση σκουπιδιών
    trash = [0] * 8
    
    # 3. Τοποθέτηση 10 σκουπιδιών τυχαία (όχι στη θέση του ρομπότ)
    items_placed = 0
    while items_placed < 10:
        tile_index = random.randint(0, 7)
        if tile_index != pos: # Η βάση δεν μπορεί να έχει σκουπίδια
            trash[tile_index] += 1
            items_placed += 1
            
    return State(pos, trash, 0, base=pos)