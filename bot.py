from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from King import King
from Queen import Queen
from Pawn import Pawn

class Bot:
    
    def __init__(self,color,level):
        
        pieces_m = [Rook,Knight,Bishop,King,Queen,Bishop,Knight,Rook]
        
        self.isWhite = color == 'white'
        self.level = level
        pieces_p = [Pawn] * 8
        self.board = [
             [piece('white',True) for piece in pieces_m],
             [piece('white',True) for piece in pieces_p],
             [None] * 8,
             [None] * 8,
             [None] * 8,
             [None] * 8,
             [piece('black',False) for piece in pieces_p],
             [piece('black',False) for piece in pieces_m]
        ]

    def opponent_move(self, origin, target):
        move_piece(self.board,origin,target)

    def choose_move(self):
        moves = []
        for target_x in range(0,8):
            for target_y in range(0,8):

                for initial_x in range(0,8):
                    for initial_y in range(0,8):
                        
                        if self.board[initial_x][initial_y] == None:
                            continue
                        
                        piece = self.board[initial_x][initial_y]

                        if piece.isWhite != self.isWhite:
                            continue

                        origin = [initial_x,initial_y]
                        target = [target_x, target_y]
                        
                        if not piece.valid_move(self.board,origin,target):
                            continue 
                        
                        moves.append({
                            'origin': origin,
                            'target': target
                        })
        
        for move in moves:
           board_c = copy_board(self.board)
           move_piece(board_c, move['origin'],move['target'])
           move['points'] = do_min(board_c,self.isWhite,-1000000,1,self.level) 
        
        coordenates = moves[0]
        for move in moves:
            if move['points'] > coordenates['points']:
                coordenates = move
        
        move_piece(self.board,coordenates['origin'],coordenates['target'])

        return coordenates
        


def copy_board(board):
    board_n = []
    for i in range(0,8):
        row = []
        for j in range(0,8):
            sq = None
            if board[i][j] != None:
                sq = board[i][j].build()
            row.append(sq)
        
        board_n.append(row)
    
    return board_n

def move_piece(board, origin, destiny):
    piece = board[origin[0]][origin[1]]
    piece.move_piece()
    board[origin[0]][origin[1]] = None
    board[destiny[0]][destiny[1]] = piece
    return board

def do_max(board,isWhite,threshold,level, maximum):
    
    if level >= maximum:
        return count_points(board,isWhite)

    value = None
    for target_x in range(0,8):
        for target_y in range(0,8):

            for initial_x in range(0,8):
                for initial_y in range(0,8):
                    
                    if board[initial_x][initial_y] == None:
                        continue
                    
                    
                    piece = board[initial_x][initial_y]

                    if piece.isWhite != isWhite:
                            continue
                    
                    
                    origin = [initial_x,initial_y]
                    target = [target_x, target_y]
                    
                    if not piece.valid_move(board,origin,target):
                        continue 
                    
                    board_c = copy_board(board)
                    move_piece(board_c,origin,target)
                    path_v = do_min(board_c,isWhite,(-1000000 if value == None else value),level + 1, maximum)
                    
                    if path_v > threshold and level > 1:
                        return path_v
                        
                    if value == None or value < path_v:
                        value = path_v
    
    return value
    

def do_min(board,isWhite,threshold,level,maximum):
    if level >= maximum:
        return count_points(board,isWhite)

    value = None
    for target_x in range(0,8):
        for target_y in range(0,8):

            for initial_x in range(0,8):
                for initial_y in range(0,8):
                    
                    if board[initial_x][initial_y] == None:
                        continue
                    
                    
                    piece = board[initial_x][initial_y]

                    if piece.isWhite == isWhite:
                            continue
                    
                    origin = [initial_x,initial_y]
                    target = [target_x, target_y]
                    
                    if not piece.valid_move(board,origin,target):
                        continue 
                    
                    board_c = copy_board(board)
                    move_piece(board_c,origin,target)
                    path_v = do_max(board_c,isWhite,(1000000 if value == None else value),level + 1, maximum)
                    
                    if path_v < threshold and  level > 1:
                        return path_v
                        
                    if value == None or value > path_v:
                        value = path_v
    
    return value


def count_points(board,isWhite):

    multiplier = [
        [0.0] * 8,
        [0.0] * 8,
        [0.0] * 8,
        [0.0,0.0,0.1,0.2,0.2,0.1,0.0,0.0],
        [0.0,0.0,0.1,0.2,0.2,0.1,0.0,0.0],
        [0.0] * 8,
        [0.0] * 8,
        [0.0] * 8
    ]

    points = 0.0

    for i in range(0,8):
        for j in range(0,8):
            piece = board[i][j]
            if piece == None: 
                continue

            elif piece.isWhite != isWhite:
                 points -= (piece.points + multiplier[i][j] * piece.points)

            else:
                points += (piece.points + multiplier[i][j] * piece.points)
    
    return points   

def print_board(board):
    b = ''

    for row in board:
        for piece in row:
            if piece == None:
                b += ' _'
            else:
                b += ' ' + piece.initial
        b += '\n'
    
    print(b)


