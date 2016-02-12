#Added two arguments
def add(a,b):
    return a + b
y = add(7,7)
print y
#Subtracted two arguments
def sub(a,b):
    return a - b
x= sub(8,4)
print x
#Multiplied two arguments
def mul(a,b):
    return a*b
n= mul(9,2)
print n
#Divided two arguments
def div(a,b):
    return a/b
f= div(4,2)
print f
#Conversion of hours to seconds
def hours_from_seconds_div(a,b):
    return a/b
s= div(86400,3600)
print s
#Representation of a radius of a circle with one argument
def circle_area(r):
    return 3.14159265359 * (r**2)
print circle_area(5)
#Representation of a volume of the spere
def sphere_volume(v):
    return 3.14159265359 * 1.333333333333 * (v**3)
print sphere_volume(5)
#Representation of the average of the volumes
def avg_volume(a,b):
    return ((1.0/6 * 3.14159265359 * a**3) + (1.0/6 * 3.14159265359 * b**3)) /2
print avg_volume (10,20)
#Area of the three side lengths of a triangle
def area(a,b,c):
	n=(a+b+c)/2
	return (n*(n-a)*(n-b)*(n-c))**0.5

print area(1,2,2.5)
#String as an argument tht returns that word with additional spaces
def right_align(word):
	return (80-len(word))* " " + word
print right_align( "Hello" )
#String as an argument tht returns the spaces centered on the screen
def center(word):
    return (40-len(word))*" "+word
print center("Hello")
#Message Box
def msg_box(word):
    return "+" + (len(word)) +4 * "-") + "+"





