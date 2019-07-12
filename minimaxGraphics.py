#!/usr/bin/env python3
from math import inf as infinity, sqrt
from random import choice
import platform
import time
from os import system
import pygame


from threading import Timer

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

class circle:
    center: (int, int)
    radius: int
    color: (int, int, int)
    _has_piece_: bool

    def __init__(self, x: int, y: int, r: int):
        self.center = (x + r, y + r)  # Assumes the top-left coordenates.
        self.radius = r
        self.color = (255, 255, 255)

    def is_in_range(self, x: int, y: int) -> bool:
        x_diff_squared = pow(self.center[0] - x, 2)
        y_diff_squared = pow(self.center[1] - y, 2)
        return sqrt(x_diff_squared + y_diff_squared) < self.radius

    def set_piece(self, value: bool):
        self._has_piece_ = value




class Board:
    color = (0, 0, 0)
    area = pygame.Rect(0, 0, 0, 0)

    piecePositions = []

    humanColor: (int, int, int)
    aiColor: (int,  int,  int)
    __humanChar: str
    __aiChar: str

    def __init__(self):
        #   X   Y
        # X  Y
        self.area = pygame.Rect(0, 0,  ## Coord
                                300, 300)  ## Size

        self.piecePositions = []

        circle_radius = min(self.area.height, self.area.width) // 8
        for circle_x in range(self.area.left, self.area.right, self.area.width // 4):
            for circle_y in range(self.area.top, self.area.bottom, self.area.height // 4):
                self.piecePositions.append(circle(circle_x, circle_y, circle_radius))

    def render_board(self, h_choice, c_choice):
        y = 0
        for i in board:
            x = 0
            for j in i:
                clr = ()
                if j == -1:
                    clr = self.humanColor
                    print("if human")
                elif j == 1:
                    clr = self.aiColor
                    print("if comp")
                else:
                    clr = (255, 255, 255)
                index = y + x * 4 
                self.piecePositions[index].color = clr
                print(self.piecePositions[index].color)
                x += 1
            y += 1


    def draw(self):
        pygame.draw.rect(gameScreen, (0, 0, 0), self.area)

        for i in self.piecePositions:
            pygame.draw.circle(gameScreen, i.color, i.center, i.radius, 0)

    def in_range_of(self, pos):
        acc = 0
        for c in self.piecePositions:
            if c.is_in_range(pos[0], pos[1]):
                return acc
            acc += 1
        return -1

    def set_player_color(self, p):
        self.__humanChar = p
        if p == "R":
            self.__aiChar = "B"
            self.humanColor = (255, 0, 0)
            self.aiColor = (0, 0, 255)
        else:
            self.__aiChar = "R"
            self.humanColor = (0, 0, 255)
            self.aiColor = (255, 0, 0)
        print(self.humanColor, " ", self.aiColor, "  " ,self.__humanChar, " ", self.__aiChar)



HUMAN = -1
COMP = +1
board = [
    [0, 0, 0 ,0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
graphicalBoard: Board = Board()

frozenGame = False

gameScreen = pygame.display.set_mode((300, 300))


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


def minimax(state, depth, player):
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
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

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
    str_line = '--------------------'

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

    #clean()
    print(f'Computer turn [{c_choice}]')


    if depth == 16:
        x = choice([0, 1, 2, 3])
        y = choice([0, 1, 2, 3])
    else:
        move = minimax(board, 6, COMP)
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

    #clean()
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


def index_to_coord(index):
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [0, 3],
        5: [1, 0], 6: [1, 1], 7: [1, 2], 8: [1, 3],
        9: [2, 0], 10: [2, 1], 11: [2, 2], 12: [2, 3],
        13: [3, 0], 14: [3, 1], 15: [3, 2], 16: [3, 3],
    }
    print(index + 1)
    z = moves[index + 1]
    print(z)
    return z


def main():
    """
    Main function that calls all functions
    """




    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while h_choice != 'R' and h_choice != 'B':
        try:
            print('')
            h_choice = input('Choose R or B\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    graphicalBoard.set_player_color(h_choice)
    if h_choice == 'R':
        c_choice = 'B'
    else:
        c_choice = 'R'

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



    gameScreen.fill((255, 255, 255))
    graphicalBoard.draw()

    if first == 'N':
        ai_turn(c_choice, h_choice)
        first = ''

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        gameScreen.fill((255, 255, 255))
        graphicalBoard.draw()

        for event in pygame.event.get():
            event_type = event.type

            buttons = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            if event_type == pygame.QUIT:
                pygame.quit()
                quit()

            if event_type == pygame.MOUSEBUTTONDOWN:
                if buttons[0]:  # Left click
                    play = graphicalBoard.in_range_of(mouse_pos)
                    if play >= 0:
                        coords = index_to_coord(play)
                        if valid_move(coords[1], coords[0]):
                            render(board, c_choice, h_choice)
                            set_move(coords[1], coords[0], HUMAN)
                            render(board, c_choice, h_choice)
                            graphicalBoard.render_board(h_choice, c_choice)
                            graphicalBoard.draw()
                            ai_turn(c_choice, h_choice)
                            render(board, c_choice, h_choice)
                            graphicalBoard.render_board(h_choice, c_choice)
                        else:
                            print('please make a valid move')

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
