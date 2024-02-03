
'''
Class responsible for storing all the information about the current state of a chess game. Also will be responsible for determining the valid moves at the current state. It will also keep a move log.
'''

class GameState():
    def __init__(self):
        #8X8 2D list, each element of the list has 2 characters
        #First character represents the color of the piece, 'b' or 'w'
        #Second character represents the type of the piece, 'K', 'Q', 'R', 'B', 'N' (for knight), or 'p'
        #"--" represents an empty space with no piece
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        #Field that determines whose turn it is
        self.whiteToMove = True 

        #List to keep track of what move is currently taking place
        self.moveLog = []