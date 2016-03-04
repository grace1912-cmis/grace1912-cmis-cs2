import math
def exp(e, x):
    return e ** x
def volumeOfsphere(v):
	volume = (4/3) * math.pi * (v ** 3)
def totals(a, b, c):
	return a + b + c
def output (a, b, c, d):
    out = """
There are three spheres on the table. Sphere One has a volume of {}, Sphere Two has a volume of {}, and Sphere Three has a volume of {}. The total volume of three Spheres are {}.
""".format(a, b, c, d)
    return out

def main():
	a= int(raw_input("The radius of SphereOne : "))
	b= int(raw_input("The radius of SphereTwo: "))
	c= int(raw_input("The radius of SphereThree: "))
	d= totals(a, b, c)
	out = output(a, b, c, d)
	print out
main()
