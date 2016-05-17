#You are trapped in a Pizza Restaurant. Certain types of pizzas can let you out. Your task is to figure out the right type of pizza to be freed from the Pizza place. You have four sections to choose the right pizza. You only have three choices for each sections. In order for you to get out, your sum has to be either 3, 6, or 9.

import math
import random

print "Holly macaroni! You are trapped in a Pizza Restaurant! If you don't want to end your life with pathetic pizzas, GO ahead and figure out the KEY PIZZA to get out of this traumatic place! Make sure to get either 3 points,6 points,or 9 points. They have to end up with exact three of the given numbers. Good Luck (:"

def add(a, b):
	return float(a) + float(b)
#Shape
def GuessingShape():
	Shape = raw_input("Choose ONE type of triangles of your pizza,(Isoceles, Scalene, Right) :")
	if Shape == "Scalene":
		print float(1)
		return float(1)
	elif Shape == "Isoceles":
		print float(2)
		return float(2)
		
	elif Shape == "Right":
		print float(3)
		return float(3)
		
#Types
def GuessingType():
	Type= raw_input("Choose the type of of your pizza (Cheese, Peperoni, Hawaiian): ")
	if Type == "Cheese":
		print float(1)
		return float(1)
	elif Type == "Peperoni":
		print float(2)
		return float(2)
	elif Type == "Hawaiian":
		print float(3)
		return float(3)
		
#Sizes	
def GuessingSize():
	Size= raw_input("Choose the size of your pizza (Large, Medium, Small): ")
	if Size == "Large":
		print float(1)
		return float(1)		
	elif Size == "Medium":
		print float(2)
		return float(2)
	elif Size== "Small":
		print float(3)
		return float(3)
#Bonus

def Bonus_2():
	Bonus2= raw_input("Guess a decimal between 0 and 1: ")
	Answer = random.random()
	if float(Bonus2) == Answer:
		print True
	else:
		return "Game Over"

def Bonus_1():
	Bonus1 = raw_input("Guess an integer between 1 and 9 for a bonus chance to fix your score: ")
	Answer = random.randint(0,9) 
	if int(Bonus1) == Answer:
		print Bonus1
	else:
		return Bonus_2()
			
#Calculation of The Points
def main():
	Shape=GuessingShape()
	Type= GuessingType()
	Size=GuessingSize()
	YourScore = int(Shape)+int(Type) + int(Size)

	output= """
Your Score is {}
Try Again.
""".format(YourScore)
	if int(YourScore) == int(3):
		print "Good Job!"
	elif int(YourScore) == int(6):
		print "You're Out!"
	elif int(YourScore) == int(9):
		print "Yappppyyyy"
#Conclusion
	elif int(YourScore) < int(3) or int(YourScore) > int(3):
		print"BOOO HOOO"
		print output
	elif not int(YourScore) < int(6) or int(YOurScore) > int(6):
		print"FAIL"
	else:
		print"GAME OVERR"
#No Bonus
	if YourScore != int(3) and YourScore != int(6) and YourScore != int(9):
		print Bonus_1()
	if YourScore != int(3) and YourScore != int(6) and YourScore != int(9):
		print Bonus_1()

main()

	



