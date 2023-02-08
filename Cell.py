from Utils import *

class Cell:
    def __init__(self, name: str, id: int, cell: str, color: str) -> None:
        self._name: str = name
        self._id: int = id
        self._cell: str = cell
        self._color: str = color
        
    def getColor(self) -> str:
        return self._color
    
    def promoteTo(self, piecePromote: str) -> None:
        self._name = piecePromote
        
    def getCell(self) -> str:
        return self._cell
    
    def isOn(self, cell: str) -> bool:
        return self._cell == cell
    
    def isWhite(self) -> bool:
        return self._color == "w"

    def promoteTo(self, newPiece):
        self._name = newPiece

    def getCellsBetweenBishop(self, begin: str, end: str) -> list[str]:
        pass
    
    def getCellsBetweenRook(self, begin: str, end: str) -> list[str]:
        pass
    
    def getCellsBetweenQueen(self, begin: str, end: str) -> list[str]:
        pass