"""
Tic Tac Toe Player
"""

import math
import copy

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
    """
    Returns player who has the next turn on a board.
    """
    xcounter = 0
    ocounter = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xcounter += 1
            elif board[i][j] == O:
                ocounter += 1

    if xcounter > ocounter:
        return O
    else:
        return X
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible.add((i,j))

    return possible

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    
    return result

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                pass
            
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                pass
            
    if board[0][0] == board[1][1] == board[2][2]:
        if board[1][1] == X:
            return X
        elif board[1][1] == O:
            return O
        else:
            pass
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == X:
            return X
        elif board[1][1] == O:
            return O
        else:
            pass
        
    else:
        return None
            
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X) or (winner(board) == O):
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
            
    return True
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    if winner(board) == None:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    else:
        if player(board) == X:
            score, move = Maximized(board)
            return move
        if player(board) == O:
            score, move = Minimized(board)
            return move

def Maximized(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        test, act = Minimized(result(board, action))
        if test > v:
            v = test
            move = action
            if v == 1:
                return v, move

    return v, move
            
def Minimized(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        test, act = Maximized(result(board, action))
        if test < v:
            v = test
            move = action
            if v == -1:
                return v, move
            
    return v, move
               
            
