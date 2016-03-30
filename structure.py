import math
def exp(e, x):
    return e ** x
def volumeOfsphere(v):
	return (4/3) * math.pi * (int(v) ** 3)
def volumeone(a):
	return float(a)
def volumeone(b):
	return float(b)
def volumeone(c):
	return float(c)
def totals(a,b,c):
	return (a+b+c)
def output (a,b,c,d):
    out = """
There are three spheres on the table. Sphere One has a volume of {}, Sphere Two has a volume of {}, and Sphere Three has a volume of {}. The total volume of three Spheres are {}.
""".format(a,b,c,d)
    return out
#Input
def main():
	a= int(raw_input("The radius of SphereOne : "))
	b= int(raw_input("The radius of SphereTwo: "))
	c= int(raw_input("The radius of SphereThree: "))
#Processing

	VolumeOne=volumeOfsphere(a)
	VolumeTwo=volumeOfsphere(b)
	VolumeThree=volumeOfsphere(c)
	d= totals(VolumeOne, VolumeTwo, VolumeThree)	
#Output
	out = output(VolumeOne, VolumeTwo, VolumeThree, d)


	print out
main()
