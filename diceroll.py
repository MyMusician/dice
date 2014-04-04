import random

import specialInput

diceNumber = specialInput.int_input("how many dice do you want to have")

for x in range(diceNumber):

    #ask how many sides

    result = random.randint(1,diceSides)

    print "after you have read the README file, here is the result:"

    print result