#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#The assignment operator is used to assign the right operans to the left
#
#
#2 3pts) Write a technical definition for 'function'
#A function is a named sequence of statements that performs a computation
#
#
#3 1pt) What does the keyword "return" do?
#It spits out a value right away from the specific function and uses the following expression  as a return value.
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: string: "Inhye" "Hi"
#	2: tuple: ("Inhye", "Eww", 34, "Wut") ("food", "Wednesday", 56, "student")
#	3:boolean: True False 
#	4:interger: 77, 17
#	5:floating point: 1.2, 0.2
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#A function call is when you define a function and specifically explain its name and the following sequence. When you call the function, you are calling that function by the name which you defined. A function definition specifies the name of a new function and the sequence of statements that execute when the function is called.

#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:Input:Get data from the keyboard, a file, or some other device.

#	2:Processing:This is the main part of the function, where the computations will be done. It may use variables defined in the input stage.
#	3:Output:Display data on the screen or send data to a file or other device.
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the radius and height of 2 cylinders.
#It should then calculate the volume of each and the difference of the volumes. 
#
#Finally, it should produce output like this:

#Cylinder      volume
#c1            ...
#c2            ...
#Difference    ...

# Hint: Volume of a sphere is pi x radius squared x height
import math

def RadiusOne(a):
    return float(a)
def RadiusTwo(b):
    return float(b)
def HeightOne(x):
    return float(x)
def HeightTwo(y):
    return float(y)
def Volume(v):
    return math.pi * (radius**2) * height
def diff(n, z, d, e):
    return n - z - d - e

def output(radius1,radius2,height1,height2,differenceOfVolumes):
    out = """
Radius Of Cylinder One : {}\n
Radius Of Cylinder Two : {}\n
Height Of Cylinder One : {}\n
Height Of Cylinder Two : {}\n
Difference Of Volumes : {}
""".format (radius1,radius2,height1,height2, differenceOfVolumes)
    return out

def main():
	#Input
    a = int(raw_input("Radius One:\n"))
    b = int(raw_input("Radius Two:\n"))
    x = int(raw_input("Height One:\n"))
    y =int(raw_input("Height Two:\n"))
	
	#Processing	
    radius1 = radius(a)
    radius2 = radius(b)
    height1 = height(x)
    height2 = height(y)
    differenceOfVolume= difference(radius1, radius2, height1, height2, differenceOfVolumes)
	#Output
    out = output(radius1, radius2, height1, height2, differenceOfVolumes)
    print out
main()




