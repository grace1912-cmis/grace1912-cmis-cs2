#Created a variable defining my name.
myName ="Inhye Kim" 
print myName
#Created a variable defining my age.
ageInYears = 16.9
print ageInYears
#Created a variable defining my height in meters.
heightInMeters = 1.66
print heightInMeters
#Created a variable defining the length of a square.
lengthOfSquare = 8
print lengthOfSquare
#Created a variable defining the length of a rectangle.
lengthOfRectangle = 16
print lengthOfRectangle
#Created a variable defining the height of a rectangle.
heightOfRectangle = 2
print heightOfRectangle
#Created a variable defining number of months in a year.
monthsInYear = 12
#Created a variable explaning how to find my age in months.
ageInMonths = ageInYears * monthsInYear
print ageInMonths
#Created a variable defining the years left to live.
yearsLeftToLive = 100
#Created a variable explaining how to find out my years to live.
yearsToLive = ageInYears + yearsLeftToLive
print yearsToLive
#Created a variable defining my height in feet.
heightInFeet = heightInMeters * 3.28084
print heightInFeet
#Created a variable defining the average height of korean girls.
koreanGirlsAverageHeight= 5.73 *3.28084
#Created a variable defining difference of height.
differenceOfHeight= koreanGirlsAverageHeight - heightInMeters
print differenceOfHeight
#Created a variable defining the area of a square.
areaOfSquare = lengthOfSquare * lengthOfSquare
print areaOfSquare
#Created a variable defining the half volume of a cube.
halfVolumeOfCube= 0.5 * (lengthOfSquare ** 3)
print halfVolumeOfCube
#Created a variable defining the ninth area of a rectangle.
ninthAreaOfaRectangle= 0.11 * lengthOfRectangle * heightOfRectangle
print ninthAreaOfaRectangle
#Printed out a message using 5 variables using (+) as a string concatenation operator.
print "Hallo,I'm" + str(myName) + "." + "I'm" + str(heightInMeters) + "meters tall" + "." + "My height in feet is" + str(heightInFeet) + "." + "I'm" + str(ageInYears) + "years old" + "." + "I have" + str(yearsLeftToLive) + "left to live" + "." + str(yearsToLive) + "sums up the years I will live before I die" + "."
#Printed out a message using the other 5 variables using (,) as a string concatenation operator.
print "Hi,the average height of Korean girls is " , str(koreanGirlsAverageHeight), "." , "The difference of height from the average Korean girls height is," , str(differenceOfHeight), "." , "I love rectangles" , "." , "The length of my rectangle is" , str(lengthOfRectangle) , "." , "Its height is" , str(heightOfRectangle), ".", "The ninth area of my rectangle is" , str(ninthAreaOfaRectangle), "."
# styped 1000 smiley faces.
smilelyFace = ";)"
print smilelyFace * int(10000)
