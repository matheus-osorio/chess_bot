def get_piece(board,coordenates): #gets piece from board
    return board[coordenates[0]][coordenates[1]]

#---------------------------------------------

def enemy_or_empty(piece, isWhite): #is None or opponent
    return piece == None or piece.isWhite != isWhite

#---------------------------------------------

def get_diff(origin,target): #gets how many squares is the move
    return target[0] - origin[0] ,target[1] - origin[1]

#---------------------------------------------

def diff_is_Zero(diff): #checks if there is any move
    return diff[0] == 0 and diff[1] == 0

#---------------------------------------------

def same_line(diff): #checks if the move is a line
    return min( abs(diff[0]), abs(diff[1]) ) == 0

#---------------------------------------------

def get_straight_path(board,origin,diff): #gets a path from a straight line

    if not diff[0]:
        if diff[1] < 0:
            start = origin[1] + diff[1]
            end = origin[1] + 1
        
        else:
            start = origin[1]
            end = origin[1] + diff[1] + 1
        return board[origin[0]][start:end]
    
    if diff[0] < 0:
            start = origin[0] + diff[0]
            end = origin[0] + 1
        
    else:
        start = origin[0]
        end = origin[0] + diff[0] + 1

    return [ row[origin[1]] for row in board[start:end]] 

#---------------------------------------------

def same_diagonal(diff): #checks if the move is a diagonal
    if abs(diff[0]) == abs(diff[1]):
        return True

    return False

#---------------------------------------------

def get_diagonal_path(board,origin,destiny,diff): #gets a diagonal path
    
    path = []
    x = origin[0]
    y = origin[1]
    x_dir = int(diff[0]/abs(diff[0]))
    y_dir = int(diff[1]/abs(diff[1]))

    while(x != destiny[0] + x_dir and y != destiny[1] + y_dir):
        path.append(board[x][y])
        x+= x_dir
        y+= y_dir
    return path

#---------------------------------------------

def same_length(arr1, arr2): #checks if 2 arrays have the same length
    return len(arr1) == len(arr2)

#---------------------------------------------

def move_in_board(matrix):
    def inside(move):
        return (0 <= move[0] < 8) and (0 <= move[1] < 8)
    moves = []
    for line in matrix:
        moves.append(
            [move for move in line if inside(move)]
        )
    
    return moves

