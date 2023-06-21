from queue import Queue
from tkinter import tk

initial = [1, 1]
goal = [8, 2]
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

fwdpath = {}


def moves(state, move):
    i, j = state[0], state[1]
    if move == 'down':
        new_i, new_j = i, j + 1
    elif move == 'up':
        new_i, new_j = i, j - 1
    elif move == 'left':
        new_i, new_j = i - 1, j
    elif move == 'right':
        new_i, new_j = i + 1, j
    new_state = [new_i, new_j]    
    print(new_state)

    if maze[new_i][new_j]==1:
        maze[new_i][new_j]=5
        cell_color="orange"
        label=tk.label(state,wdith=1,height=1,bg=cell_color)
        label.grid(row=i,column=j)
    return new_state


def gen(state):
    i, j = state[0], state[1]
    possible_moves = []
    if maze[i + 1][j] == 1:
        possible_moves.append('right')
    if maze[i - 1][j] == 1:
        possible_moves.append('left')
    if maze[i][j + 1] == 1:
        possible_moves.append('down')
    if maze[i][j - 1] == 1:
        possible_moves.append('up')
    print(possible_moves)
    return possible_moves


def bfs(initial, goal):
    bfspath = {}
    frontier = Queue()
    frontier.put((initial, []))
    explored = []
    while not frontier.empty():
        state, path = frontier.get() #################################
        explored.append(str(state))
        if state == goal:
            return path ################################

        for move in gen(state):
            new_state = moves(state, move)
            if str(new_state) not in explored:
                frontier.put((new_state, path + [new_state])) ######################
                explored.append(str(new_state))
            
def final(state,path):
    cell_color='green'
    for state in path:
        label=tk.label(state,width=1,height=1,bg=cell_color)
        label.grid(row=state[0],column=state[1])
        state.update()


result_unsolvable = bfs(initial, goal)
print(result_unsolvable)
