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
    if n >= start:
        print "Blastoff!"
    if n >= stop:
        print "Blastoff!"
    else:
        print n
        count_up_from(start,stop)
def main():
    count_up_from(-1,20)

main()
        
        

