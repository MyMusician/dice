import random

import specialInput

diceNumber = specialInput.int_input("how many dice do you want to have")

diceSides = specialInput.int_input("how many sides do your dice have?")
for x in range(diceNumber):

    result = random.randint(1,diceSides)

    print "after you have read the README file, here is the result:"

    print result