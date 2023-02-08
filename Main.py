from Chess import *
from Utils import *

def main():
    game = Chess()
    while(not game.isEnded()):
        nextMove = Utils.askMove()
        game.convertMove(nextMove)
    
if __name__ == "__main__":
    main()