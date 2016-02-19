import math
def exp(e, x):
    return e ** x
def output (name, e, x, y):
    out = """
Hey {} !
Did you know:
{} ** {} = {}
""".format(name, e, x, y)
    return out

def main():
   
    name = raw_input("What is your name? : ")
    e= int(raw_input("Type a number: "))
    x= int(raw_input("Type another: "))
    y= exp(e, x)

    out = output(name, e, x, y)
    print out

main()
