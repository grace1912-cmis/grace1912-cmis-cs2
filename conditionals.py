#You are trapped in a Pizza Restaurant. Certain types of pizzas can let you out. Your task is to figure out the right type of pizza to be freed from the Pizza place. You have four sections to choose the right pizza. You only have three choices for each sections. In order for you to get out, your sum has to be either 3, 6, or 9.

import math
import random

print "Holly macaroni! You are trapped in a Pizza Restaurant! If you don't want to end your life with pathetic pizzas, GO ahead and figure out the KEY PIZZA to get out of this traumatic place! Make sure to get either 3 points,6 points,or 9 points. They have to end up with exact three of the given numbers. Good Luck (:"

def add(a, b):
	return float(a) + float(b)

def GuessingShape():
	Shape = raw_input("Choose ONE type of triangles of your pizza,(Isoceles, Scalene, Right) :")
	if Shape == "Scalene":
		print float(1)
	elif Shape == "Isoceles":
		print float(2)
	elif Shape == "Right":
	    print float(3)
GuessingShape()
#Types
def GuessingType():
	Type= raw_input("Choose the type of of your pizza (Cheese, Peperoni, Hawaiian): ")
	if Type == "Cheese":
		print float(1)
	elif Type == "Peperoni":
		print float(2)
	elif Type == "Hawaiian":
		print float(3)
GuessingType()
#Sizes
def GuessingSize():
	Size= raw_input("Choose the size of your pizza (Large, Medium, Small): ")
	if Size == "Large":
		print float(1)
	elif Size == "Medium":
		print float(2)
	elif Size== "Small":
		print float(3)
GuessingSize()

#Calculation of The Points

def main():
	return GuessingShape()
	return GuessingType()
	return GuessingSize()
	YourScore = GuessinShape +GuessinType+ GuessinSize
	output= """
Your Score is {}
Try Again.
""".format(YourScore)
	if int(YourScore) == int(3):
		print "Good JOb!"
	elif int(YourScore) == int(6):
		print "You're Out!"
	elif int(YourScore) == int(9):
		print "Yappppyyyy"
#Conclusion
	elif int(YourScore) < int(3) or int(YourScore) > int(3):
		print"BOOO HOOO"
	elif int(YourScore) < int(6) or int(YOurScore) > int(6):
		print"FAIL"
	elif int(YourScore)< int(9) or int(YourScore) > int(9):
		print"GAME OVERR"
	else:
		print output
main()
	



