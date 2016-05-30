#def CountDown(x):
#	while 0 < x:
#		print x
#		x-=1
#CountDown(12)

#def Counter(x):
#	while 0 > x:
#		print x
#		x+=1
#	while 0 < x:
#		print x
#		x-=1
#Counter(-10)
#Counter(10)

#def CountFrom(x,y):
#	while x >= y:
#		print x
#		x-=1
#	while x <= y:
#		print x
#		x+=1
#CountFrom(5,0)
#CountFrom(0,5)

#def SumOfOdds(n):
#	if n > 0:
#		while n > 0:
#			if n % 2 == 1:
#				total += n
#			n -= 1
#	elif n < 0:
#		while n < 0:
#			if n % 2 == 1:
#				total += n
#			n+ = 1
#	return total
#print SumOfOdds(10)

def Grid(w, h):
	out = ""
	while h > 0:
		while w > 0:
			out += "."
			w -= 1
		out += "/n"
		h-= 1
		return out	
print Grid(5, 2)

		
