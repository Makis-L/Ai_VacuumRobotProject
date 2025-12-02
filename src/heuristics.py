def remaining_trash(state):
    return sum(state.trash)

def h1(state):
    # Ευριστική h1: Απλή καταμέτρηση σκουπιδιών.
    # Επιστρέφει το πλήθος των μονάδων σκουπιδιών που υπάρχουν στο πάτωμα.
    # Δεν είναι πολύ ισχυρή, δεν θα την χρησιμοποιήσουμε.
    return remaining_trash(state)

def h2(state):
    rem = remaining_trash(state)
    if rem == 0:
        return abs(state.position - state.base)

    # Χρησιμοποιούμε i αντί για i+1 γιατί το position είναι 0-7
    dirt_positions = [i for i, v in enumerate(state.trash) if v > 0]
    
    min_p, max_p = min(dirt_positions), max(dirt_positions)
    
    # Απόσταση που καλύπτει τα σκουπίδια
    span = max_p - min_p
    
    # Απόσταση από τη θέση μας στο πλησιέστερο άκρο του διαστήματος των σκουπιδιών
    enter = min(abs(state.position - min_p), abs(state.position - max_p))
    
    # Απόσταση από τα σκουπίδια πίσω στη βάση (κατά προσέγγιση)
    exit_to_base = min(abs(state.base - min_p), abs(state.base - max_p))
    
    movement_est = span + enter + exit_to_base
    
    # Πολλαπλασιάζουμε το rem με έναν παράγοντα αν θέλουμε να του δώσουμε βάρος, 
    # αλλά εδώ το κρατάμε απλό (admissible).
    return rem + movement_est