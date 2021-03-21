from pieces_functions import *
from Piece import Piece

class Knight(Piece):
    def __init__(self, color, isWhite): #sets attribute
        self.isWhite = isWhite
        self.color = color
        self.type = 'Knight'
        self.points = 3
        self.initial = 'N' if isWhite else 'n'

    def build(self): #build copy of object
        return Knight(self.color,self.isWhite)

    def valid_move(self,board, origin, target): #checks if move is valid

        piece_d = get_piece(board,target)

        if not enemy_or_empty(piece_d, self.isWhite): #checks if target is empty or opponent
            return False
        
        diff = get_diff(origin,target)

        if not (min(abs(diff[0]), abs(diff[1])) == 1 and max(abs(diff[0]), abs(diff[1])) == 2): #checks if it's a L shaped move
            return  False
        
        return True