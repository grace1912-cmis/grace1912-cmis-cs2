def countdown(n):
    if n<= 0:
        print "Blastoff!"
    else:
        print n
        countdown(n-1)
def countup(n):
    if n == 10:
        print "Blastoff!"
    else:
        print n
        countup(n+1)
def main():
    countdown(10)
    countup(-5)

main()

def count_up_from(start, stop):
    if start> stop:
        print "Blastoff!"
    else:
        print start
        count_up_from(start + 1,stop)
def count_down_from(start, stop):
    if start< stop:
        print "Blastoff!"
    else:
        print start
        count_down_from(start - 1, stop)
def main():
    count_up_from(-1,20)
    count_down_from(20, -1)

main()


#Adder
def adder(Number, total):
    Number = raw_input("Next number: ")
    if Number == '':
        print "The running total is: " + str(total) + "."
    else:
        total = total + float(Number)
        print "Running total: " + str(total) + "."
        return adder(Number, total)

adder("Number", 0)

#Biggest
def


        

