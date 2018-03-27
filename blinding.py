from random import randint
def getinv(r1,n):
	# with open("./output_rahul.txt", "a") as ofile:
	val = 1
	while (True):
		y = pow((x * r1),1,n)
		if y == 1:
			break
# 			exiting the inverse fun
		val = val + 1
	print("\ncalculated r-inverse : ",str(val))
	return val
def calcS(e,d,c,n):
	with open("./output_rahul.txt", "a") as ofile:
		ofile.write("\ngiven value e : "+str(e))
		ofile.write("\ngiven value d : "+str(d))
		ofile.write("\ngiven value n : "+str(n))
		ofile.write("\ngiven value c : "+str(c))
		r = randint(1, n-1)
		ofile.write("\n random r is taken as : "+str(r))
		print("\n random r is taken as : ",str(r))
		r1 = pow(r,1,n)
		x = getinv(r1,n)
		ofile.write("\ncalculated r-inverse : "+str(x))
		m1 = pow(pow(r,e)*c,1,n)
		ofile.write("\n m' is calculated as : "+str(m1))
		print("\n m' is calculated as : ",str(m1))
		s1 = pow(m1, d, n)
		ofile.write("\n s' is calculated as : "+str(s1))
		print("\n s' is calculated as : ",str(s1))

		s = (s1 * x) % n
		ofile.write("\n s is calculated as : "+str(s))
		print("\n s is calculated as : ",str(s))
	return s
def block(numb,n):
	with open("./output_rahul.txt", "a") as ofile:
		numstr=str(numb)
		counter=len(str(numb))
		# print("len : ",counter)
		cf=0
		ct=1
		block=[]
		while cf<counter and ct<=counter:
			# print(cf,ct)
			if int(numstr[cf:ct])<n:
				if (ct==counter):
					# print("\n last & less case",numstr[cf:ct])
					block.append(int(numstr[cf:ct]))
					return block
				# print("\n less case",numstr[cf:ct])
				ct=ct+1
			elif int(numstr[cf:ct])==n:
				# print("\n equal case",numstr[cf:ct])
				block.append(int(numstr[cf:ct]))
				cf=ct
				ct=cf+1
			elif int(numstr[cf:ct])>n:
				# print("\n grater  case",numstr[cf:ct])
				block.append(int(numstr[cf:ct-1]))
				cf=ct-1
				ct=cf+1
			# print(block)
		ofile.write("\n blocks are  : "+str(block))
		print("\n blocks are : ",str(block))
		return block
def main():
	with open("./output_rahul.txt", "a") as ofile:
		e = int(input("enter value of E: "))
		d = int(input("enter value of d: "))
		n = int(input("enter N: "))
		c = int(input("enter ciphertext: "))
		# e,d,n,c=5,173,323,15
		# sign = calcS(e,d,c,n)
		# print(block(c,n))
		# print(sign)
		method = int(input("enter 1 for block, or 2 for stream : "))
		# M = getM(c,d,n)
		if (method==1):
			blocks=block(c,n)
			for i in blocks:
				sign = calcS(e,d,int(i),n)
		if (method==2):
			quit=1
			while(quit != 'q' or quit!='Q'):
			 quit = int(input("enter the cipher chunk"))
			 calcS(e,d,quit,n)
main()
