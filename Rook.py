from pieces_functions import *
from Piece import Piece

class Rook(Piece):
    
    def __init__(self, color, isWhite): #sets variables for Rook object
        self.isWhite = isWhite
        self.color = color
        self.moved = False
        self.points = 5
        self.type = 'Rook'
        self.initial = 'R' if isWhite else 'r'
    
    def build(self): #Function to replicate the object
        return Rook(self.color,self.isWhite)
    
    def move_piece(self): #Changes Status (prevents castling with this Rook)
        self.moved = True

    def valid_move(self,board, origin, target): 
        
        piece_d = get_piece(board,target)

        if not enemy_or_empty(piece_d, self.isWhite): #checks if is opponent or empty square
            return False

        diff = get_diff(origin,target)

        if diff_is_Zero(diff): #checks if it's the same square
            return False

        if not same_line(diff): #checks if it is a straight line
            return  False
        

        path = get_straight_path(board,origin,diff)  

        path = path[1:-1]
        
        path_filtered = filter(lambda x: x == None, path) 
        path_filtered = list(path_filtered)
        
        if not same_length(path,path_filtered): #checks length
            return False
        
        return True