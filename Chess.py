from Cell import *

class Chess:
    def __init__(self) -> None:
        self.initialChessPosition = [
            # White pieces
            { "name": 'P', "id": 1, "cell": "a2", "color": 'w' }, # White pawn 1
            { "name": 'P', "id": 2, "cell": "b2", "color": 'w' }, # White pawn 2
            { "name": 'P', "id": 3, "cell": "c2", "color": 'w' }, # White pawn 3
            { "name": 'P', "id": 4, "cell": "d2", "color": 'w' }, # White pawn 4
            { "name": 'P', "id": 5, "cell": "e2", "color": 'w' }, # White pawn 5
            { "name": 'P', "id": 6, "cell": "f2", "color": 'w' }, # White pawn 6
            { "name": 'P', "id": 7, "cell": "g2", "color": 'w' }, # White pawn 7
            { "name": 'P', "id": 8, "cell": "h2", "color": 'w' }, # White pawn 8
            { "name": 'R', "id": 9, "cell": "a1", "color": 'w' }, # White rook 1
            { "name": 'N', "id": 10, "cell": "b1", "color": 'w' },# White knight 1
            { "name": 'B', "id": 11, "cell": "c1", "color": 'w' },# White bishop 1
            { "name": 'Q', "id": 12, "cell": "d1", "color": 'w' },# White queen 1
            { "name": 'k', "id": 13, "cell": "e1", "color": 'w' },# White king 1
            { "name": 'B', "id": 14, "cell": "f1", "color": 'w' },# White bishop 2
            { "name": 'N', "id": 15, "cell": "g1", "color": 'w' },# White knight 2
            { "name": 'R', "id": 16, "cell": "h1", "color": 'w' },# White rook 2
            
            # Black pieces
            { "name": 'P', "id": 17, "cell": "a7", "color": 'b' }, # Black pawn 1
            { "name": 'P', "id": 18, "cell": "b7", "color": 'b' }, # Black pawn 2
            { "name": 'P', "id": 19, "cell": "c7", "color": 'b' }, # Black pawn 3
            { "name": 'P', "id": 20, "cell": "d7", "color": 'b' }, # Black pawn 4
            { "name": 'P', "id": 21, "cell": "e7", "color": 'b' }, # Black pawn 5
            { "name": 'P', "id": 22, "cell": "f7", "color": 'b' }, # Black pawn 6
            { "name": 'P', "id": 23, "cell": "g7", "color": 'b' }, # Black pawn 7
            { "name": 'P', "id": 24, "cell": "h7", "color": 'b' }, # Black pawn 8
            { "name": 'R', "id": 25, "cell": "a8", "color": 'b' }, # Black rook 1
            { "name": 'N', "id": 26, "cell": "b8", "color": 'b' }, # Black knight 1
            { "name": 'B', "id": 27, "cell": "c8", "color": 'b' }, # Black bishop 1
            { "name": 'Q', "id": 28, "cell": "d8", "color": 'b' }, # Black queen 1
            { "name": 'k', "id": 29, "cell": "e8", "color": 'b' }, # Black king 1
            { "name": 'B', "id": 30, "cell": "f8", "color": 'b' }, # Black bishop 2
            { "name": 'N', "id": 31, "cell": "g8", "color": 'b' }, # Black knight 2
            { "name": 'R', "id": 32, "cell": "h8", "color": 'b' }, # Black rook 2
        ]
        self.numberTurn = 0
        self.pieceMatrix: list[Cell] = []
        self.reset()
        self.status: int = -1
        
    def reset(self) -> None:
        for piece in self.initialChessPosition:
            self.pieceMatrix.append(Cell(piece["name"], piece["id"], piece["cell"], piece["color"]))
      
    def getIndexForCell(self, nameCell: str) -> int:
        for i in range(len(self.pieceMatrix)):
            if(self.pieceMatrix[i].getCell() == nameCell): return i
      
    def isAStalemat(self) -> bool:
        return False
            
    def havePieceToMat(self) -> bool:
        return False    
    
    def isADraw(self, color: str) -> bool:
        return False  
    
    def isAChessPos(self, color: str) -> bool:
        return False
    
    def isAChessMate(self, color: str) -> bool:
        return False

    def isEnded(self) -> bool:
        return self.status != -1

    def convertMove(self, nameMove: str) -> list[str]:
        print(nameMove)