import random

import specialInput

diceSides = specialInput.int_input("how many sides does your die have?")

result = random.randint(1,diceSides)

print "after you have read the README file, here is the result:"

print result