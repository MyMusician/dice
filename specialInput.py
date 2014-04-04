
def name_input(prompt):
	name = raw_input(prompt)
	if len(name) > 10:
		print "that name is too long. I am going to give you a nick name"
		return len(name) < 10
	else:
		return name

def int_input(prompt):
	while True:
			number = raw_input(prompt)
			try:
				number = int(number)
				return number
			except:
				print "try again its not a valid number"
		
def float_input(prompt):
	while True:
		number = raw_input(prompt)
		try:
			number = float(number)
			return number
		except:
			print "try again its not a valid number"
		
		
	
		
