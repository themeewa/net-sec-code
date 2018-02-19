# take input packet
# calculate header part length
# extract payload part and look for #, return X, Y, N
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#Baby Step Giant Step DLP problem y = a**x mod n


#Example 70 = 2**x mod 131
# taking input from packet: N, 

y = 70
a = 2
n = 131

s = floor(sqrt(n))

A = []
B = []

for r in range(0,s):
    value = y*(a^r) % n
    A.append(value)

for t in range(1,s+1):
    value = a^(t*s) % n
    B.append(value)

print A
print B

x1,x2 =0,0
 
for r in A:
    for t in B:
        if r == t:
            x1 = A.index(r)            
            x2 = B.index(t)
            print x1,x2
            break
            

print 'the value of x is ', ((x2+1)*s - x1) % n # Answer