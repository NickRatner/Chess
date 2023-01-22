import pygame
import Board
import PySimpleGUI as sg
from copy import deepcopy

class PVPWindow: #Player vs Player

    def __init__(self):
        pygame.display.init()
        if not pygame.get_init():
            pygame.init()
        self.ChessBoard = Board.Board()
        self.circleImage = pygame.image.load('Images/greenCircle-rbg.png')
        self.redCircleImage = pygame.image.load('Images/redCircle-rbg.png')
        self.isWhiteTurn = True

        #tempBoard = self.ChessBoard.board.copy()
        self.states = []
        self.states.append(deepcopy(self.ChessBoard.board))

        self.create()


    def create(self):
        pieceSelected = False
        previousMX = 0
        previousMY = 0

        icon = pygame.image.load('chessIcon.png')

        gameWindow = pygame.display.set_mode((1100,800))
        pygame.display.set_caption("PvP Chess")
        pygame.display.set_icon(icon)

        self.drawBoard(gameWindow)


        pygame.display.update()  # update all visuals


        running = True
        while running: #game loop
            for event in pygame.event.get(): #exits game loop when window is closed
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mx < 800:  #if the click is on the chess board
                        if (self.ChessBoard.board[int(mx / 100)][int(my / 100)] != 0):

                            if(self.ChessBoard.board[int(mx/100)][ int(my/100)].team == 'white' and self.isWhiteTurn) or ((self.ChessBoard.board[int(mx/100)][ int(my/100)].team == 'black' and (not self.isWhiteTurn))): #if a chess piece is selected, and if the selected piece is the same team as the current turn
                                if pieceSelected == False: #if a chess piece was not already selected
                                    pieceSelected = True
                                    self.displayAvailableMovements(gameWindow, self.ChessBoard.board[int(mx/100)][ int(my/100)], (int(mx/100),int(my/100)))

                                elif int(previousMX/100) == int(pygame.mouse.get_pos()[0]/100) and int(previousMY/100) == int(pygame.mouse.get_pos()[1]/100): #if the selected piece is the same as the previously selected piece
                                    pieceSelected = False
                                    self.drawBoard(gameWindow)

                                else: #otherwise the selected piece is different from the previously selected piece
                                    self.drawBoard(gameWindow)
                                    self.displayAvailableMovements(gameWindow, self.ChessBoard.board[int(mx / 100)][int(my / 100)], (int(mx / 100), int(my / 100)))

                        elif pieceSelected:  #if a piece is selected, and then one of its possible moves is clicked, move the peice
                            if (int(mx/100), int(my/100)) in self.ChessBoard.determinePossibleMoves(self.ChessBoard.board[int(previousMX/100)][int(previousMY/100)], (int(previousMX/100),int(previousMY/100))):   #if a piece is currently selected and one of its avaialbe moves is clicked
                                #print(self.states[0])
                                self.ChessBoard.board[int(mx/100)][int(my/100)] = self.ChessBoard.board[int(previousMX/100)][int(previousMY/100)]  #move the piece to a new spot
                                self.ChessBoard.board[int(previousMX/100)][int(previousMY/100)] = 0  #set the piece's old spot to empty (0)

                                self.changeTurn()  #switches turn when a move is made
                                pieceSelected = False

                                if self.ChessBoard.board[int(mx/100)][int(my/100)].type == 'PAWN' and self.ChessBoard.board[int(mx/100)][int(my/100)].team == 'white' and int(my/100) == 0:
                                    self.ChessBoard.transformPawn((int(mx/100),int(my/100)))

                                elif self.ChessBoard.board[int(mx/100)][int(my/100)].type == 'PAWN' and self.ChessBoard.board[int(mx/100)][int(my/100)].team == 'black' and int(my/100) == 7:
                                    self.ChessBoard.transformPawn((int(mx/100),int(my/100)))

                                self.states.append(deepcopy(self.ChessBoard.board))  # pushes the current state of the board to the stack

                                self.drawBoard(gameWindow)


                        if (self.ChessBoard.board[int(mx/100)][int(my/100)] != 0) and (self.ChessBoard.board[int(previousMX/100)][int(previousMY/100)] != 0):
                            if pieceSelected and (self.ChessBoard.board[int(mx / 100)][int(my / 100)].team == 'white' and (not self.isWhiteTurn)) or ((self.ChessBoard.board[int(mx / 100)][int(my / 100)].team == 'black' and self.isWhiteTurn)):   #if the piece clicked is the opposite team of the piece selected
                                if (int(mx / 100), int(my / 100)) in self.ChessBoard.determinePossibleMoves(self.ChessBoard.board[int(previousMX / 100)][int(previousMY / 100)],(int(previousMX / 100), int(previousMY / 100))): #if a piece is selected and one of its available moves is clicked

                                    self.ChessBoard.board[int(mx / 100)][int(my / 100)] = self.ChessBoard.board[int(previousMX / 100)][int(previousMY / 100)] #moves the piece to a new spot
                                    self.ChessBoard.board[int(previousMX / 100)][int(previousMY / 100)] = 0  # set the piece's old spot to empty (0)

                                    self.changeTurn()  #switches turns
                                    pieceSelected = False

                                    if self.ChessBoard.board[int(mx / 100)][int(my / 100)].type == 'PAWN' and \
                                            self.ChessBoard.board[int(mx / 100)][int(my / 100)].team == 'white' and int(
                                            my / 100) == 0:
                                        self.ChessBoard.transformPawn((int(mx / 100), int(my / 100)))

                                    elif self.ChessBoard.board[int(mx / 100)][int(my / 100)].type == 'PAWN' and \
                                            self.ChessBoard.board[int(mx / 100)][int(my / 100)].team == 'black' and int(
                                            my / 100) == 7:
                                        self.ChessBoard.transformPawn((int(mx / 100), int(my / 100)))


                                    self.states.append(deepcopy(self.ChessBoard.board))  # pushes the current state of the board to the stack

                                    self.drawBoard(gameWindow)

                        if(self.ChessBoard.board[int(mx/100)][ int(my/100)] != 0):  #if a piece is clicked
                            previousMX = mx
                            previousMY = my

                    else:
                        if mx > 875 and mx < 1025:  #a button is pressed (this checks x coordinate)
                            if my > 675 and my < 750: #reset game button is pressed (this checks y coordinate)
                                self.resetGame()   #CAUSES ERROR, FIX
                                running = False
                            if my > 525 and my < 600:  #surrender button is pressed
                                self.surrender()
                                running = False


                            if my > 375 and my < 450:  #undo move button pressed
                                self.undoMove(gameWindow)
            if running:
                pygame.display.update()  #update all visuals
        pygame.display.quit()


    def drawBoard(self, gameWindow):

        if self.isWhiteTurn:  #sets turn text to whatever turn it currently is
            currentTurn = 'White'
        else:
            currentTurn = 'Black'

        pygame.draw.rect(gameWindow, (242, 214, 205), (800, 0, 300, 800))  #draws the side menu background
        pygame.draw.line(gameWindow, (0,0,0), (800,0), (800,1100), width=5)

        pygame.draw.rect(gameWindow, (106, 121, 248), (875, 100, 150, 75), 250 ,3) #draws Turn Indicator
        pygame.draw.rect(gameWindow, (106, 121, 248), (875, 375, 150, 75), 250 ,3)  # draws Undo Move button
        pygame.draw.rect(gameWindow, (106, 121, 248), (875, 525, 150, 75), 250 ,3)  # draws Surrender button
        pygame.draw.rect(gameWindow, (106, 121, 248), (875, 675, 150, 75), 250 ,3)  # draws undo Game button

        font = pygame.font.Font('freesansbold.ttf', 20)  #creating the text for the buttons

        turnIndicatorText = font.render('Turn:', True, (255,255,255))
        currentTurnText = font.render(currentTurn, True, (255,255,255))
        undoMovetext = font.render('Undo Move', True, (255,255,255))
        surrenderText = font.render('Surrender', True, (255,255,255))
        resetGameText = font.render('Reset Game', True, (255,255,255))

        turnIndicatorTextRect = turnIndicatorText.get_rect()
        currentTurnTextRect = turnIndicatorText.get_rect()
        undoMovetextRect = undoMovetext.get_rect()
        surrenderTextRect = surrenderText.get_rect()
        resetGameTextRect = resetGameText.get_rect()

        turnIndicatorTextRect.center = (910 , 137.5)
        currentTurnTextRect.center = (970, 137.5)
        undoMovetextRect.center = (950 , 412.5)
        surrenderTextRect.center = (950 , 562.5)
        resetGameTextRect.center = (950 , 712.5)

        gameWindow.blit(turnIndicatorText, turnIndicatorTextRect)
        gameWindow.blit(currentTurnText, currentTurnTextRect)
        gameWindow.blit(undoMovetext, undoMovetextRect)
        gameWindow.blit(surrenderText, surrenderTextRect)
        gameWindow.blit(resetGameText, resetGameTextRect)



        pygame.draw.rect(gameWindow, (193, 75, 31), (0, 0, 800, 800))  # draws the chess board background

        for i in range(8):  # this loop draws all the light colored rectangles on the board
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        pygame.draw.rect(gameWindow, (225, 198, 153), (j * 100, i * 100, 100, 100))
                elif i % 2 != 0:
                    if j % 2 != 0:
                        pygame.draw.rect(gameWindow, (225, 198, 153), (j * 100, i * 100, 100, 100))

        for i in range(8): #this loop draws all the chess pieces
            for j in range(8):
                if self.ChessBoard.board[j][i] != 0:

                    if self.ChessBoard.board[j][i].team == "white":
                        if self.ChessBoard.board[j][i].type == "PAWN":
                            image = pygame.image.load('Images/WhitePawnIcon-rbg.png')
                        elif self.ChessBoard.board[j][i].type == "BISHOP":
                            image = pygame.image.load('Images/WhiteBishopIcon-rbg.png')
                        elif self.ChessBoard.board[j][i].type == "KNIGHT":
                            image = pygame.image.load('Images/WhiteKnightIcon-rbg.png')
                        elif self.ChessBoard.board[j][i].type == "ROOK":
                            image = pygame.image.load('Images/WhiteRookIcon-rbg.png')
                        elif self.ChessBoard.board[j][i].type == "QUEEN":
                            image = pygame.image.load('Images/WhiteQueenIcon-rbg.png')
                        elif self.ChessBoard.board[j][i].type == "KING":
                            image = pygame.image.load('Images/WhiteKingIcon-rbg.png')

                    if self.ChessBoard.board[j][i].team == "black":
                        if self.ChessBoard.board[j][i].type == "PAWN":
                            image = pygame.image.load('Images/BlackPawnIcon-rbg.png')
                        elif self.ChessBoard.board[j][i].type == "BISHOP":
                            image = pygame.image.load('Images/BlackBishopIcon-rbg.png')
                        elif self.ChessBoard.board[j][i].type == "KNIGHT":
                            image = pygame.image.load('Images/BlackKnightIcon-rbg.png')
                        elif self.ChessBoard.board[j][i].type == "ROOK":
                            image = pygame.image.load('Images/BlackRookIcon-rbg.png')
                        elif self.ChessBoard.board[j][i].type == "QUEEN":
                            image = pygame.image.load('Images/BlackQueenIcon-rbg.png')
                        elif self.ChessBoard.board[j][i].type == "KING":
                            image = pygame.image.load('Images/BlackKingIcon-rbg.png')

                    gameWindow.blit(image, (j * 100, i * 100))


    def displayAvailableMovements(self, gameWindow, piece, coordinate):

        for location in self.ChessBoard.determinePossibleMoves(piece, coordinate): #This will return a list of all coordinates where a move is possible
            gameWindow.blit(self.circleImage, (location[0]*100, location[1]*100))

        for location in self.ChessBoard.determinePossibleCaputures(piece, coordinate): #This will return a list of all coordinates where a move is possible
            gameWindow.blit(self.redCircleImage, (location[0]*100, location[1]*100))


    def changeTurn(self):
        self.isWhiteTurn = not self.isWhiteTurn

    def resetGame(self):
        self.__init__()

    def surrender(self):
        self.endGame()

    def undoMove(self, gameWindow):

        if len(self.states) > 1:  #if there is a move to undo
            self.changeTurn()
            self.states.pop(-1)   #pops the last state of the board

        for i in self.states:
            print(i)
            print('==============================')

        self.ChessBoard.board = self.states[-1]  #sets the state of the board to the new most recent state

        self.drawBoard(gameWindow)   #redraws (updates) the board


    def endGame(self):
        sg.theme("LightGreen4")

        if self.isWhiteTurn:  #this means black made the last move, hence black wins
            winner = "Black"
        else:
            winner = 'White'

        layout = [
            [sg.Text("Game Over!")],
            [sg.Text('Winner: ' + winner)],
            [sg.Button("Play Again")],
            [sg.Button("Exit")]   #EXIT BUTTON DOES NOT WORK
        ]

        gameOverScreen = sg.Window("Chess", layout, size=(500, 300), margins=(0, 75), element_justification="center")

        while True:
            event, values = gameOverScreen.read()

            if event == "Exit" or event == sg.WIN_CLOSED:
                gameOverScreen.close()
                pygame.quit()

                break

            if event == "Play Again":
                gameOverScreen.close()
                self.resetGame()
                break