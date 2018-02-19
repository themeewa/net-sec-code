from math import sqrt, floor

# get version
def getVERSION(packetdata):
    print("DATA PASSED TP FUN",packetdata)
    if (int(packetdata[0], 16) == 4):
        return 4
    else:
        return 6
# get x y n from ipv4 packet
def getXYN4(data):
        protocol = int(data[18:20], 16)
        tcp_packet_length = int(data[4:8], 16) - (int(data[1:2], 16) * 8)
        data = data[(int(data[1:2], 16) * 8):]

        if protocol == 1:
            data = data[16:]
            print(data)
            data = data.split('#')
            return int(data[0], 16), int(data[1], 16), int(data[2], 16)
        elif protocol == 17:
            data = data[16:]
            print(data)
            data = data.split('#')
            return int(data[0], 16), int(data[1], 16), int(data[2], 16)

        elif protocol == 6:
            # TCP data
            # tcp_header_length = int(data[24:25], 16) * 8
            data = data[int(data[24:25], 16) * 8:]
            data = data.split("#")
            return int(data[0], 16), int(data[1], 16), int(data[2], 16)

# get x y n from ipv6 packet
def getXYN6(data):
        # next_header = data[12:14]
        data = data[80:]
        if data[12:14] == 17 or data[12:14] == 58:
            # icmp packet
            data = data[16:]
            print(data)
            data = data.split('#')
            return int(data[0], 16), int(data[1], 16), int(data[2], 16)

        if data[12:14] == 6:
            # TCP data
            # tcp_header_length = int(data[24:25], 16) * 8
            data = data[int(data[24:25], 16) * 8:]
            data = data.split("#")
            return int(data[0], 16), int(data[1], 16), int(data[2], 16)
# 
# meewa
def getSorted(pairs):
    with open("./output.txt", "a") as ofile:
        ofile.write("sorted value: \n")
        sortedPairs = sorted(pairs, key=lambda x: x[0])
        ofile.write("sorted value: \n")
        ofile.write(sortedPairs)
        ofile.write("\n")
        print("sorted value: \n",sortedPairs)
        return sortedPairs

def getSvalues(y,n,a):
    s= int(floor(sqrt(n)))
    print("using s = suare root of n: ")
    print(s)
    with open("./output.txt", "a") as ofile:
        ofile.write("using s = suare root of n: ")
        ofile.write(str(s))
        ofile.write("\n")
        Svalues = []
        for r in range(s):
            Svalues.append((y*pow(a,x))%n,)
        ofile.write("S, (y* (a to the power r) % n, r)\n")
        ofile.write(Svalues)
        ofile.write("\n")
        print("S, (y* (a to the power r) % n, r)\n", Svalues)
        sortedSvalues = getSorted(Svalues)
        return sortedSvalues

def getTvalues(y,n,a):
    s= floor(sqrt(n))
    with open("./output.txt", "a") as ofile:
        Tvalues = []
        for x in range(1,s+1):
            Tvalues.append((pow(a,x*s))%n,x*s)
        ofile.write("T, (a to the power r*s) % n, r*s)\n")
        ofile.write(Tvalues)
        ofile.write("\n")
        print("T, (a to the power r*s) % n, r*s)\n", Tvalues)
        sortedTvalues = getSorted(Tvalues)
        return sortedTvalues
# 
def solve(y, n, x):
    with open("./output.txt", "a") as ofile:
        S = getSvalues(y,n,x)
        T = getTvalues(y,n,x)
        Results = []
        ofile.write("comparing y*(a^r) from S to a^(t*s) from T\n")
        x=0
        z=0
        for  x in S:
            for z in T:
                if x[0] == z[0]:
                    Results.append(z[1] - x[1])
        for r in Results:
            print("\nrequired value of k, in y = x^k mod n is ", r)
            ofile.write("required value of k, in y = x^k mod n is ")
            ofile.write(str(r))
            Yvalue  = pow(x,r) % n
            print("y : " , Yvalue)
            ofile.write("\nThe value of y is\n")
            ofile.write(str(Yvalue))

if __name__ == "__main__":
    with open('packet.txt') as packet:
        print(packet)
        packetdata =packet.readlines()
        print(packetdata)
        for data in packetdata:
            version = getVERSION(data)
            if (version==4):
                print("version 4 ")
                x, y, n = getXYN4(data)
                print(x, y, n)
                solve(y, n, x)
            elif (version==6):
                print("version 6")
                x, y, n = getXYN6(data)
                print(x, y, n)
                solve(y, n, x)
