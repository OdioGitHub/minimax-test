#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
WARNING: the code that follows will make you cry
     a safety dragon is provided below for your own security
                                                                 `.                                 
                                                             .++:.                                  
                                               .         `/sodN.                                    
                                      `+hs:`   y-     `/yy:` d+`                                    
                    `          ``    /Nd-     oN.   .sd+`    s+:                                    
                  ++:      `+y++N: -h++-    :d+o  :hh:       `sNo://:-.`                            
                `+++Nhhhhd+NNs  +NN++++s.-od+N+ -hd:       `:oyy+o`                                 
                s+++++++++++++++++++++++++++o.`sN+      .+hho- -+:                                  
                `N+++s/::://+sh+++++N+++y+-  -+h.    `/hd+.    `Ny                                  
                 -yo :hdhyssyhy:+++++d+No   +Ns    .s+s-        .yh:.-///:-.`                       
                  `+yo+` `.:+osd+++N/h+++- ++o   -y+o`        .:osy++:.`                            
            ``.-+ss/` :yy++++hsoosys+++++-++s  .yNo`     `:ohhs/.  hs                               
            `---`     /++do-     s++++++h-Nd``oNh.    -ohho:`      ++                               
                      `h-     `oNN+dN++N-d+:-d+o   :sdy/`          hy                               
                       ``    `y+N++++++::+++N+/`:s+h/`      ```....:+o.`                            
                          `s+NN+dN+++++ o+NhdNdN+h--/+syhhhyyssso++//sd/:-.`     
                         `h++++++++++d  sh.+:/++++yo+:.`            +s`                             
                       `o++ddd++++++++hooyNN.+++y-                `s/         `.                    
 .:/ss ``:            .++++++++++++++++++Ny-:N+NN+Ndyo+:-.`      .h.          s:                    
    `h+h-d-           oyhhhN++++++++++/...:y+N: ``.-:/++ossssoo++sy::-.     .h+`                    
   -o++++++         `sN++++++++++++++++o::/+sysooooo++///+++++/:--.`     `:yN+-  ``                 
  /+:s++++y         /+++++++++++++++++++++N++dddddd+++N++++++++++++++hoyd+++h+oyy:                  
     `N+++/       -+:ysyyd++++++++++++++++++++++++++++++++++++++++++++++++++++h/``-`                
      ./+h+:` `-od+++h++++++++++++++++++++++++++++++++++++N+N++++++++++++++++++N+s-                 
          h+NhN+++++N++++++dhd+++++++++++++++++++++++++dosyhyysoh+++++++++++++++N/                  
         s+++ `:sN++++:sysy+++++++++++++++++++++++++++y/++++++++s++++s`/h+++++++++s                 
         :++.    `/Nh    /+N++++++++++++++++++++N+ddd+-++++++++++.N++    -h++++++++.                
         .d/      `d-     .s++++++++++++++++++ssyd+Ny``d+++++++++.-        y+++++++-                
         .`       `        ++++++++++s++N+y+-y++++++`   +++++++++`         -++++++d                 
                           `N++++++y:`-`     :h++++d`     /d++++N+` `:     +++++++/                 
                           -+++y:`           `y+++NN+s:`    .odN++N+h/    `N++++++`                 
                           +++:             /dy+-.````         `o+++/     y++++++N:                 
                           /+y             s++                   /N+s     h++++++++do/-`            
                    `-.   o+N.       .-`./y++h--                 `N+``:.`  :sdN++++++++++y+-`       
                  :ooNNddN++Nd:    -h+++++hsyd++:          `/yds++++++Nh:-`   `.:osh+N++++++Ndo:`   
                  `  :ysNhd+h/oo  .s--+++N`   /h/          o/-/y++y+h`               `.:+y++++++Ns. 
                    +dys-/++y` `  `. s+hy:     `.             .NNs:+N.                     .++++++N:
                   `y    /o         :+          `/sy/`        ys:  -s-                       `y++++N
                    `    :          `.       .+d++h`         `/                               :+++++
                                           :h+++Nh/:+osyyhhhhhyysso+/::.``                   `h++++N
                                        `++++Nhyydho+/:-----:/+osyd+++++++N+dhyso+/::-----:+yN+++++/
                                     `:yN+Nyyyhh+`                   .-/oydN+++++++++++++++++++++d- 
                            :+///+sy+++++++N+N++++dhhho-                    `-/oydNN+++++++++Nds-   
                             `:oydNN+++++++++++N+dy+-`                             `.-:////-.`      
                                    `+++++++++´                                                     
"""

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0 ,0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Four rows     [X X X X] or [O O O O]
    * Four cols     [X X X X] or [O O O O]
    * Two diagonals [X X X X] or [O O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2], state[0][3]],
        [state[1][0], state[1][1], state[1][2], state[1][3]],
        [state[2][0], state[2][1], state[2][2], state[2][3]],
        [state[3][0], state[3][1], state[3][2], state[3][3]],
        [state[0][0], state[1][0], state[2][0], state[3][0]],
        [state[0][1], state[1][1], state[2][1], state[3][1]],
        [state[0][2], state[1][2], state[2][2], state[3][2]],
        [state[0][3], state[1][3], state[2][3], state[3][3]],
        [state[0][0], state[1][1], state[2][2], state[3][3]],
        [state[3][0], state[2][1], state[1][2], state[0][3]],
    ]
    if [player, player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player, cont):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 16),
    but never sixteen in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        cont = cont + 1
        if cont <= 30:
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = minimax(state, depth - 1, -player, cont)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == COMP:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value
        else:
            return best

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 16,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 16:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        cont = 0
        move = minimax(board, 5, COMP, cont)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


def human_turn(c_choice, h_choice):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [0, 3],
        5: [1, 0], 6: [1, 1], 7: [1, 2], 8: [1, 3], 
        9: [2, 0], 10: [2, 1], 11: [2, 2], 12: [2, 3],
        13: [3, 0], 14: [3, 1], 15: [3, 2], 16: [3, 3],
    }

    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 16:
        try:
            move = int(input('Use numpad (1..16): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()