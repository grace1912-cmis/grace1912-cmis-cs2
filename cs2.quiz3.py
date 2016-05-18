#Section 1: Terminology
# 1) What is a recursive function?
#Recursice function is when the function repeats the certain lines of codes.
#
#
# 2) What happens if there is no base case defined in a recursive function?
#If there is no base case defined in a recursive function, then the function will repeat unendingly. There could also be an error about the maximum of recursion.
#
#
# 3) What is the first thing to consider when designing a recursive function?
#The first thing is to consider the base cases of a recursive function. You should know what it will return.
#
#
# 4) How do we put data into a function call?
#By parameters
#
# 
# 5) How do we get data out of a function call?
#By parameters
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 =8
#a2 =8
#a3 =-1

#b1 =2
#b2 =2
#b3 =4

#c1 =-2
#c2 =4
#c3 =45

#d1 =6
#d2 =8
#d3 =-4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def Odd_Avg(total):
#Base Case
	Number = raw_input("Number: ")
	if Number== "":
		return raw_input("The Average of all the odd Number is: " + str(total)+ ".")
#Recursive Case
	else:
		Average=  float(total) % 2
		print "Odd Average: " +str(total) + "."
		return Odd_Avg(total) 



