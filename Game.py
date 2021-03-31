import pygame
from pygame import (Rect)
from pygame.locals import (QUIT,MOUSEBUTTONUP)
from bot import Bot

class Game:
    def __init__(self,width,height,player,level):
        self.width = width
        self.height = height
        self.player = player
        self.pygame = pygame
        
        self.level = level

        self.pygame.init() #initializes pygame

        self.screen = pygame.display.set_mode((width,height)) #creates screen

        self.pygame.display.set_caption('Chess Bot') #puts name

        self.font = pygame.font.Font('freesansbold.ttf', 32) #saves font
        
        icon = self.pygame.image.load('chess.png')  #loads image
        self.pygame.display.set_icon(icon) #sets image

        self.make_pieces() 
        part = int(height * 0.1) #defines pieces
        self.part = part #sets part
        self.define_board_specs() 
        
        self.define_square_specs()

    def make_pieces(self): #puts pieces on a matrix
        pieces = 'R N B K Q B N R'.split(' ')
        pawns = ['p'] * 8
        
        def make_obj(values, id,color):
            obj = []
            for i in range(0,8):
                obj.append(
                    {
                        'piece': values[i],
                        'color': color,
                        id: id + i
                    }
                )
            
            return obj
        
        self.pieces = [
            make_obj(pieces,1,(200,200,200)),
            make_obj(pawns,9,(200,200,200)),
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            make_obj(pawns,17,(50,50,50)),
            make_obj(pieces,25,(50,50,50))
        ]


    def define_board_specs(self): #defines parameters to render the board
        part = self.part
        self.board_specs = {
            'top': part,
            'left': (self.width - 8*part) / 2,
            'width': 8 * part,
            'height': 8 * part
        }
    

    def define_square_specs(self): #defines paremeters to make each square on the board
        top = self.board_specs['top']
        left = self.board_specs['left']
        part = self.part
        self.square_specs = []
        for i in range(0,8):
            row = []
            for j in range(0,8):
                row.append({
                    'top': top + part*i,
                    'left': left + part*j,
                    'center': (left + part*j + 0.5*part,top + part*i + 0.5*part)
                })
            self.square_specs.append(row)
    

    def make_board(self): #makes the board
        board = self.board_specs
        border_w = 5
        self.screen.fill((255,255,255))
        self.pygame.draw.rect(self.screen,(89, 47, 5),Rect(board['left'] - border_w,board['top'] - border_w,board['width'] + border_w * 2,board['height'] + border_w * 2))
        self.pygame.draw.rect(self.screen,(0,0,0),Rect(board['left'],board['top'],board['width'],board['height']))
        n = 0
        for row in self.square_specs:
            for sq in row:
                if n %2 == 0:
                    self.pygame.draw.rect(self.screen,(255,255,255),Rect(sq['left'],sq['top'],self.part,self.part))
                n+=1
            n+=1
    

    def insert_piece(self,obj,center): #puts a piece according to paremeters
        font = self.font
        text = font.render(obj['piece'], True, obj['color'], None)
        textRect = text.get_rect()
        textRect.center = center
        self.screen.blit(text, textRect)



    def put_pieces(self): #defines which pieces go where
        for i in range(0,8):
            for j in range(0,8):
                if self.pieces[i][j] != None:
                    self.insert_piece(self.pieces[i][j], self.square_specs[i][j]['center'])
                    
    
    def move_piece(self,origin, destiny): #moves a piece from one place to another
        piece = self.pieces[origin[0]][origin[1]]
        self.pieces[origin[0]][origin[1]] = None
        self.pieces[destiny[0]][destiny[1]] = piece
    
    def detect_square(self,position):
        pos_x = int((position[1] - self.board_specs['top']) / self.part)
        pos_y = int((position[0] - self.board_specs['left']) / self.part)

        return pos_x,pos_y
    
    def run(self): #loop function to run the game

        running = True
        origin = None
        turn = 'white'

        bot = Bot('black' if self.player == 'white' else 'white',self.level) #creates bot

        while running:
            
            self.make_board()
            self.put_pieces()
            self.pygame.display.update()

            if turn != self.player: #bot move
                choice = bot.choose_move() #choose move
                self.move_piece(choice['origin'],choice['target']) #do move
                turn = 'white' if turn == 'black' else 'black'

            for event in self.pygame.event.get(): #Quit event
                if event.type == QUIT:
                    running = False
                    
                
                if self.player == turn: #player move
                    if event.type == MOUSEBUTTONUP:

                        pos = pygame.mouse.get_pos()
                        pos = self.detect_square(pos) 

                        if origin == None:
                            origin = pos

                        else:
                            turn = 'white' if turn == 'black' else 'black'
                            self.move_piece(origin,pos)
                            bot.opponent_move(origin,pos)
                            origin = None
                         


