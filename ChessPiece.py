import pygame

class ChessPiece:


    def __init__(self,type, team):
        self.type = type #PAWN, BISHIP, KNIGHT, ROOK, QUEEN, KING
        self.team = team #white or black
        self.isDead = False
        self.setImage()

    def __str__(self):
        return self.type + " "+ self.team[0]

    def __repr__(self):
        return self.__str__()

    def setImage(self):

        if self.team == "white":
            if self.type == "PAWN":
                self.image = pygame.image.load('Images/WhitePawnIcon-rbg.png')
            elif self.type == "BISHOP":
                self.image = pygame.image.load('Images/WhiteBishopIcon-rbg.png')
            elif self.type == "KNIGHT":
                self.image = pygame.image.load('Images/WhiteKnightIcon-rbg.png')
            elif self.type == "ROOK":
                self.image = pygame.image.load('Images/WhiteRookIcon-rbg.png')
            elif self.type == "QUEEN":
                self.image = pygame.image.load('Images/WhiteQueenIcon-rbg.png')
            elif self.type == "KING":
                self.image = pygame.image.load('Images/WhiteKingIcon-rbg.png')

        if self.team == "black":
            if self.type == "PAWN":
                self.image = pygame.image.load('Images/BlackPawnIcon-rbg.png')
            elif self.type == "BISHOP":
                self.image = pygame.image.load('Images/BlackBishopIcon-rbg.png')
            elif self.type == "KNIGHT":
                self.image = pygame.image.load('Images/BlackKnightIcon-rbg.png')
            elif self.type == "ROOK":
                self.image = pygame.image.load('Images/BlackRookIcon-rbg.png')
            elif self.type == "QUEEN":
                self.image = pygame.image.load('Images/BlackQueenIcon-rbg.png')
            elif self.type == "KING":
                self.image = pygame.image.load('Images/BlackKingIcon-rbg.png')