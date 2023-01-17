import pygame
import Board


class PVPWindow: #Player vs Player

    def __init__(self):
        self.ChessBoard = Board.Board()  #note! for now all the coordinates are NOT multiplied by 100 to be scaled properly
        self.circleImage = pygame.image.load('Images/greenCircle-rbg.png')
        self.create()


    def create(self):

        pieceSelected = False
        previousMX = 0
        previousMY = 0

        pygame.init()

        icon = pygame.image.load('chessIcon.png')

        gameWindow = pygame.display.set_mode((800,800))
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
                    if(self.ChessBoard.board[int(mx/100)][ int(my/100)] != 0): #if a chess piece is selected
                        if pieceSelected == False: #if a chess piece was not already selected
                            pieceSelected = True
                            self.displayAvailableMovements(gameWindow, self.ChessBoard.board[int(mx/100)][ int(my/100)], (int(mx/100),int(my/100)))

                        elif int(previousMX/100) == int(pygame.mouse.get_pos()[0]/100) and int(previousMY/100) == int(pygame.mouse.get_pos()[1]/100): #if the selected piece is the same as the previously selected piece
                            pieceSelected = False
                            self.drawBoard(gameWindow)

                        else: #otherwise the selected piece is different from the previously selected piece
                            self.drawBoard(gameWindow)
                            self.displayAvailableMovements(gameWindow, self.ChessBoard.board[int(mx / 100)][int(my / 100)], (int(mx / 100), int(my / 100)))

                    elif pieceSelected:  #if a piece is selected, and then one of its possible moves is clicked, move the peice, Note: add turn checking
                        if (int(mx/100), int(my/100)) in self.ChessBoard.determinePossibleMoves(self.ChessBoard.board[int(previousMX/100)][int(previousMY/100)], (int(previousMX/100),int(previousMY/100))):   #if a piece is currently selected and one of its avaialbe moves is clicked
                            print("Time to move!")
                            self.ChessBoard.board[int(mx/100)][int(my/100)] = self.ChessBoard.board[int(previousMX/100)][int(previousMY/100)]
                            self.ChessBoard.board[int(previousMX/100)][int(previousMY/100)] = 0

                            pieceSelected = False
                            self.drawBoard(gameWindow)

                    if(self.ChessBoard.board[int(mx/100)][ int(my/100)] != 0):  #if a piece is clicked
                        previousMX = mx
                        previousMY = my





            pygame.display.update()  #update all visuals

        pygame.quit()


    def drawBoard(self, gameWindow):

        pygame.draw.rect(gameWindow, (193, 75, 31), (0, 0, 800, 800))  # draws the game board

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

