import copy

INFINITY = 1e+10

class Puzzle:

    def __init__(self, elements):
        assert len(elements) == len(elements[0]), "Puzzle must have equal rows and columns"
        self.board = elements
        self.n_dims = len(elements)
        
        for i in range(self.n_dims):
            for j in range(self.n_dims):
                if self.board[i][j] == 0:
                    self.pos = (i, j)
                    break
                
    def display(self):
        for i in range(self.n_dims):
            for j in range(self.n_dims):
                print(self.board[i][j], end = " ")
            print()
        
        

def move(puzzle: Puzzle):

    x, y = puzzle.pos[0], puzzle.pos[1]
    dim = puzzle.n_dims
    possible_pos = []
    
    if x+1 < dim and y < dim:
        possible_pos.append((x+1, y))
    if x < dim and y+1 < dim:
        possible_pos.append((x, y+1))
    if x >= 1 and y >= 0:
        possible_pos.append((x-1, y))
    if x >= 0 and y >= 1:
        possible_pos.append((x, y-1))
        
    new_states = []
    for pos in possible_pos:
        pos_x, pos_y = pos[0], pos[1]
        new_elements = copy.deepcopy(puzzle.board)
        new_elements[pos_x][pos_y], new_elements[x][y] = new_elements[x][y], new_elements[pos_x][pos_y]
        new_states.append(Puzzle(new_elements))
        
    return new_states


def heuristic(init_puzzle: Puzzle, goal_puzzle: Puzzle):
    assert init_puzzle.n_dims == goal_puzzle.n_dims, "Puzzles must have equal dimensions"
    count_misplaced = 0
    
    for i in range(init_puzzle.n_dims):
        for j in range(init_puzzle.n_dims):
            if init_puzzle.board[i][j] != goal_puzzle.board[i][j]:
                count_misplaced += 1
                
    return count_misplaced


def is_goal(curr_puzzle: Puzzle, goal_puzzle: Puzzle):
    assert curr_puzzle.n_dims == goal_puzzle.n_dims , "Puzzles must have equal dimensions"

    for i in range(curr_puzzle.n_dims ):
        for j in range(curr_puzzle.n_dims ):
            if curr_puzzle.board[i][j] != goal_puzzle.board[i][j]:
                return False
            
    return True   



init_puzzle = Puzzle( [ [ 1 , 2 , 3 ] , [ 0 , 4 , 6 ] , [ 7 , 5 , 8 ] ] )
print( "Initial state:" )
init_puzzle.display()

goal_puzzle = Puzzle( [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 0 ] ] )
print( "Goal state:" )
goal_puzzle.display()

print("---------------------------------------")

open_set: list[Puzzle] = [ init_puzzle ]

g_score: dict[Puzzle,int] = {}
g_score[ init_puzzle ] = 0

f_score: dict[Puzzle,int] = {}
f_score[ init_puzzle ] = heuristic(init_puzzle, goal_puzzle)

num_step = 1
while len(open_set) != 0:
    print(">>> Step ", num_step, ":")

    min_f_score_node = open_set[0]
    min_f_score = f_score.get(min_f_score_node, INFINITY)
    for node in open_set:
        score = f_score.get(node, INFINITY)
        if score < min_f_score:
            min_f_score = score 
            min_f_score_node = node

    print(">> Selected state from Frontier: ")    
    current_state = min_f_score_node
    current_state.display()
    print()
    num_step += 1

    if is_goal(current_state, goal_puzzle):
        print("Done") 
        break

    print(">> Possible States: ")
    open_set.remove(current_state)

    for neighbour in move(current_state):
        cost_thru_current = g_score.get(current_state, INFINITY) + 1

        if cost_thru_current < g_score.get(neighbour , INFINITY):
            g_score[neighbour] = cost_thru_current
            f_score[neighbour] = cost_thru_current + heuristic(neighbour, goal_puzzle)
            if neighbour not in open_set:
                open_set.append(neighbour)
                neighbour.display()
                print(f"h(n) for above state is {heuristic(neighbour, goal_puzzle)}")
                print(f"g(n) for above state is {g_score[neighbour]}")
                print(f"f(n) for above state is {f_score[neighbour]}")
                print()
    print()
    print("-------------------------")
    print()