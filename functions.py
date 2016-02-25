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
addition1= add(8,7)
subtraction1= sub(6,4)
multiplication1= mul(4,2)
division1= div(8,2)
hours_to_seconds1= div(96400,3600)
area_of_circle1= circle_area(4)
volume_of_sphere1= sphere_volume(7)
average_volume1= avg_volume (20,40)
area_of_three_sides1= area(2,3,3.5)
right_align1= right_align( "Hey" )
center1= center("HaHaHa")
message_box_one1= msg_box("Hi")
message_box_two1= msg_box("I eat burgers!")
#Calling functions 2
addition2= add(3,5)
subtraction2= sub(6,1)
multiplication2= mul(3,2)
division2= div(10,5)
hrs_to_sec2= (76400,3600)
circle_area2= circle_area(3)
volume_of_sphere2= sphere_volume(9)
average_volume2= avg_volume (60,40)
area_of_three_sides2= area(4,6,6.5)
rightalign2= right_align("Bye")
center2= center("Goaway")
messagebox_one2= msg_box("Eww")
messagebox_two2= msg_box("I hate you")
#printing functions1
print msg_box (str(addition1))
print msg_box (str(subtraction1))
print msg_box (str(multiplication1))
print msg_box (str(division1))
print msg_box (str(hours_to_seconds1))
print msg_box (str(area_of_circle1))
print msg_box (str(volume_of_sphere1))
print msg_box (str(average_volume1))
print msg_box (str(area_of_three_sides1))
print msg_box (str(right_align1))
print msg_box (str(center1))
print msg_box (str(message_box_one1))
print msg_box (str(message_box_two1))
#printing functions2
print msg_box (str(addition2))
print msg_box (str(subtraction2))
print msg_box (str(multiplication2))
print msg_box (str(division2))
print msg_box (str(hrs_to_sec2))
print msg_box (str(circle_area2))
print msg_box (str(volume_of_sphere2))
print msg_box (str(average_volume2))
print msg_box (str(area_of_three_sides2))
print msg_box (str(rightalign2))
print msg_box (str(center2))
print msg_box (str(messagebox_one2))
print msg_box (str(messagebox_two2))

