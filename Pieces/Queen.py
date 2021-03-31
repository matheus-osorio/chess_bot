from pieces_functions import *
from Pieces.Piece import Piece

class Queen(Piece):
    def __init__(self, color, isWhite): #creates piece attributes
        self.isWhite = isWhite
        self.color = color
        self.type = 'Queen'
        self.points = 9
        self.initial = 'Q' if isWhite else 'q'
    
    def build(self): #Builds copy
        return Queen(self.color,self.isWhite)

    def possible_moves(self,origin):
        moves = [
            [[i,j] for i in range(origin[0],-1,-1) for j in range(origin[1],-1,-1)],
            [[i,j] for i in range(origin[0],8) for j in range(origin[1],-1,-1)],
            [[i,j] for i in range(origin[0],-1,-1) for j in range(origin[1],8)],
            [[i,j] for i in range(origin[0],8) for j in range(origin[1],8)]
        ]

        moves += [
            [[i,origin[1]] for i in range(origin[0]+1, 8)],
            [[i,origin[1]] for i in range(origin[0]-1, -1, -1)],
            [[origin[0],i] for i in range(origin[1]+1, 8)],
            [[origin[0],i] for i in range(origin[1]-1, -1, -1)]
        ]

        return moves

    def valid_move(self,board, origin, target): #WChecks if move is valid

        piece_d = get_piece(board,target)

        if not enemy_or_empty(piece_d, self.isWhite): #checks if target is opponent or empty space
            return False
        
        diff = get_diff(origin,target)

        if diff_is_Zero(diff): #checks if there is any move at all
            return False
               

        if not (same_line(diff) or same_diagonal(diff)): #checks if it is a valid move
            return False
        
        elif same_line(diff): #sets path if it is straight line
            path = get_straight_path(board,origin,diff)
        
        else: #sets path if it is diagonal
            path = get_diagonal_path(board,origin,target,diff)
        
            
        path = path[1:-1]

        path_filtered = filter(lambda x: x == None, path)
        path_filtered = list(path_filtered)

        if not same_length(path,path_filtered): #checks length
            return False

        return True

