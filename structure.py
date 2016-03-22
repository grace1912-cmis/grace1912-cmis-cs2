import math
def exp(e, x):
    return e ** x
def volumeOfsphere(v):
	volume = (4/3) * math.pi * (v ** 3)
def totals(a, b, c):
	return a + b + c
def output (VolumeOne, VolumeTwo, VolumeThree, d):
    out = """
There are three spheres on the table. Sphere One has a volume of {}, Sphere Two has a volume of {}, and Sphere Three has a volume of {}. The total volume of three Spheres are {}.
""".format(VolumeOne,VolumeTwo ,VolumeThree, d)
    return out

def main():
	a= int(raw_input("The radius of SphereOne : "))
	b= int(raw_input("The radius of SphereTwo: "))
	c= int(raw_input("The radius of SphereThree: "))
	d= totals(VolumeOne, VolumeTwo, VolumeThree)
out = output (VolumeOne, VolumeTwo, VolumeThree, d)
VolumeOne=int(volumeOfsphere(a))
VolumeTwo=int(volumeOfsphere(b))
VolumeThree=int(volumeOfsphere(c))


print out
main()
