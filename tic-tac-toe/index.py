import os
import random

BOARD_PATH = './tic-tac-toe/board.txt'
EMPTY_BOARD = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def read_board(path):
    with open(path, 'r') as file:
        return file.read().splitlines()

def write_board(path, board):
    with open(path, 'w') as file:
        file.write('\n'.join(board))

def get_winner(board):
    lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]  # diagonals
    ]
    for line in lines:
        values = [board[idx-1] for idx in line]
        if all(value == values[0] for value in values):
            return values[0] if values[0] in ['x', 'o'] else ''
    return None

def find_empty_cells(board):
    return [idx for idx, cell in enumerate(board) if cell == ' ']

def print_board(board):
    print('Current Board:')
    print(board[:3])
    print(board[3:6])
    print(board[6:9])

def is_move_valid(board, row, col):
    is_off_board = (row < 0 or row > 2 or col < 0 or col > 2)
    idx = row * 3 + col
    return not (is_off_board or board[idx] != ' ')

def get_move(board):
    row = int(input("Which row? (0-indexed): "))
    col = int(input("Which col? (0-indexed): "))
    if is_move_valid(board, row, col):
        return row * 3 + col
    else:
        print('Invalid move... try again')
        return get_move(board)

def get_random_ai_move(board):
    empty_cell_idxs = find_empty_cells(board)
    rand_idx = random.choice(empty_cell_idxs)
    return rand_idx

def play_human_turn(player, board):
    move_idx = get_move(board)
    board[move_idx] = player
    return board

def play_ai_turn(player, board):
    move_idx = get_random_ai_move(board)
    board[move_idx] = player
    return board

def human_turn():
    continue_game = input("Continue? (y/n, default: y): ").lower()
    if continue_game == 'y':
        print('Continuing')
        board = read_board(BOARD_PATH)
    elif continue_game == 'n':
        print('Starting new game')
        board = EMPTY_BOARD[:]
    else:
        print('Only y and n are allowed')
        main()
        return

    print_board(board)
    winner = get_winner(board)
    if winner:
        print(f'{winner} wins!')
        return

    board = play_human_turn('x', board)
    print_board(board)
    winner = get_winner(board)
    if winner:
        print(f'{winner} wins!')
        return

    write_board(BOARD_PATH, board)
    print('Turn complete. Please commit and push the updated board file.')
    print('Pull in ~30 seconds to get the updated board for your next turn.')

def ai_turn():
    board = read_board(BOARD_PATH)
    play_ai_turn('o', board)
    write_board(BOARD_PATH, board)

