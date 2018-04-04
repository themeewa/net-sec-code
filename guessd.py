import math, random

def guessd(e,C,phiN,N):
	with open("./output_rahul.txt", "a") as ofile:
		ofile.write("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
		# ofile.write("\ngiven value M : "+str(M))
		ofile.write("\ngiven value C : "+str(C))
		ofile.write("\ngiven N : "+str(N))
		ofile.write("\n given e  : "+str(e))
		ofile.write("\nguessing d now:")
		print("guessing d now:\n")
		C2=pow(C,e,N)
		for d in range(phiN):
			# ofile.write("\n"+str(d))
			C1=pow(C2,d,N)
			modofd=pow((e*d),1,phiN)
			if(C1==C and modofd==1):
				ofile.write("\nd guessed as : "+str(d))
				print("guessed d as : ",d)
				# print("d guess sccesfully as : "+str(d))
				return d
			else:
				ofile.write("\n not passed for d value  = "+str(d))
				print("unsuccesful value : ",d)
		ofile.write("\nd not guessed ")
		print("d guessing failed\n")
		return 0	

def main():
	with open("./output_rahul.txt", "a") as ofile:
		e=int(input("enter the 'e' : "))
		N=int(input("enter the 'N' : "))
		phiN =int(input("enter the phiN : "))
		C=int(input("enter the 'C' : "))
		# M=int(input("enter the 'M' : "))
		d = guessd(e,C,phiN,N)
		#change: stringify for file write
		if (d!=0):
			ofile.write("\nvalue of d : "+str(d))
		ofile.write("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
main()
