"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid move")

    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    for player in (X, O):
        # Check row and column
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):  # Cek baris
                return player
            if all(board[j][i] == player for j in range(3)):  # Cek kolom
                return player
        # Cek diagonal
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return player
    return None


def terminal(board):
    return winner(board) is not None or all(EMPTY not in row for row in board)


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    if terminal(board):
        return None

    turn = player(board)

    if turn == X:
        best_score = -math.inf
        best_move = None
        for action in actions(board):
            score = minimax_value(result(board, action), False)
            if score > best_score:
                best_score = score
                best_move = action
        return best_move

    else:
        best_score = math.inf
        best_move = None
        for action in actions(board):
            score = minimax_value(result(board, action), True)
            if score < best_score:
                best_score = score
                best_move = action
        return best_move

def minimax_value(board, is_maximizing):
    if terminal(board):
        return utility(board)

    if is_maximizing:
        return max(minimax_value(result(board, action), False) for action in actions(board))
    else:
        return min(minimax_value(result(board, action), True) for action in actions(board))
