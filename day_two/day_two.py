import sys
from enum import Enum

ABC_Value_Offset = 64
XYZ_Value_Offset = 23

LOSE = 0
DRAW = 3
WIN = 6

class Symbol(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

class Hand:
    def __init__(self, *args):
        if len(args) > 1:
            # initalize hand with Symbol based on opponent's hand and desired outcome
            desired_outcome = args[0] - ABC_Value_Offset
            opponent_hand = args[1]
            
            #desired outcome
            if desired_outcome == 1: #LOSS
                if opponent_hand == Symbol.ROCK.value:
                    self.hand = Symbol.SCISSOR.value
                elif opponent_hand == Symbol.PAPER.value:
                    self.hand = Symbol.ROCK.value
                elif opponent_hand == Symbol.SCISSOR.value:
                    self.hand = Symbol.PAPER.value
            elif desired_outcome == 2: #DRAW
                self.hand = opponent_hand
            elif desired_outcome == 3: #WIN
                if opponent_hand == Symbol.ROCK.value:
                    self.hand = Symbol.PAPER.value
                elif opponent_hand == Symbol.PAPER.value:
                    self.hand = Symbol.SCISSOR.value
                elif opponent_hand == Symbol.SCISSOR.value:
                    self.hand = Symbol.ROCK.value
        elif len(args) == 1:
            self.hand = args[0] - ABC_Value_Offset
        else:
            raise Exception("Invalid arg when constructing Hand object")
        
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
        yourself = Hand(ord(yourself)-XYZ_Value_Offset, opponent.hand)
        print(f'you get {yourself.hand} for playing {yourself}')
        score += yourself.hand #your decision
        # add score of whether you win, lose, or tie
        score += yourself.versus(opponent)
        
    print(f'Your score following the strategy is {score}.')
    f.close()




 
