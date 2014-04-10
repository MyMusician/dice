import random

import specialInput

diceNumber = specialInput.int_input("how many dice do you want to have")


for x in range(diceNumber):
        
    diceSides = specialInput.int_input("how many sides do your dice have?")

    if diceSides < 2:
    
        print "sorry we could not code a one sided die. The costumer service is on aisle 7

    else:

        result = random.randint(1,diceSides)
    
        print "after you have read the README file, here is the result:"

        print result
