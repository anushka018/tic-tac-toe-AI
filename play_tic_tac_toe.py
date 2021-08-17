#==========================================
# Purpose: determines the indicies of opens spaces on the board list
# Input Parameter(s): a list representing the board 
# Return Value(s): a list containing the indicies of the open slots 
#==========================================
def open_slots(board):
    openSlots = []
    for i in range (len(board)):
        if board[i]=="-":
            openSlots.append(i)
    return openSlots

#==========================================
#Purpose: prints out a tic-tac-toe board in standard 3x3 grid style
# Input Parameter(s): board - a 9 element list representing the 9 spots on a tic-tac-toe board
# Return Value(s): None
#==========================================
def display_board(board):
    for i in range(3):
        print(' '.join(board[3*i:3*i+3]))
    print()
    
#==========================================
# Purpose: determines if a player has won the game 
# Input Parameter(s): a list representing the board 
# Return Value(s): a single character string describing which player has won a game, if it is a draw, or if there are still open slots availible
#==========================================
def winner (board):
    wins = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == 'X':
            return 'X'
        if board[win[0]] == board[win[1]] == board[win[2]] == 'O':
            return 'O'
    if '-' in board:
        return '-'
    return 'D'

        


#==========================================
# Purpose: determines which player has won the game or if there is a draw
# Input Parameter(s): none
# Return Value(s): a single character string describing which player has won the game or if there is a draw
#==========================================
def tic_tac_toe():
    board = ['-']*9
    turn = 'X'
    while winner(board) == '-':
        slots = open_slots(board)
        pick = random.choice(slots)
        if turn == 'X':
            board[pick] = 'X'
            turn = 'O'


        elif turn == 'O':
            state = 1
            move = 0
            for i in (open_slots(board)):
                board_cpy=board[:]
                board_cpy[i]='O'
                current_state = force_win(board_cpy)
                
                if current_state < state:
                    state = current_state
                    move = i

            board[move] = 'O'
            turn = 'X'
    return winner(board)
            
                                  
#==========================================
# Purpose: print the number of x wins, o wins, and draws for a given number of tic tac toe games 
# Input Parameter(s): an integer representing the number of games to be played 
# Return Value(s): none
#==========================================
def play_games(n):
    winnars = []
    for i in range(n):
        game = tic_tac_toe()
        winnars.append(game)
    print("X wins:",winnars.count('X'))
    print("O wins:",winnars.count('O'))
    print("Draw:",winnars.count('D'))
    
    
#==========================================
# Purpose: create a tic tac toe AI using recursion that never loses 
# Input Parameter(s): board, a list that represents the current board
# Return Value(s): an int that represents the current state of the board:
# 0 if it is a draw, 1 if X won or can force a win. & -1 if O won or can force win
#==========================================
def force_win(board):
    
        if winner(board)== 'X':
            return 1
        elif winner(board)== 'O':
            return -1
        elif winner(board)== 'D':
            return 0
  
        else:
            if len(open_slots(board))%2==0:
                lowest_state = 1 
                for i in (open_slots(board)):
                    board_cpy=board[:]
                    board_cpy[i]='O'
                    current_value=force_win(board_cpy)                    

                    if current_value<lowest_state:
                        lowest_state = current_value
                        
                return lowest_state
            
            else:
                highest_state= -1
                for i in (open_slots(board)):
                    board_cpy=board[:]
                    board_cpy[i]='X'
                    current_value=force_win(board_cpy)                              

                    
                    if current_value>highest_state:
                        highest_state = current_value
                        
                return highest_state
                
