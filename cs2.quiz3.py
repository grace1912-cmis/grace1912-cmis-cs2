#Section 1: Terminology
# 1) What is a recursive function?
#Recursice function is when the function repeats the certain lines of codes. It calls itself.
#(1point)
#
# 2) What happens if there is no base case defined in a recursive function?
#If there is no base case defined in a recursive function, then the function will repeat unendingly. There could also be an error about the maximum of recursion.
#(1 point)
#
# 3) What is the first thing to consider when designing a recursive function?
#The first thing is to consider the base cases of a recursive function. You should know what it will return.
#(1 point)
#
# 4) How do we put data into a function call?
#By parameters
#(1 point)
# 
# 5) How do we get data out of a function call?
#By return
#( 1 point)
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
#d3 =4
#(12 points)

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def Odd_Avg(input,total):

	Number = raw_input("Number: ")
	if Number== "":
#Base Case
		return raw_input("The Average of all the odd Number is: " + str(total)+ ".")
	else:
#Recursive Case
		Average=  float(total) % 2
		print "Odd Average: " +str(total) + "."
		return Odd_Avg(total) 


def average(sum, ct):
    n = raw_input("Next: ")
    if n == "":
        #BASE CASE
        return sum/ct
    else:
        #RECURSIVE CASE
        n = float(n)
        if n % 2 == 1:
            sum += n
            ct += 1
        return average(sum, ct)
def main():
    a = average(0.0 ,0.0)
    print "The average of your odd numbers was {}.".format(a)
main()

# +2 base case is present (MUST BE LABELED) (2 points)
# +2 recursive case is present (MUST BE LABELED) (2 points)
# +1 base case returns sum/ct (or equivalent) 
# +2 recursive case filters even numbers
# +1 recursive case increments sum and ct correctly
# +1 recursive case returns correct recursive call
# +1 main function present AND called  




