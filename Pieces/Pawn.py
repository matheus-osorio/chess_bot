from pieces_functions import *
from Pieces.Piece import Piece

class Pawn(Piece):
    def __init__(self, color, isWhite): #basic attributes for piece
        self.isWhite = isWhite
        self.color = color
        self.moved = False
        self.points = 1
        self.type = 'Pawn'
        self.initial = 'P' if isWhite else 'p'
    
    def build(self): #builds a copy of this object
        piece = Pawn(self.color,self.isWhite)
        if(self.moved):
            piece.move_piece()
        
        return piece

    def move_piece(self): #what to do if piece moved (prevents doing 2 square move)
        self.moved = True
    
    def possible_moves(self,origin):
        coordenates = []

        if self.isWhite:
            line = [[origin[0] + 1, origin[1]], [origin[0] + 2, origin[1]]]
            diag1 = [[origin[0] + 1, origin[1] + 1]]
            diag2 = [[origin[0] + 1, origin[1] + -1]]
        else:
            line = [[origin[0] -1, origin[1]], [origin[0] -2, origin[1]]]
            diag1 = [[origin[0] - 1, origin[1] + 1]]
            diag2 = [[origin[0] - 1, origin[1] + -1]]
        
        coordenates = [line,diag1,diag2]

        return move_in_board(coordenates)

    def valid_move(self,board, origin, target): #checks if this piece can do this move

        piece_d = get_piece(board,target)

        if not enemy_or_empty(piece_d, self.isWhite): #checks if target is opponent or empty square
            return False
        
        diff = get_diff(origin,target)
        if self.isWhite: #because Pawn only moves foward you need to check a few things
                
            if diff[0] < 1 or abs(diff[1]) > 1 or diff[0] > 2: #checks if move is inside what is possible
                return False
                
            if diff[0] == 2 and (self.moved or diff[1] != 0 or get_piece(board,[origin[0] + 1,origin[1]]) != None): #checks double move is possible
                return False
            
    
        else:
            if diff[0] >= 0 or abs(diff[1]) > 1 or diff[0] < -2: #same as above but for black
                return False
            
            if diff[0] == -2 and (self.moved or diff[1] != 0 or get_piece(board,[origin[0] - 1,origin[1]]) != None):
                return False
        
            
        if same_diagonal(diff) and piece_d == None: #if diagonal, has to be capturing
                return False
        
        if same_line(diff) and piece_d != None: #if not diagonal, cant be capturing
                return False

        return True
