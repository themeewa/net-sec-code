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

def extended_eu_a(e,phiN):
	s = 0; old_s = 1
	t = 1; old_t = 0
	r = phiN; old_r = e
	while r != 0:
		quotient = old_r//r
		old_r, r = r, old_r%r
		old_s, s = s, old_s - quotient*s
		old_t, t = t, old_t - quotient*t
	return old_s
def cyclic(e,N):
	with open("./output_rahul.txt", "a") as ofile:
		C = int(input("enter the ciphertext C : "))
		k = 1
		flag = 1
		counter = 0
		while(flag == 1):
			print("counter : ",counter)
			counter = counter+1
			A = pow(C,pow(e,k),N)
			if (A == C):
				M = pow(C,pow(e,k-1),N)
				ofile.write("\nfound order k : "+str(k))
				print("found order k : ",k)
				print("M, C : ",M,C)
				flag = 0
			else:
				k= k+1
def computeNphiN(P,Q):
	with open("./output_rahul.txt", "a") as ofile:
		N = P*Q
		phiN = (P-1)*(Q-1)
		ofile.write("\ncomputing N = (P*Q) : "+str(N))
		ofile.write("\ncomputing phi(N) = (P-1)*(Q-1) : "+str(phiN))
		print("computing N = (P*Q) : ",N)
		print("computing phi(N) = (P-1)*(Q-1) : ",phiN)
		return N,phiN

def main():
	with open("./output_rahul.txt", "a") as ofile:
		P = int(input("enter number P : "))
		Q = int(input("enter number Q : "))
		N,phiN = computeNphiN(P,Q)
		e=int(input("enter the 'e' : "))
		# N=int(input("enter the 'N' : "))
		cyclic(e,N)
		d = extended_eu_a(e,phiN)
		d = d if d > 0 else phiN+d
		ofile.write("\nvalue of d : "+str(d))
		print("value of  d : ",d)
		ofile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
main()
