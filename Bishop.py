
from pieces_functions import *
from Piece import Piece

class Bishop(Piece):
    def __init__(self, color, isWhite): #makes attribute of piece
        self.isWhite = isWhite
        self.color = color
        self.type = 'Bishop'
        self.points = 3
        self.initial = 'B' if isWhite else 'b'
    
    def build(self): #build copy of piece
        return Bishop(self.color,self.isWhite)

    def valid_move(self,board, origin, target): #checks if the move is valid

        piece_d = get_piece(board,target)

        if not enemy_or_empty(piece_d, self.isWhite): #checks if target is opponent of empty square
            return False
        
        diff = get_diff(origin,target)

        if diff_is_Zero(diff): #checks if there is any move
            return False

        if not same_diagonal(diff): #checks if the move is a diagonal
            return False
        
        path = get_diagonal_path(board,origin,target,diff) #sets path
        
        path = path[1:-1]

        path_filtered = filter(lambda x: x == None, path)
        path_filtered = list(path_filtered)

        if not same_length(path,path_filtered): #checks path
            return False

        return True