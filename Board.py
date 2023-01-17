import ChessPiece

class Board:

    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]

        self.board[0][1] = ChessPiece.ChessPiece("PAWN", "black")
        self.board[1][1] = ChessPiece.ChessPiece("PAWN", "black")
        self.board[2][1] = ChessPiece.ChessPiece("PAWN", "black")
        self.board[3][1] = ChessPiece.ChessPiece("PAWN", "black")
        self.board[4][1] = ChessPiece.ChessPiece("PAWN", "black")
        self.board[5][1] = ChessPiece.ChessPiece("PAWN", "black")
        self.board[6][1] = ChessPiece.ChessPiece("PAWN", "black")
        self.board[7][1] = ChessPiece.ChessPiece("PAWN", "black")

        self.board[1][0] = ChessPiece.ChessPiece("KNIGHT", "black")
        self.board[6][0] = ChessPiece.ChessPiece("KNIGHT", "black")
        self.board[2][0] = ChessPiece.ChessPiece("BISHOP", "black")
        self.board[5][0] = ChessPiece.ChessPiece("BISHOP", "black")
        self.board[0][0] = ChessPiece.ChessPiece("ROOK", "black")
        self.board[7][0] = ChessPiece.ChessPiece("ROOK", "black")

        self.board[3][0] = ChessPiece.ChessPiece("QUEEN", "black")
        self.board[4][0] = ChessPiece.ChessPiece("KING", "black")


        self.board[0][6] = ChessPiece.ChessPiece("PAWN", "white")
        self.board[1][6] = ChessPiece.ChessPiece("PAWN", "white")
        self.board[2][6] = ChessPiece.ChessPiece("PAWN", "white")
        self.board[3][6] = ChessPiece.ChessPiece("PAWN", "white")
        self.board[4][6] = ChessPiece.ChessPiece("PAWN", "white")
        self.board[5][6] = ChessPiece.ChessPiece("PAWN", "white")
        self.board[6][6] = ChessPiece.ChessPiece("PAWN", "white")
        self.board[7][6] = ChessPiece.ChessPiece("PAWN", "white")

        self.board[1][7] = ChessPiece.ChessPiece("KNIGHT", "white")
        self.board[6][7] = ChessPiece.ChessPiece("KNIGHT", "white")
        self.board[2][7] = ChessPiece.ChessPiece("BISHOP", "white")
        self.board[5][7] = ChessPiece.ChessPiece("BISHOP", "white")
        self.board[0][7] = ChessPiece.ChessPiece("ROOK", "white")
        self.board[7][7] = ChessPiece.ChessPiece("ROOK", "white")

        self.board[3][7] = ChessPiece.ChessPiece("QUEEN", "white")
        self.board[4][7] = ChessPiece.ChessPiece("KING", "white")



    def determinePossibleMoves(self, piece, coordinate): #return a list of tuples (coordinates) with all possible moves a piece can make
        result = []

        if piece.type == "PAWN":
            if piece.team == "white":
                if self.board[coordinate[0]][coordinate[1] - 1] == 0: #if space above pawn is free
                    result.append((coordinate[0], coordinate[1] - 1))

                if coordinate[0] != 0: #check if pawn is in the leftmost column
                    if self.board[coordinate[0] - 1][coordinate[1] - 1] != 0:  # check that 1 up and 1 left is a piece
                        if self.board[coordinate[0] - 1][coordinate[1] - 1].team == "black": #if space 1 up and 1 left is has an enemy piece
                            result.append((coordinate[0] - 1, coordinate[1] - 1))

                if coordinate[0] != 7: #check if pawn is in the rightmost column
                    if self.board[coordinate[0] + 1][coordinate[1] - 1] != 0:  # check that 1 up and 1 right is a piece
                        if self.board[coordinate[0] + 1][coordinate[1] - 1].team == "black": #if space 1 up and 1 right is has an enemy piece
                            result.append((coordinate[0] + 1, coordinate[1] - 1))
            elif piece.team == "black":
                if self.board[coordinate[0]][coordinate[1] + 1] == 0: #if space below pawn is free
                    result.append((coordinate[0], coordinate[1] + 1))

                if coordinate[0] != 0: #check if pawn is in the leftmost column
                    if self.board[coordinate[0] - 1][coordinate[1] + 1] != 0:  # check that 1 up and 1 left is a piece
                        if self.board[coordinate[0] - 1][coordinate[1] + 1].team == "white": #if space 1 up and 1 left is has an enemy piece
                            result.append((coordinate[0] - 1, coordinate[1] + 1))

                if coordinate[0] != 7: #check if pawn is in the rightmost column
                    if self.board[coordinate[0] + 1][coordinate[1] + 1] != 0:  # check that 1 up and 1 right is a piece
                        if self.board[coordinate[0] + 1][coordinate[1] + 1].team == "white": #if space 1 up and 1 right is has an enemy piece
                            result.append((coordinate[0] + 1, coordinate[1] + 1))



        elif piece.type == "BISHOP":
            if piece.team == "white":   #white bishop
                i = coordinate[0] + 1   #tracking the horizontal position
                j = coordinate[1] - 1   #tracking the vertical position
                while i >= 0 and i <= 7 and j >= 0 and j <= 7:   #going up and right
                    if self.board[i][j] == 0:
                        result.append((i,j))
                    elif self.board[i][j].team == "black":
                        result.append((i,j))
                        break
                    else:
                        break
                    i += 1
                    j -= 1

                i = coordinate[0] - 1   #tracking the horizontal position
                j = coordinate[1] - 1   #tracking the vertical position
                while i >= 0 and i <= 7 and j >= 0 and j <= 7:   #going up and left
                    if self.board[i][j] == 0:
                        result.append((i,j))
                    elif self.board[i][j].team == "black":
                        result.append((i,j))
                        break
                    else:
                        break
                    i -= 1
                    j -= 1

                i = coordinate[0] + 1   #tracking the horizontal position
                j = coordinate[1] + 1   #tracking the vertical position
                while i >= 0 and i <= 7 and j >= 0 and j <= 7:   #going down and right
                    if self.board[i][j] == 0:
                        result.append((i,j))
                    elif self.board[i][j].team == "black":
                        result.append((i,j))
                        break
                    else:
                        break
                    i += 1
                    j += 1

                i = coordinate[0] - 1   #tracking the horizontal position
                j = coordinate[1] + 1   #tracking the vertical position
                while i >= 0 and i <= 7 and j >= 0 and j <= 7:   #going down and left
                    if self.board[i][j] == 0:
                        result.append((i,j))
                    elif self.board[i][j].team == "black":
                        result.append((i,j))
                        break
                    else:
                        break
                    i -= 1
                    j += 1


            if piece.team == "black":   #black bishop
                i = coordinate[0] + 1   #tracking the horizontal position
                j = coordinate[1] - 1   #tracking the vertical position
                while i >= 0 and i <= 7 and j >= 0 and j <= 7:   #going up and right
                    if self.board[i][j] == 0:
                        result.append((i,j))
                    elif self.board[i][j].team == "white":
                        result.append((i,j))
                        break
                    else:
                        break
                    i += 1
                    j -= 1

                i = coordinate[0] - 1   #tracking the horizontal position
                j = coordinate[1] - 1   #tracking the vertical position
                while i >= 0 and i <= 7 and j >= 0 and j <= 7:   #going up and left
                    if self.board[i][j] == 0:
                        result.append((i,j))
                    elif self.board[i][j].team == "white":
                        result.append((i,j))
                        break
                    else:
                        break
                    i -= 1
                    j -= 1

                i = coordinate[0] + 1   #tracking the horizontal position
                j = coordinate[1] + 1   #tracking the vertical position
                while i >= 0 and i <= 7 and j >= 0 and j <= 7:   #going down and right
                    if self.board[i][j] == 0:
                        result.append((i,j))
                    elif self.board[i][j].team == "white":
                        result.append((i,j))
                        break
                    else:
                        break
                    i += 1
                    j += 1

                i = coordinate[0] - 1   #tracking the horizontal position
                j = coordinate[1] + 1   #tracking the vertical position
                while i >= 0 and i <= 7 and j >= 0 and j <= 7:   #going down and left
                    if self.board[i][j] == 0:
                        result.append((i,j))
                    elif self.board[i][j].team == "white":
                        result.append((i,j))
                        break
                    else:
                        break
                    i -= 1
                    j += 1




        elif piece.type == "KNIGHT":
            if piece.team == "white":
                try:
                    if self.board[coordinate[0] + 1][coordinate[1] + 2] == 0 or self.board[coordinate[0] + 1][coordinate[1] + 2].team == "black":
                        result.append((coordinate[0] + 1, coordinate[1] + 2))
                except:
                    pass
                try:
                    if self.board[coordinate[0] + 1][coordinate[1] - 2] == 0 or self.board[coordinate[0] + 1][coordinate[1] - 2].team == "black":
                        result.append((coordinate[0] + 1, coordinate[1] - 2))
                except:
                    pass
                try:
                    if self.board[coordinate[0] - 1][coordinate[1] + 2] == 0 or self.board[coordinate[0] - 1][coordinate[1] + 2].team == "black":
                        result.append((coordinate[0] - 1, coordinate[1] + 2))
                except:
                    pass
                try:
                    if self.board[coordinate[0] - 1][coordinate[1] - 2] == 0 or self.board[coordinate[0] - 1][coordinate[1] - 2].team == "black":
                        result.append((coordinate[0] - 1, coordinate[1] - 2))
                except:
                    pass
                try:
                    if self.board[coordinate[0] + 2][coordinate[1] + 1] == 0 or self.board[coordinate[0] + 2][coordinate[1] + 1].team == "black":
                        result.append((coordinate[0] + 2, coordinate[1] + 1))
                except:
                    pass
                try:
                    if self.board[coordinate[0] + 2][coordinate[1] - 1] == 0 or self.board[coordinate[0] + 2][coordinate[1] - 1].team == "black":
                        result.append((coordinate[0] + 2, coordinate[1] - 1))
                except:
                    pass
                try:
                    if self.board[coordinate[0] - 2][coordinate[1] + 1] == 0 or self.board[coordinate[0] - 2][coordinate[1] + 1].team == "black":
                        result.append((coordinate[0] - 2, coordinate[1] + 1))
                except:
                    pass
                try:
                    if self.board[coordinate[0] - 2][coordinate[1] - 1] == 0 or self.board[coordinate[0] - 2][coordinate[1] - 1].team == "black":
                        result.append((coordinate[0] - 2, coordinate[1] - 1))
                except:
                    pass



            if piece.team == "black":
                try:
                    if self.board[coordinate[0] + 1][coordinate[1] + 2] == 0 or self.board[coordinate[0] + 1][coordinate[1] + 2].team == "white":
                        result.append((coordinate[0] + 1, coordinate[1] + 2))
                except:
                    pass
                try:
                    if self.board[coordinate[0] + 1][coordinate[1] - 2] == 0 or self.board[coordinate[0] + 1][coordinate[1] - 2].team == "white":
                        result.append((coordinate[0] + 1, coordinate[1] - 2))
                except:
                    pass
                try:
                    if self.board[coordinate[0] - 1][coordinate[1] + 2] == 0 or self.board[coordinate[0] - 1][coordinate[1] + 2].team == "white":
                        result.append((coordinate[0] - 1, coordinate[1] + 2))
                except:
                    pass
                try:
                    if self.board[coordinate[0] - 1][coordinate[1] - 2] == 0 or self.board[coordinate[0] - 1][coordinate[1] - 2].team == "white":
                        result.append((coordinate[0] - 1, coordinate[1] - 2))
                except:
                    pass
                try:
                    if self.board[coordinate[0] + 2][coordinate[1] + 1] == 0 or self.board[coordinate[0] + 2][coordinate[1] + 1].team == "white":
                        result.append((coordinate[0] + 2, coordinate[1] + 1))
                except:
                    pass
                try:
                    if self.board[coordinate[0] + 2][coordinate[1] - 1] == 0 or self.board[coordinate[0] + 2][coordinate[1] - 1].team == "white":
                        result.append((coordinate[0] + 2, coordinate[1] - 1))
                except:
                    pass
                try:
                    if self.board[coordinate[0] - 2][coordinate[1] + 1] == 0 or self.board[coordinate[0] - 2][coordinate[1] + 1].team == "white":
                        result.append((coordinate[0] - 2, coordinate[1] + 1))
                except:
                    pass
                try:
                    if self.board[coordinate[0] - 2][coordinate[1] - 1] == 0 or self.board[coordinate[0] - 2][coordinate[1] - 1].team == "white":
                        result.append((coordinate[0] - 2, coordinate[1] - 1))
                except:
                    pass


        elif piece.type == "ROOK":
            if piece.team == "white":   #white rook
                for i in range(coordinate[0] + 1,8):  #going right
                    if self.board[i][coordinate[1]] == 0:
                        result.append((i,coordinate[1]))
                    elif self.board[i][coordinate[1]].team == "black":
                        result.append((i,coordinate[1]))
                        break
                    else:
                        break

                for i in range(coordinate[0] - 1,-1,-1):  #going left
                    if self.board[i][coordinate[1]] == 0:
                        result.append((i,coordinate[1]))
                    elif self.board[i][coordinate[1]].team == "black":
                        result.append((i,coordinate[1]))
                        break
                    else:
                        break

                for i in range(coordinate[1] - 1,0,-1):  #going up
                    if self.board[coordinate[0]][i] == 0:
                        result.append((coordinate[0],i))
                    elif self.board[coordinate[0]][i].team == "black":
                        result.append((coordinate[0],i))
                        break
                    else:
                        break

                for i in range(coordinate[1] + 1,8):  #going down
                    if self.board[coordinate[0]][i] == 0:
                        result.append((coordinate[0],i))
                    elif self.board[coordinate[0]][i].team == "black":
                        result.append((coordinate[0],i))
                        break
                    else:
                        break


            if piece.team == "black":   #black rook
                for i in range(coordinate[0] + 1,8):  #going right
                    if self.board[i][coordinate[1]] == 0:
                        result.append((i,coordinate[1]))
                    elif self.board[i][coordinate[1]].team == "white":
                        result.append((i,coordinate[1]))
                        break
                    else:
                        break

                for i in range(coordinate[0] - 1,-1,-1):  #going left
                    if self.board[i][coordinate[1]] == 0:
                        result.append((i,coordinate[1]))
                    elif self.board[i][coordinate[1]].team == "white":
                        result.append((i,coordinate[1]))
                        break
                    else:
                        break

                for i in range(coordinate[1] - 1,0,-1):  #going up
                    if self.board[coordinate[0]][i] == 0:
                        result.append((coordinate[0],i))
                    elif self.board[coordinate[0]][i].team == "white":
                        result.append((coordinate[0],i))
                        break
                    else:
                        break

                for i in range(coordinate[1] + 1,8):  #going down
                    if self.board[coordinate[0]][i] == 0:
                        result.append((coordinate[0],i))
                    elif self.board[coordinate[0]][i].team == "white":
                        result.append((coordinate[0],i))
                        break
                    else:
                        break


        elif piece.type == "QUEEN":
            tempBishop = ChessPiece.ChessPiece("BISHOP", piece.team)
            tempRook = ChessPiece.ChessPiece("ROOK",piece.team)

            result = result + self.determinePossibleMoves(tempBishop, coordinate) + self.determinePossibleMoves(tempRook, coordinate)

        elif piece.type == "KING":
            if piece.team == "white":
                for i in range(-1,2):
                    for j in range(-1,2):
                        try:
                            if self.board[coordinate[0] + i][coordinate[1] + j] == 0 or self.board[coordinate[0] + i][coordinate[1] + j].team == "black":
                                result.append((coordinate[0] + i,coordinate[1] + j))
                        except:
                            pass

            if piece.team == "black":
                for i in range(-1,2):
                    for j in range(-1,2):
                        try:
                            if self.board[coordinate[0] + i][coordinate[1] + j] == 0 or self.board[coordinate[0] + i][coordinate[1] + j].team == "white":
                                result.append((coordinate[0] + i,coordinate[1] + j))
                        except:
                            pass

        return result

    def printBoard(self):
        for i in range(8):
            print(self.board[i])