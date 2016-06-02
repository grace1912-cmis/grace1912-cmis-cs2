import random

def GuessingNumber(Number, Total):

    NumberGuess = int(raw_input("Guess a number: "))
    if NumberGuess  == Number:
        print "You got the answer in " + str(Total) + " tries."
    elif NumberGuess  == Number:
        print "GoodJob"
    elif NumberGuess  > Number:
        print "Too High"
        GuessingNumber(Number, Total + 1)
    else:
        print "Too Low"
        Total + 1
        GuessingNumber(Number,Total + 1)

GuessingNumber(random.randint(1, 10), 0)



