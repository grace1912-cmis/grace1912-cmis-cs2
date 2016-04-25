#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a)5==5 (True)
#b)6<5 (False)
#c)7>3 (True)

#(+3 points)
#
#2) What does 'return' do?
#Spits out the output. Tells you what your function will do for the output.
#(+1 point)

#
#
#3) What are 2 ways indentation is important in python code?
#a)If you don't indent, your function will not be part of the function
#b)The indentation will tell you when your function will end.
#
#(+1 Point)

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) -36
#problem1_b) sqrt 3
#problem1_c) 0
#problem1_d) -5
#(+3 points)
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) True
#(+4 points)
#
#problem3_a) 0.3 
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5

#(+4 points)
#problem4_a) 7
#problem4_b) 5
#problem4_c) 1/6
#problem4_d) 5.0

#(+2 points)

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)
import math



def number(A):
    return float(A)
def number(B):
    return float(B)
def number(C):
    return float(C)
def output(A,B,C):
    out= """
A = {}
B = {}
C = {}
 """.format(A,B,C)
    return out

   
def main():
    #Input
    Number= raw_input("Type three different numbers (decimals are OK) :")

    A =float(raw_input(" A :"))
    B =float(raw_input(" B : "))
    C =float(raw_input("C :"))
    #Processing
def number(A , B, C):
	if A > B and A > C:
		return A
	elif B > A and B > C:
		return B
	else:
		return C

if float(A > B):
    print A
elif float(B > C):
    print B
elif float(C > A):
    print C
elif float(A > C):
    print A
elif float(B > A):
    print B
elif float(C > B):
    print C
else:
    print "You didn't follow the directions"
    #Output
    print output(A,B,C)
main()
# +1 correct function headers (ALL MUST BE CORRECT) (+1)
# +1 correctly structured script: 
#	 (main function defined, process functions defined, process functions called in main, calls main) 

# +1 use if...elif...else or an equivalent structure (+1)
# +1 uses a boolean expression to test numbers (+1)
# +1 CORRECTLY determines and returns largest number (+1)
# +1 gets and converts 3 values correctly (+1)
# +1 uses conditional to give feedback if numbers are not all different (+1)



main()

