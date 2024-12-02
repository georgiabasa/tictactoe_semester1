import pygame
import random
import tkinter as tk

# Creating the board and uploading the images
pygame.init()
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Tic-Tac-Toe")
x = pygame.image.load('cancel.png')
o = pygame.image.load('circle-ring.png')
symbols=[x,o]
p_values=[1,2]
icon = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)

class Handler():  # creates the tkinter window
    def __init__(self, root, screen, x, o):
        self.screen = screen
        self.x = x
        self.o = o
        self.root = root
        self.root.title('Tic tac toe')
        self.root.resizable(False, False)
        self.root.geometry('500x500')
        self.mywidgets()

    def mywidgets(self): #creates the widgets 
        f=tk.Frame(root,bg='#7fa99b')
        f.pack(expand=1,fill='both')
        l=tk.Label(f,text='Welcome, would you like to play \n Single Player or Multiplayer? \n\n Press Space to Play Again \n\n Press x on the tic-tac-toe window to re-select Game mode \n\n Press Exit to Exit the Game',\
                   bg='#16697a',font=('Times',13))
        l.pack(expand=1,fill='both')
        b=tk.Button(f,text='Single Player',bg='#db6400',font=('Times',13), command=self.single_player)
        b.pack(expand=1,fill='x')
        b2=tk.Button(f,text='Multiplayer',bg='#ffa62b',font=('Times',13), command=self.multiplayer)
        b2.pack(expand=1,fill='x')
        b3=tk.Button(f,text='Exit',bg='#ffa62b',font=('Times',13), command=self.destroy_window)
        b3.pack(expand=1,fill='x')

    def single_player(self): #καλεί την κλάση ΑΙ 
        AI(screen, x, o)

    def multiplayer(self): #καλεί την κλάση Game 
        Game(screen, x, o)

    def destroy_window(self): #κλείνει τα παράθυρα των tkinter και pygame 
        pygame.quit()
        self.root.destroy()
        


class TicTacToe():
#Αυτή η κλάση περιέχει τις κοινές μεθόδους των AI και Game (μητρική κλάση)
    def square_maker(self):  # Creating the squares
        self.first = pygame.draw.rect(self.screen, (192, 192, 192), (43, 30, 180, 180))
        self.second = pygame.draw.rect(self.screen, (192, 192, 192), (288, 30, 180, 180))
        self.third = pygame.draw.rect(self.screen, (192, 192, 192), (533, 30, 180, 180))
        self.fourth = pygame.draw.rect(self.screen, (192, 192, 192), (43, 275, 180, 180))
        self.fifth = pygame.draw.rect(self.screen, (192, 192, 192), (288, 275, 180, 180))
        self.sixth = pygame.draw.rect(self.screen, (192, 192, 192), (533, 275, 180, 180))
        self.seventh = pygame.draw.rect(self.screen, (192, 192, 192), (43, 520, 180, 180))
        self.eighth = pygame.draw.rect(self.screen, (192, 192, 192), (288, 520, 180, 180))
        self.ninth = pygame.draw.rect(self.screen, (192, 192, 192), (533, 520, 180, 180))

    def open_positions(self):  # Defining the booleans that determine if a block is open to play or not
        self.first_open = True
        self.second_open = True
        self.third_open = True
        self.fourth_open = True
        self.fifth_open = True
        self.sixth_open = True
        self.seventh_open = True
        self.eighth_open = True
        self.ninth_open = True

    def win_check(self, num): #Ελέγχει αν έχει κερδίσει κάποιος από τους δύο παίκτες 
        for row in self.board:
            for tile in row:
                if tile == num:
                    continue
                else:
                    break
            else:
                return True

        for column in range(3):
            for row in self.board:
                if row[column] == num:
                    continue
                else:
                    break
            else:
                return True

        for tile in range(3):
            if self.board[tile][tile] == num:
                continue
            else:
                break
        else:
            return True

        for tile in range(3):
            if self.board[tile][2 - tile] == num:
                continue
            else:
                break
        else:
            return True

        return False 
    
    def draw_line(self):  # This is a function that draws a line according to whoever won the game and which win condition did they meet
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == 1 or self.board[0][0] == self.board[0][1] == self.board[0][2] == 2:
            pygame.draw.line(self.screen, (0, 0, 0), (30, 120), (720, 120), 10)
        if self.board[1][0] == self.board[1][1] == self.board[1][2] == 1 or self.board[1][0] == self.board[1][1] == self.board[1][2] == 2:
            pygame.draw.line(self.screen, (0, 0, 0), (30, 365), (720, 365), 10)
        if self.board[2][0] == self.board[2][1] == self.board[2][2] == 1 or self.board[2][0] == self.board[2][1] == self.board[2][2] == 2:
            pygame.draw.line(self.screen, (0, 0, 0), (30, 610), (720, 610), 10)
        if self.board[0][0] == self.board[1][0] == self.board[2][0] == 1 or self.board[0][0] == self.board[1][0] == self.board[2][0] == 2:
            pygame.draw.line(self.screen, (0, 0, 0), (132, 30), (132, 720), 10)
        if self.board[0][1] == self.board[1][1] == self.board[2][1] == 1 or self.board[0][1] == self.board[1][1] == self.board[2][1] == 2:
            pygame.draw.line(self.screen, (0, 0, 0), (378, 30), (378, 720), 10)
        if self.board[0][2] == self.board[1][2] == self.board[2][2] == 1 or self.board[0][2] == self.board[1][2] == self.board[2][2] == 2:
            pygame.draw.line(self.screen, (0, 0, 0), (623, 30), (623, 720), 10)
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 1 or self.board[0][0] == self.board[1][1] == self.board[2][2] == 2:
            pygame.draw.line(self.screen, (0, 0, 0), (35, 25), (713, 700), 10)
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == 1 or self.board[0][2] == self.board[1][1] == self.board[2][0] == 2:
            pygame.draw.line(self.screen, (0, 0, 0), (35, 705), (713, 25), 10)

