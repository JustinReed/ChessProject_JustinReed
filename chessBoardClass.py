#import chessPieceClass

class ChessBoard:
    def __init__(self):
        self.chessMatrix = []  # array works in reverse: y is listed first, x is listed second
        for i in range(8):
            self.chessMatrix.append([])
            for j in range(8):
                self.chessMatrix[i].append([])

    def getArray(self):
        return self.chessMatrix

    def __str__(self):
        chessBoardString = ""
        for i in range(8):
            chessBoardString += str(self.chessMatrix[i][0:8]) + "\n"
        return chessBoardString

def printChessBoard():

    chessBoardString = ""

    for i in range(7, -1, -1):
        for j in range(8):
            chessBoardString += str(CurrentBoard.getArray()[i][j])
        chessBoardString += "\n"
    print(str(CurrentBoard.getArray()[1][1]))
    print(chessBoardString)

CurrentBoard: ChessBoard = ChessBoard()

class Piece:
    def __init__(self, coords: list[int], color):
        self.coords = coords  # x listed first, y listed second
        self.xPos: int = coords[0]
        self.yPos: int = coords[1]
        self.color = color

    def checkCapture(self, newCoords) -> bool:
        if CurrentBoard.getArray()[newCoords[1]][newCoords[0]] != []:
            return True
        else:
            return False

    def movePiece(self, newCoords: list[int]) -> bool:

        if newCoords[0] not in range(8) or newCoords[1] not in range(8):
            print("error")
            return False
        elif self.checkValidMove(newCoords):
            CurrentBoard.getArray()[self.yPos][self.xPos] = []
            self.coords = newCoords
            self.xPos = newCoords[0]
            self.yPos = newCoords[1]
            CurrentBoard.getArray()[newCoords[1]][newCoords[0]] = self
            return True
        else:
            print("error")
            return False

    def checkValidMove(self, newCoords):
        pass

class WhitePawn(Piece):
    """
    White Pawns need a move-set distinct from black pawns as they move in opposite directions
    """
    def __init__(self, coords: list[int]):
        super().__init__(coords, "White")

    def checkValidMove(self, newCoords: list[int]) -> bool:
        if abs(newCoords[0] - self.coords[0]) == 1 and newCoords[1] - self.coords[1] == 1: # pawn captures diagonally
            return self.checkCapture(newCoords)
        elif newCoords[0] - self.coords[0] == 0:  # pawn moves forward
            if newCoords[1] - self.coords[1] == 1: # move forward one square
                return not self.checkCapture(newCoords) # pawn cannot capture pieces directly in front of it
            elif newCoords[1] - self.coords[1] == 2:
                return (not self.checkCapture(newCoords)) and self.checkCapture([newCoords[0], newCoords[1] - 1]) and self.coords[1] == 1
        else:
            return False

    def __str__(self):
        return "WP"  # stands for white pawn

for i in range(8):
    CurrentBoard.getArray()[1][i] = WhitePawn([i, 1])


class BlackPawn(Piece):
    def __init__(self, coords: list[int]):
        super().__init__(coords, "Black")

    def checkValidMove(self, newCoords: list[int]) -> bool:
        if abs(newCoords[0] - self.coords[0]) == 1 and newCoords[1] - self.coords[1] == -1: # pawn captures diagonally
            return self.checkCapture(newCoords)
        elif newCoords[0] - self.coords[0] == 0:  # pawn moves forward
            if newCoords[1] - self.coords[1] == -1: # move forward one square
                return not self.checkCapture(newCoords) # pawn cannot capture pieces directly in front of it
            elif newCoords[1] - self.coords[1] == -2:
                return (not self.checkCapture(newCoords)) and self.checkCapture([newCoords[0], newCoords[1] + 1]) and self.coords[1] == 6
        else:
            return False

    def __str__(self):
        return "BP"  # stands for white pawn

for i in range(8):
    CurrentBoard.getArray()[6][i] = BlackPawn([i, 6])

class Rook(Piece):
    def __init__(self, coords: list[int], color):
        super().__init__(coords, color)

    def checkValidMove(self, newCoords):
        if self.yPos - newCoords[1] == 0 and self.xPos - newCoords[0] != 0: # rook moves along x-axis
            for i in range(min(self.xPos, newCoords[0]) + 1, max(self.xPos, newCoords[0]) - 1): # check if rook intersects piece while trying to move to new square
                if self.checkCapture([i, self.yPos]):
                    return False
            return True
        elif self.xPos - newCoords[0] == 0 and self.yPos - newCoords[1] != 0: # rook moves along y-axis
            for i in range(min(self.yPos, newCoords[1]) + 1, max(self.yPos, newCoords[1]) - 1):
                if self.checkCapture([self.xPos, i]):
                    return False
            return True
        else: # rook moves neither horizontally nor diagonally
            return False



    def __str__(self):
        if self.color == "White":
            return "WR"  # stands for white pawn
        elif self.color == "Black":
            return "BR"

CurrentBoard.getArray()[0][0] = Rook([0, 0], "White")
CurrentBoard.getArray()[0][7] = Rook([7, 0], "White")

CurrentBoard.getArray()[7][0] = Rook([0, 7], "Black")
CurrentBoard.getArray()[7][7] = Rook([7, 7], "Black")







printChessBoard()
activePiece = CurrentBoard.getArray()[1][3]
activePiece.movePiece([3, 2])
activePiece.movePiece([3, 3])
activePiece.movePiece([3, 4])
printChessBoard()


printChessBoard()

activePiece = CurrentBoard.getArray()[0][0]
activePiece.movePiece([3, 0])
activePiece.movePiece([3, 3])
activePiece.movePiece([5, 3])
printChessBoard()

activePiece.movePiece([6, 4])

activePiece.movePiece([11, 3])
