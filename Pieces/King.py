from pieces_functions import *
from Pieces.Piece import Piece

class King(Piece):
    def __init__(self, color, isWhite): #sets attributes of piece
        self.isWhite = isWhite
        self.color = color
        self.points = 1000
        self.moved = False
        self.type = 'King'
        self.initial = 'K' if isWhite else 'k'
    
    def build(self): #builds copy of piece
        return King(self.color,self.isWhite)

    def move_piece(self): #changes status of piece, prevents castling
        self.moved = True
    
    def possible_moves(self,origin):
        change = [
            [-1,-1],
            [-1,1],
            [1,-1],
            [1,1],
            [1,0],
            [-1,0],
            [0,1],
            [0,-1]
        ]

        moves = []

        for m in change:
            moves.append(
                [[origin[0] + m[0], origin[1] + m[1]]]
            )
        
        return move_in_board(moves)

    def valid_move(self,board, origin, target):

        piece_d = get_piece(board,target)

        if not enemy_or_empty(piece_d, self.isWhite): #checks if is opponent of empty square
            return False
        
        diff = get_diff(origin,target)

        if diff_is_Zero(diff): #check if there is a move at all
            return False
        
        if not (abs(diff[0]) <= 1 and abs(diff[1]) <= 1): #checks if it is a 1 square move
            return False
        
        if not (same_line(diff) or same_diagonal(diff)): #is diagonal or line
            return False
        
        elif same_line(diff):
            path = get_straight_path(board,origin,diff) #sets path if line
        
        else:
            path = get_diagonal_path(board,origin,target,diff) #sets path if diagonal
        
        path = path[1:-1]

        path_filtered = filter(lambda x: x == None, path)
        path_filtered = list(path_filtered)

        if not same_length(path,path_filtered): #checks length
            return False

        return True