###############################################################################  

class AI(TicTacToe):  # Creating the class of the AI Game
    def __init__(self, screen, x, o):
        self.screen = screen
        self.x = x
        self.o = o
        self.square_maker()
        self.game = True
        self.won = False
        self.run = True
        self.open_positions()
        self.starting_status()
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.runner()

    def starting_status(self):# A function that contains the status of the game at the start
        self.current_player = 1
        self.font = pygame.font.Font('freesansbold.ttf', 26)
        self.text = self.font.render("It's your turn.", True, (215, 236, 255))
        self.textRect = self.text.get_rect()
        self.screen.blit(self.text, self.textRect)
        self.rects = {"first": (70, 55), "second": (315, 55), "third": (560, 55), "fourth": (70, 300),
                      "fifth": (315, 300),
                      "sixth": (560, 300), "seventh": (70, 545), "eighth": (315, 545), "ninth": (560, 545)}


    def draw_symbol(self, pos):  # Function that draws x in the selected square and deletes the same square from the dictionary
        if not self.won and self.game:
            if self.current_player == 1:
                if self.first.collidepoint(pos) and self.first_open:
                    screen.blit(x, (70, 55))
                    self.board[0][0] = 1
                    del self.rects["first"]
                    self.first_open = False
                    return True
                if self.second.collidepoint(pos) and self.second_open:
                    screen.blit(x, (315, 55))
                    self.board[0][1] = 1
                    del self.rects["second"]
                    self.second_open = False
                    return True
                if self.third.collidepoint(pos) and self.third_open:
                    screen.blit(x, (560, 55))
                    self.board[0][2] = 1
                    del self.rects["third"]
                    self.third_open = False
                    return True
                if self.fourth.collidepoint(pos) and self.fourth_open:
                    screen.blit(x, (70, 300))
                    self.board[1][0] = 1
                    del self.rects["fourth"]
                    self.fourth_open = False
                    return True
                if self.fifth.collidepoint(pos) and self.fifth_open:
                    screen.blit(x, (315, 300))
                    self.board[1][1] = 1
                    del self.rects["fifth"]
                    self.fifth_open = False
                    return True
                if self.sixth.collidepoint(pos) and self.sixth_open:
                    screen.blit(x, (560, 300))
                    self.board[1][2] = 1
                    del self.rects["sixth"]
                    self.sixth_open = False
                    return True
                if self.seventh.collidepoint(pos) and self.seventh_open:
                    screen.blit(x, (70, 545))
                    self.board[2][0] = 1
                    del self.rects["seventh"]
                    self.seventh_open = False
                    return True
                if self.eighth.collidepoint(pos) and self.eighth_open:
                    screen.blit(x, (315, 545))
                    self.board[2][1] = 1
                    del self.rects["eighth"]
                    self.eighth_open = False
                    return True
                if self.ninth.collidepoint(pos) and self.ninth_open:
                    screen.blit(x, (560, 545))
                    self.board[2][2] = 1
                    del self.rects["ninth"]
                    self.ninth_open = False
                    return True
                return False
        

    def computer_bool_changer(self, key):
        if str(key) == "first":
            self.first_open = False
        elif key == "second":
            self.second_open = False
        elif key == "third":
            self.third_open = False
        elif key == "fourth":
            self.fourth_open = False
        elif key == "fifth":
            self.fifth_open = False
        elif key == "sixth":
            self.sixth_open = False
        elif key == "seventh":
            self.seventh_open = False
        elif key == "eighth":
            self.eighth_open = False
        elif key == "ninth":
            self.ninth_open = False

    def computer_move(self, player):
        if self.game and not self.won:
            if player == 2:
                self.list_square = [x for x in self.rects.keys()]
                if len(self.list_square) == 0:
                    self.game = False
                    pass
                else:
                    i = random.choice(self.list_square)
                    self.screen.blit(o, self.rects[i])
                    self.board_adder(i)
                    self.computer_bool_changer(i)
                    self.current_player = 1
                    del self.rects[i]

    def board_adder(self, key):
        if str(key) == "first":
            self.board[0][0] = 2
        elif key == "second":
            self.board[0][1] = 2
        elif key == "third":
            self.board[0][2] = 2
        elif key == "fourth":
            self.board[1][0] = 2
        elif key == "fifth":
            self.board[1][1] = 2
        elif key == "sixth":
            self.board[1][2] = 2
        elif key == "seventh":
            self.board[2][0] = 2
        elif key == "eighth":
            self.board[2][1] = 2
        elif key == "ninth":
            self.board[2][2] = 2

    def check(self):
        if self.win_check(1):
            self.won = True
            self.game = False
            self.screen.fill((0, 0, 0), (0, 0, 750, 30))
            self.text = self.font.render('You won!', True, (215, 236, 255))
            self.screen.blit(self.text, self.textRect)
            self.draw_line()
        if self.win_check(2):
            self.won = True
            self.game = False
            self.screen.fill((0, 0, 0), (0, 0, 750, 30))
            self.text = self.font.render('Computer has won.', True, (215, 236, 255))
            self.screen.blit(self.text, self.textRect)
            self.draw_line()
        if 0 not in self.board[0] and 0 not in self.board[1] and 0 not in self.board[2] and not self.win_check(1) and not self.win_check(2):
            self.screen.fill((0, 0, 0), (0, 0, 750, 30))
            self.text = self.font.render("It's a tie!", True, (215, 236, 255))
            self.screen.blit(self.text, self.textRect)

    def runner(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen.fill((0, 0, 0), (0, 0, 750, 30))
                    self.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game = True
                        self.won = False
                        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        self.screen.fill((0, 0, 0), (0, 0, 750, 750))
                        self.starting_status()
                        self.open_positions()
                        self.square_maker()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.draw_symbol(pos):
                        self.check()
                        self.computer_move(2)
                        self.check()

            pygame.display.update()
##################################################################################
# Creating the class of the 2 players game
class Game(TicTacToe):
    def __init__(self, screen, x, o):  # The variables used in the class
        self.screen = screen
        self.x = x
        self.o = o
        self.square_maker()
        self.starting_status()
        self.game = True
        self.won = False
        self.run = True
        self.open_positions()
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.cell_rects = {"first":self.first,"second": self.second,"third": self.third,"fourth": self.fourth,"fifth": self.fifth,\
                           "sixth":self.sixth,"seventh": self.seventh,"eighth":self.eighth,"ninth": self.ninth}
        self.rect_info = {"first": [(70, 55),(0,0)], "second": [(315, 55),(0,1)], "third": [(560, 55),(0,2)],
                      "fourth": [(70, 300),(1,0)], "fifth": [(315, 300),(1,1)], "sixth": [(560, 300),(1,2)],
                      "seventh": [(70, 545),(2,0)], "eighth": [(315, 545),(2,1)], "ninth": [(560, 545),(2,2)]}
        self.init_list_open()
        self.runner()

    def init_list_open(self):
        self.rects_open = {"first": self.first_open, "second": self.second, "third": self.third_open,
                           "fourth": self.fourth_open, "fifth": self.fifth_open,
                           "sixth": self.sixth_open, "seventh": self.seventh_open, "eighth": self.eighth_open,
                           "ninth": self.ninth_open}

        

    def starting_status(self):  # A function that contains the status of the game at the start
        self.player = 0
        self.font = pygame.font.Font('freesansbold.ttf', 26)
        self.text = self.font.render("Player 1's turn", True, (215, 236, 255))
        self.textRect = self.text.get_rect()
        self.screen.blit(self.text, self.textRect)

    def switch_players(self):  # This function prints a different text according to which player is playing
        if self.player == 0:
            self.text = self.font.render("Player 2's turn.", True, (215, 236, 255), (0, 0, 0))
            self.textRect = self.text.get_rect()
            self.screen.blit(self.text, self.textRect)
            self.player = 1
        elif self.player == 1:
            self.text = self.font.render("Player 1's turn.", True, (215, 236, 255), (0, 0, 0))
            self.textRect = self.text.get_rect()
            self.screen.blit(self.text, self.textRect)
            self.player = 0


    def draw_mark(self, current_player,key):
        if not self.won:
            if self.rects_open.get(key):
                self.rects_open[key]= False
                self.screen.blit(symbols[current_player], self.rect_info.get(key)[0])
                board_pos = self.rect_info.get(key)[1]
                self.board[board_pos[0]][board_pos[1]] = p_values[current_player]

    def check(self):
        if self.win_check(1):
            self.won = True
            self.game = False
            self.screen.fill((0, 0, 0), (0, 0, 750, 30))
            self.text = self.font.render("Player 1 has won.", True, (215, 236, 255))
            self.screen.blit(self.text, self.textRect)
            self.draw_line()
        if self.win_check(2):
            self.won = True
            self.game = False
            self.screen.fill((0, 0, 0), (0, 0, 750, 30))
            self.text = self.font.render('Player 2 has won.', True, (215, 236, 255))
            self.screen.blit(self.text, self.textRect)
            self.draw_line()
        if 0 not in self.board[0] and 0 not in self.board[1] and 0 not in self.board[2] and not self.win_check(1) and not self.win_check(2):
            self.screen.fill((0, 0, 0), (0, 0, 750, 30))
            self.text = self.font.render("It's a tie!", True, (215, 236, 255))
            self.screen.blit(self.text, self.textRect)

    def runner(self):
        while self.run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen.fill((0, 0, 0), (0, 0, 750, 30))
                    self.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game = True
                        self.won = False
                        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        self.screen.fill((0, 0, 0), (0, 0, 750, 30))
                        self.starting_status()
                        self.open_positions()
                        self.init_list_open()                 
                        self.square_maker()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for cell in self.cell_rects:
                        if self.cell_rects.get(cell).collidepoint(pos) and self.game and self.rects_open.get(cell):
                            self.draw_mark(self.player, cell)
                            self.switch_players()
                            self.check()
                            break

            pygame.display.update()

root = tk.Tk()
root.title('Tic-Tac-Toe')
mygame = Handler(root, screen, x, o)
root.mainloop()
