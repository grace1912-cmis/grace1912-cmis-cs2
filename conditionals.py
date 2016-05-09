#You are trapped in a Pizza Restaurant. Certain types of pizzas can let you out. Your task is to figure out the right type of pizza to be freed from the Pizza place. You have four sections to choose the right pizza. You only have three choices for each sections. In order for you to get out, your sum has to be either 3, 6, or 9.

print "Holly macaroni! You are trapped in a Pizza Restaurent! If you don't want to end your life with pathetic pizzas, GO ahead and figure out the KEY PIZZA to get out of this traumatic place! Make sure to get either 3 points,6 points,or 9 points. They have to end up with exact three of the given numbers. Good Luck (:"
import math
import random
def add(a, b):
	return float(a) + float(b)

def GuessingShape():
	Shape = raw_input("Choose ONE type of triangles of your pizza,(Isoceles, Scalene, Right) :")
	if Shape == "Scalene":
		print float("1")
	elif Shape == "Isoceles":
		print float("2")
	elif Shape == "Right":
	    print float("3")
#Types
def GuessingType():
	Type= raw_input("Choose the type of of your pizza (Cheese, Peperoni, Hawaiian): ")
	if Type == "Cheese":
		print float("1")
	elif Type == "Peperoni":
		print float("2")
	elif Type == "Hawaiian":
		print float("3")
#Sizes
def GuessinSize():
	Size= raw_input("Choose the type of your pizza (Large, Medium, Small): ")
	if Size == "Large":
		print float("1")
	elif Size == "Medium":
		print float("2")
	elif Size== "Small":
		print float("3")

GuessingShape()
#Calculation of The Points
   

