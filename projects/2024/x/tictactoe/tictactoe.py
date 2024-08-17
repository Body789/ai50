"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


# Node data structure
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


# frontier
class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


# queue
class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


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
    Xs = 0
    Os = 0
    for row in board:
        for element in row:
            if element == X:
                Xs += 1
            elif element == O:
                Os += 1
    if Xs > Os:
        return O
    else:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.add((i, j))
    return result
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copied = copy.deepcopy(board)
    if copied[action[0]][action[1]] != EMPTY or action[0] > 2 or action[1] > 2 or action[0] < 0 or action[1] < 0:
        raise ValueError("Action not valid")
    copied[action[0]][action[1]] = player(board)
    return copied
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check each row , column and the x
    if board[0][0] == board[0][1] == board[0][2] == X or board[0][0] == board[0][1] == board[0][2] == O:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] == X or board[1][0] == board[1][1] == board[1][2] == O:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] == X or board[2][0] == board[2][1] == board[2][2] == O:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] == X or board[0][0] == board[1][0] == board[2][0] == O:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] == X or board[0][1] == board[1][1] == board[2][1] == O:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] == X or board[0][2] == board[1][2] == board[2][2] == O:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] == X or board[0][0] == board[1][1] == board[2][2] == O:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] == X or board[0][2] == board[1][1] == board[2][0] == O:
        return board[0][2]
    else:
        return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board)) == 0:
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError


# returs the min value which is O's opinion
def min_value(board):
    # setting infinity for recursion
    v = math.inf
    # condition to stop recursion
    if terminal(board):
        return utility(board)
    # for every action available
    for action in actions(board):
        # will check every conditon till end
        v = min(v, max_value(result(board, action)))
    return v


# same as before
def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Check each available
    # if lose remove
    # if won choose
    if terminal(board) == True:
        return None
    elif player(board) == X:
        games = []
        for action in actions(board):
            games.append([min_value(result(board, action)), action])
        return sorted(games, key=lambda x: x[0], reverse=True)[0][1]

    else:
        games = []
        for action in actions(board):
            games.append([max_value(result(board, action)), action])
        return sorted(games, key=lambda x: x[0])[0][1]
    raise NotImplementedError
