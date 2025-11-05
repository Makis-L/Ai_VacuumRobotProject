from src.state import State, create_initial_state, is_goal
from src.findchildren import findchildren
from src.search_algorithms.statistics import Stats

def bfs(initial_state):
    
    initial_state = create_initial_state()
    
    frontier = [initial_state]
    closed = set() # Δημιουργούμε ένα άδειο σύνολο state που έχουμε επισκεφθεί, με set()
    
    while frontier:
        current = frontier.pop(0) # Παίρνουμε το πρώτο στοιχείο της λίστας, δηλαδή το αφαιρεί από την λίστα και το παίρνουμε σαν τιμή
        
        if current in closed:
            continue
        
        if is_goal(current):
            return current
        
        children = findchildren(current)
        
        for child in children:
            frontier.append(child)
        
        closed.add(current)
    
    
