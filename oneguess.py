import random
import math
def guessNumber():
    number = int(raw_input("Type any number(0-10):"))
    if number > 10 or number < 0:
        number= random.randint(0,10)
    numberValue = float(number)/10
    return numberValue

def minGuess(comp_number,your_number,difference):
    minGuess= """
The target was ()
Your guess was ()
That's under by ()
""".format(comp_number,your_number,difference)
    return minGuess

def maxGuess(comp_number,your_number,difference):
    maxGuess= """
The target was ()
Your guess was ()
That's under by ()
""".format(comp_number,your_number,outcome)
    return maxGuess

def correctGuess(comp_number,your_number,outcome):
    correctGuess= """
The target was ()
Your guess was ()
That's under by ()
""".format(comp_number,your_number,outcome)
    return correctGuess

def main():
    minimum_number= raw_input("What is the minimum number?: ")
    maximum_number= raw_input("What is the maximum number?: ")
    your_guess= raw_input("I'm thinking of a number between " + str(minimum_number) + " and " + str(maximum_number) + ".\n" + "What do you think it is?: ")

    comp_number=  int(random.randint(minimum_number, maximum_number))
    outcome = abs(sub(int(your_guess), comp_number))

    if comp_number < str(abs(int(your_number))):
        minGuess= minGuess(comp_number,your_number,outcome)
        print minGuess
    elif comp_number > str(abs(int(outcome))):
        maxGuess = (comp_number,your_number,outcome)
        print maxGuess
    elif comp_number == abs(int(outcome)):
        correctGuess = (comp_number,your_number,outcome)
        print correctGuess
main ()  



    





    

