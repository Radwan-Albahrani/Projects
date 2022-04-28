"""
Tic Tac Toe Player
"""

from copy import deepcopy


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

# Get current player from the board
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count for how many X and O are in the game currently
    xCount = 0
    oCount = 0
    for player in board:
        for position in player:
            if position == X:
                xCount += 1
            elif position == O:
                oCount += 1

    # If X is more than O, next player is O. Otherwise next player is X
    if xCount > oCount:
        return O
    else:
        return X
            
# Get all available actions from the board
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Set of available moves
    available = set()

    # Find all available moves and add them to the set
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available.add((i, j))

    # Return available moves
    return available

# Get resultant board
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Get current player and assign their action to the board
    playerNow = player(board)
    newBoard = deepcopy(board)
    newBoard[action[0]][action[1]] = playerNow

    # Return the new board
    return newBoard

# Get the winner of the game, if there is one
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check Rows
    for row in board:
        if X in row and O not in row and EMPTY not in row:
            return X
        elif O in row and X not in row and EMPTY not in row:
            return O
        
    
    # Check Columns
    xFound = [False, 0]
    oFound = [False, 0]
    for j in range(3):
        for i in range(3):
            if board[i][j] == X:
                xFound[0] = True
                xFound[1] += 1
                continue
            elif board[i][j] == O:
                oFound[0] = True
                oFound[1] += 1
                continue
        if (xFound[0] and oFound[0]) or (xFound[0] and xFound[1] < 3) or (oFound[0] and oFound[1] < 3):
            xFound = [False, 0]
            oFound = [False, 0]
            continue
        
        else:
            if xFound[0] and xFound[1] == 3:
                return X
            if oFound[0] and oFound[1] == 3:
                return O

    # Check Diagonals
    if (board[0][0] == board[1][1] == board[2][2] ) or (board[0][2] == board[1][1] == board[2][0]):
        if board[1][1] == X:
            return X
        elif board[1][1] == O:
            return O

# Check if the game has ended, Return the winner
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If there is a winner, return True
    currentWinner = winner(board)
    if currentWinner is not None:
        return True
    
    # If no further actions are possible, return true
    if not any(EMPTY in row for row in board):
        return True

# Return numerical value for who won
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    whoWon = winner(board)
    if whoWon == X:
        return 1
    elif whoWon == O:
        return -1
    elif whoWon is None:
        return 0

# Function to start the minimax Algorithm
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Get Current Player
    currentPlayer = player(board)
    
    # If the player is X, find the max Value. Else, Find the min Value
    if currentPlayer == X:
        result = maxValue(board)
    else:
        result = minValue(board)
    
    # Return Optimal Action
    return result[1]

# Function to find the minimum Value a player can get
def minValue(board, Max = -2, Min = 2):
    # Best Action Value
    bestAction = None
    
    # If game is over
    if terminal(board):
        return [utility(board), bestAction]
    
    # Set value Current Min
    v = Min

    # Loop Through All actions
    for action in actions(board):
        # Get a utility value from maxValue function
        test = maxValue(result(board, action), Max, Min)[0]

        # If The test is the minimum Value, this is the best action. Exit loop
        if test == -1:
            bestAction = action
            return[test, action]
        
        # If the test value is less, That is the current optimal solution
        if test < v:
            v = test
            bestAction = action
        
        # Alpha-Beta Pruning Test
        Min = min(Min, test)
        if Max >= Min:
            break
    
    # After loop, Return value and best action
    return[v, bestAction]

# Function to find the Maximum Value a player can get
def maxValue(board, Max = -2, Min = 2):
    # Best Action Value
    bestAction = None

    # If the game is over, find utility
    if terminal(board):
        return [utility(board), bestAction]

    # Set value to current Max
    v = Max

    # Loop through all Actions
    for action in actions(board):
        
        # Get minimum Value
        test = minValue(result(board, action), Max, Min)[0]

        # If Test value is 1, this is the best action. Return it
        if test == 1:
            bestAction = action
            return[test, action]
        
        # If the test Value is more, this is an optimal Action
        if test > v:
            v = test
            bestAction = action
        
        # Check Max for Alpha Beta Pruning
        Max = max(Max, test)
        if Max >= Min:
            break
    # Return utility Value and best action
    return[v, bestAction]