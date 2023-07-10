
board = ['#'," ", " "," ", " "," ", " "," ", " "," "]
test_board = ['#','X','O','X','O','X','O','X','O','X']
def display_board(board):
    print(board[1]+" |"+board[2]+" |"+board[3])
    print("__|__|_")
    print(board[4]+" |"+board[5]+" |"+board[6])
    print("__|__|_")
    print(board[7]+" |"+board[8]+" |"+board[9])

def player_input():    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()  #Taking Player Input

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position]= marker                      #Assigning the Marker to the desired position



def win_check(board, mark):    #Winning conditions
    if board[1]==mark and board[5]==mark and board[9]==mark:
        return True
    elif board[3]==mark and board[5]==mark and board[7]==mark:
        return True
    elif board[1]==mark and board[2]==mark and board[3]==mark:
        return True
    elif board[4]==mark and board[5]==mark and board[6]==mark:
        return True
    elif board[7]==mark and board[8]==mark and board[9]==mark:
        return True
    elif board[1]==mark and board[4]==mark and board[7]==mark:
        return True
    elif board[2]==mark and board[5]==mark and board[8]==mark:
        return True
    elif board[3]==mark and board[9]==mark and board[9]==mark:
        return True
    else:
        return False



import random           #Computer's Turn
def choose_first():
    if random.randint(1,2)==1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):   
    if board[position]=='x' or board[position]=='o':
        return False
    else:
        return True

def full_board_check(board):
    if ' ' not in board:
        return True

def player_choice(board):
    position = int(input("Enter the next position(1 to 9): "))
    if space_check(board, position):
        return position

def replay():
    value = input("do you want to play again y/n: ")
    if value == 'y':
        return True
    else:
        return False

print("welcome to tic tack toe")
while True:
    board = [' ']*10
    player1, player2 = player_input()
    turn = choose_first()
    print(turn + "will go first")
    play_game= input("Ready to play y/n: ").lower()
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    # Set the game up here
    #pass

    while game_on:
        if turn=='Player 1':
        #Player 1 Turn
            display_board(board)
            position = player_choice(board)
            place_marker(board,player1,position)
            if win_check(board,player1):
                print("CONGRATULATIONS PLAYER 1 WON")
                display_board(board)
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Draw")
                    break
                else:
                    turn='Player2'
        else:
        # Player2's turn.
            display_board(board)
            position = player_choice(board)
            place_marker(board,player2,position)
            if win_check(board,player2):
                print("CONGRATULATIONS PLAYER 2 WON")
                display_board(board)
                game_on=False
            else:
                if full_board_check(board):
                    #display_board(board)
                    print("Draw")
                    break
                else:
                    turn='Player 1'
    if not replay():
        break
