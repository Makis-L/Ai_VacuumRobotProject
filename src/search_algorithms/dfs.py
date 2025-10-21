from src.state import State, create_initial_state, is_goal
from src.findchildren import findchildren

def dfs(initial_state):
    
    initial_state = create_initial_state()
    
    frontier = [initial_state]
    closed = set() # Δημιουργούμε ένα άδειο σύνολο state που έχουμε επισκεφθεί, με set()
    
    while frontier:
        current = frontier.pop() # Παίρνουμε το τελευταίο στοιχείο της λίστας, δηλαδή το αφαιρεί από την λίστα και το παίρνουμε σαν τιμή
        
        if current in closed:
            continue # Αν εντοπιστεί state με ίδιο __hash__ με το current state, τότε απλά προχωράμε στο επόμενο
            
        if is_goal(current):
            return current
        
        children = findchildren(current) # Επιστρέφουμε μια λίστα με τα παιδία του current state
        
        for child in children:
            frontier.append(child) # Προσθέτουμε τα παιδία του current state στο τέλος της ουράς frontier
        
        closed.add(current)
    
    return None