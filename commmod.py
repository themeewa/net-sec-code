import math, random

def gcd_ea(a,b):
	r0=a
	r1=b
	r2=1
	q=0
	while(r2!=0):
		q = r0/r1
		r2 = r0 - q*r1
		r0 = r1
		r1=r2
	return r0

def extended_eu_a(e1,e2):
	s = 0; old_s = 1
	t = 1; old_t = 0
	r = e2; old_r = e1
	while r != 0:
		quotient = old_r//r
		old_r, r = r, old_r - quotient*r
		old_s, s = s, old_s - quotient*s
		old_t, t = t, old_t - quotient*t
	return old_s,old_t,old_r
def getciphers(e1,e2,n):
	m = int(input("enter the message"))
	c1 = pow(pow(m,e1),1,n)
	c2 = pow(pow(m,e2),1,n)
	print("value of  c1 : ",c1)
	print("value of  c2 : ",c2)
	return m,c1,c2
def commN(x,y,c1,c2,N):
	if (x<=0):
		print("x is negative")
		temp = extended_eu_a(c1,N)
		c1 = int(temp[0])
		return commN(x,y,c1,c2,N)
	if (y<=0):
		print("x is negative")
		temp = extended_eu_a(c2,N)
		c2 = int(temp[0])
		return commN(x,y,c1,c2,N)
	c11=pow(c1,x)
	c22=pow(c2,y)
	c12 = int(c11*c22)
	m = c12%N
	return m
def main():
	with open("./output_rahul.txt", "a") as ofile:
		e1=int(input("enter the 'e1' : "))
		e2=int(input("enter the 'e2' : "))
		c1=int(input("enter the 'c1' : "))
		c2=int(input("enter the 'c2' : "))
		N=int(input("enter the 'N' : "))
		m = int(input("enter the message"))		
		x,y,gcd=extended_eu_a(e1,e2)
		if (gcd!=1):
			print("inverse found error")
			# break;
		# m,c1,c2 = getciphers(e1,e2,N)
		ofile.write("\ngiven value of e1 : "+str(e1))
		ofile.write("\ngiven value of e2 : "+str(e2))
		ofile.write("\ngiven value of c1 : "+str(c1))
		ofile.write("\ngiven value of c2 : "+str(c2))
		ofile.write("\ngiven value of N : "+str(N))
		print("value of  x : ",x)
		print("value of  y : ",y)
		ofile.write("\ngiven value of x : "+str(x))
		ofile.write("\ngiven value of y : "+str(y))
		mes = commN(x,y,c1,c2,N)
		ofile.write("\nmessage decoded : "+str(mes))
		print("message decoded : ",mes)
		print("expected value of message : ",m)

main()
