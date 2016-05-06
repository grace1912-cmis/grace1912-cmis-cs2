import random
def ReGuess(Guessing_Number,Comp_Number):
	return Difference(First, Second)  
def Difference(First, Second):
	return abs(First - Second)
	
def main(): 
	Minimum = raw_input("Type in the Minimum number:")
	Maximum = raw_input("Type in the Maximum number:")

	output = """I'm thinking of a number between {} and {} """.format(Minimum, Maximum)
	print output


	Comp_Number = random.randint(int(Minimum), int(Maximum))
	Guessing_Number = raw_input("Guess:")

	
	output = """The number was {}.Your guess was {}. """.format(Comp_Number,Guessing_Number)
	print output
	
	if int(Guessing_Number) == int(Comp_Number):
		print "Congratulations! You got it Right!"

	elif int(Guessing_Number) > int(Comp_Number):
		print "Your Guess was over by" ,str(Difference(int(Guessing_Number), int(Comp_Number)))
	else:
		return ReGuess(Guessing_Number,Comp_Number)
	
	elif int(Guessing_Number) < int(Comp_Number):
		print "Your Guess was under by" ,Difference(int(Guessing_Number), int(Comp_Number))



main()
