from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
                        
                 Or(AKnave,AKnight), 
                 Not(And(AKnave, AKnight)), 

                 #Implication(Not(And(AKnave,AKnight)), AKnave),
                 Implication(AKnight,And(AKnave,AKnight))

#                 
                 
                 
    # TODO
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
      Or(AKnave,AKnight),
      Or(BKnave,BKnight),
   
      Not(And(BKnave, BKnight)),
      Not(And(AKnave, AKnight)),
      

      Implication(AKnight, And(BKnave,AKnave)),
      Implication(AKnave, Not(BKnave))
    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
      Or(AKnave,AKnight),
      Or(BKnave,BKnight),
   
      Not(And(BKnave, BKnight)),
      Not(And(AKnave, AKnight)),


      Implication(AKnight, And(BKnight,AKnight)),
      Implication(AKnave, BKnight),
      Implication(BKnight, Not(AKnight)),
      Implication(BKnave, AKnave)
                 
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
      Or(AKnave,AKnight),
      Or(BKnave,BKnight),
      Or(CKnave,CKnight),

   
      Not(And(BKnave, BKnight)),
      Not(And(AKnave, AKnight)),
      Not(And(CKnave, CKnight)),
      
      Implication(AKnight, BKnave),
      Implication(BKnave, CKnight),
      Implication(BKnave, CKnave),
      Biconditional(BKnight, AKnave),

      Implication(BKnight, CKnave)
      #Implication(CKnave, And(BKnight,AKnave))

      
                 
                 
                 
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print("    {}".format(symbol))


if __name__ == "__main__":
    main()
