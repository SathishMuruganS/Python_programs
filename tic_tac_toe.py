print('Tic Tac Toe')
numpad ={1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1],9:[2,2]}
board = [[' ' for j in range(3)] for i in range(3)]
print(board)

player1 = 'X'
player2 = '0'
players = [player1, player2]
current_player_flag = player1


def clear_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '

def print_game_board(board):
    for col in board:
        print('------------------------------------')
        print('|     {}    |     {}     |     {}     |'.format(col[0], col[1], col[2]))
    print('------------------------------------')
    print()
    print()

def check_result(board):
    global current_player_flag
    n = 3
    for i in range(n):
        if board[0][i] == current_player_flag and board[1][i] == current_player_flag and board[2][i] == current_player_flag:
            return 1
        if board[i][0] == current_player_flag and board[i][1] == current_player_flag and board[i][2] == current_player_flag:
            return 1
    if board[0][0] == current_player_flag and board[1][1] == current_player_flag and board[2][2] == current_player_flag:
        return 1
    if board[0][2] == current_player_flag and board[1][1] == current_player_flag and board[2][0] == current_player_flag:
        return 1

    for i in range(n):
        for j in range(n):
            if board[i][j] == ' ':
                return 2
    return 3


def update_current_player():
    global current_player_flag
    if current_player_flag == player1:
        current_player_flag = player2
    else:
        current_player_flag = player1


def get_current_player():
    return current_player_flag

def get_input(board, location):
    current_player = get_current_player()
    numpad_pos_list = numpad[location]
    if board[numpad_pos_list[0]][numpad_pos_list[1]] != ' ':
        return False
    board[numpad_pos_list[0]][numpad_pos_list[1]] = current_player
    return True

while True:
    clear_board(board)
    while True:
        player1 = input('Player1 Do you want to be X or O')
        if player1 == 'X':
            player2 = 'O'
            break
        elif player1 == 'O':
            player2 = 'X'
            break
        else:
            print('Invalid input... Please enter again...')
            continue
    val = input('Are you ready to play? Enter Yes or No ')
    if val.lower() == 'yes':
        current_player_flag = player1
        while True:
            print_game_board(board)
            location_val = input('Choose your next position (1-9)')
            if len(location_val) > 0 and location_val not in '123456789':
                print('Wrong entry... Please try again...')
                continue
            location = int(location_val)
            if get_input(board, location) == False:
                print('Wrong input... please enter again')
                continue
            print_game_board(board)
            results = check_result(board)
            if 0 == results or 1 == results:
                print('{} won this game'.format(current_player_flag))
                break
            elif 3 == results:
                print('Draw...')
                break

            update_current_player()
    elif val.lower() == 'no':
        print('Good bye...')
        break
    else:
        print('Wrong input.. Please try again...')
        continue
