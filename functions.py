#Added two arguments
def add(a,b):
    return a + b
print add(7,7)

#Subtracted two arguments
def sub(a,b):
    return a - b
print sub(8,4)

#Multiplied two arguments
def mul(a,b):
    return a*b
print mul(9,2)

#Divided two arguments
def div(a,b):
    return a/b
print div(4,2)

#Conversion of hours to seconds
def hours_from_seconds_div(a,b):
    return a/b
print div(86400,3600)

#Representation of a radius of a circle with one argument
def circle_area(r):
    return 3.14159265359 * (r**2)
print circle_area(5)
#Representation of a volume of the spere
def sphere_volume(v):
    return 3.14159265359 * 1.333333333333 * (v**3)
print sphere_volume(5)
#Representation of the average volumes
def avg_volume(a,b):
    return ((1.0/6 * 3.14159265359 * a**3) + (1.0/6 * 3.14159265359 * b**3)) /2
print avg_volume (10,20)
#Area of the three side lengths of a triangle
def area(a,b,c):
	n=(a+b+c)/2
	return (n*(n-a)*(n-b)*(n-c))**0.5

print area(1,2,2.5)
#String as an argument that returns the word with additional spaces
def right_align(word):
	return (80-len(word))* " " + word
print right_align( "Hello" )
#String as an argument that returns the spaces centered on the screen
def center(word):
    return (40-len(word))*" "+word
print center("Hello")
#Defineing a function that takes a string as an argument and returning a Message Box
def msg_box(x):
    return "+" + ((len(x)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (x)+ (2*" ") + "|" + "\n" + "+" + ((len(x)+4)*"-") + "+"
print msg_box("Hello")
#Returning a message box with the given phrase
print msg_box("I eat cats!")


#Calling functions1
addition= add(8,7)
a=8
b=7
q= add(a,b)
print msg_box(str(q))
subtraction= sub(6,4)
a=6
b=4
q= sub(a,b)
print msg_box(str(q))
multiplication= mul(4,2)
a=4
b=2
q= mul(a,b)
print msg_box(str(q))
division= div(8,2)
a=8
b=2
q= div(a,b)
print msg_box(str(q))
hours_to_seconds= div(96400,3600)
a=96400
b=3600
q= div(a,b)
print msg_box(str(q))
area_of_circle= circle_area(4)
a=4
print msg_box(str(a))
volume_of_sphere= sphere_volume(7)
a=7
print msg_box(str(a))
average_volume= avg_volume (20,40)
a=20
b=40
print msg_box(str(average_volume))
area_of_three_sides= area(2,3,3.5)
a=2
b=3
c=3.5
print msg_box(str(area_of_three_sides))
right_align= right_align( "Hey" )
print msg_box(str(a))
center= center("HaHaHa")
a= "HaHaHa"
print msg_box(str(a))
message_box_one= msg_box("Hi")
print msg_box(str(message_box_one))
message_box_two= msg_box("I eat burgers!")
print msg_box(str(message_box_two))
#Calling functions 2
z= add(3,5)
a=3
b=5
print msg_box(str(z))
s= sub(6,1)
a=6
b=1
print msg_box(str(s))
m= mul(3,2)
a=3
b=2
print msg_box(str(m))
d= div(10,5)
a=10
b=5
q= div(a,b)
print msg_box(str(q))
hrs_to_sec= (76400,3600)
a=76400
b=3600
c= div(76400, 3600)
print msg_box(str(c))
c_a= circle_area(3)
a=3
print msg_box(str(c_a))
v_s= sphere_volume(9)
a=9
print msg_box(str(v_s))
a_v= avg_volume (60,40)
a=60
b=40
print msg_box(str(a_v))
a_th_s= area(4,6,6.5)
a=4
b=6
c=6.5
print msg_box(str(a_th_s))
r_a= right_align("Bye")
a= "Bye"
print msg_box(str(right_align("Bye"))
c = center("Goaway")
a= "Goaway"
print msg_box(str(a))
mb1= msg_box("Eww")
print msg_box(str(mb1))
mb2= msg_box("I hate you")
print msg_box(str(mb2))
