#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a)5==5 (True)
#b)6<5 (False)
#c)7>3 (True)
#
#2) What does 'return' do?
#Spits out the output. Tells you what your function will do for the output.
#
#
#
#3) What are 2 ways indentation is important in python code?
#a)If you don't indent, your function will not be part of the function
#b)The indentation will tell you when your function will end.
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) 36
#problem1_b) sqrt 3
#problem1_c) 0
#problem1_d) -5
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) True
#
#problem3_a) 0.3 
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 1/6
#problem4_d) 5.0
#

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

    A =int(raw_input(" A :"))
    B =int(raw_input(" B : "))
    C =int(raw_input("C :"))
    #Processing
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


