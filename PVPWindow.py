import pygame
import Board


class PVPWindow: #Player vs Player

    def __init__(self):
        self.ChessBoard = Board.Board()  #note! for now all the coordinates are NOT multiplied by 100 to be scaled properly
        self.circleImage = pygame.image.load('Images/greenCircle-rbg.png')
        self.isWhiteTurn = True
        self.create()


    def create(self):

        pieceSelected = False
        previousMX = 0
        previousMY = 0


        pygame.init()

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mx < 800:  #if the click is on the chess board
                        if(self.ChessBoard.board[int(mx/100)][ int(my/100)] != 0) and not pieceSelected: #if a chess piece is selected
                            if (self.ChessBoard.board[int(mx/100)][ int(my/100)].team == 'white' and self.isWhiteTurn) or ((self.ChessBoard.board[int(mx/100)][ int(my/100)].team == 'black' and (not self.isWhiteTurn))):  #checks if the selected piece is the same team as the current turn
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
                                self.ChessBoard.board[int(mx/100)][int(my/100)] = self.ChessBoard.board[int(previousMX/100)][int(previousMY/100)]
                                self.ChessBoard.board[int(previousMX/100)][int(previousMY/100)] = 0

                                self.isWhiteTurn = not self.isWhiteTurn  #switches turn when a move is made
                                pieceSelected = False
                                self.drawBoard(gameWindow)


                        if(self.ChessBoard.board[int(mx/100)][ int(my/100)] != 0):  #if a piece is clicked
                            previousMX = mx
                            previousMY = my

                    else:
                        pass #write menu button click code here



            pygame.display.update()  #update all visuals

        pygame.quit()


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
        pygame.draw.rect(gameWindow, (106, 121, 248), (875, 675, 150, 75), 250 ,3)  # draws Reset Game button

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
                    gameWindow.blit(self.ChessBoard.board[j][i].image, (j * 100, i * 100))


    def displayAvailableMovements(self, gameWindow, piece, coordinate):

        for location in self.ChessBoard.determinePossibleMoves(piece, coordinate): #This will return a list of all coordinates where a move is possible
            gameWindow.blit(self.circleImage, (location[0]*100, location[1]*100))

