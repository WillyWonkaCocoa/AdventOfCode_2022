import sys
from enum import Enum

ABC_Value_Offset = 64
XYZ_Value_Offset = 23

WIN = 6
LOSE = 0
DRAW = 3

class Symbol(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

class Hand:
    def __init__(self, hand):
        self.hand = hand - ABC_Value_Offset
    def __str__(self):
        if self.hand == Symbol.ROCK.value:
            return "Rock"
        elif self.hand == Symbol.PAPER.value:
            return "Paper"
        elif self.hand == Symbol.SCISSOR.value:
            return "Scissor"
        else:
            return "Invalid hand"
    def versus(self, opponent):
        if self.hand == opponent.hand:
            return DRAW
        elif self.hand == Symbol.ROCK.value and opponent.hand == Symbol.SCISSOR.value:
            return WIN
        elif self.hand == Symbol.SCISSOR.value and opponent.hand == Symbol.ROCK.value:
            return LOSE
        elif self.hand > opponent.hand:
            return WIN
        else:
            return LOSE
            
        
            


if len(sys.argv) < 2:
    raise Exception("Missing input file!")
else:
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    score = 0

    for line in lines:
        opponent, yourself = line.split()
        opponent = Hand(ord(opponent))
        yourself = Hand(ord(yourself)-XYZ_Value_Offset)
        print(f'you get {yourself.hand} for playing {yourself}')
        score += yourself.hand #your decision
        # add score of whether you win, lose, or tie
        score += yourself.versus(opponent)
        
            
    print(f'Your score following the strategy is {score}.')
    f.close()




 
