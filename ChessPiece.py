import pygame

class ChessPiece:


    def __init__(self,type, team):
        self.type = type #PAWN, BISHIP, KNIGHT, ROOK, QUEEN, KING
        self.team = team #white or black
        self.isDead = False
        self.hasMoved = False

    def __str__(self):
        return self.type + " "+ self.team[0]

    def __repr__(self):
        return self.__str__()