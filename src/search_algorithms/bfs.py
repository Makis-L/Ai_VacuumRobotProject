from queue import Empty
from src.state import State, create_initial_state, is_goal
from src.findchildren import findchildren

initial_state = create_initial_state()

frontier = [initial_state]
closed = 0