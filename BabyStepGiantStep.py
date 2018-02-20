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
        # print("protocol : ",int(data[18:20], 16))
        # print("total lemgth : ",int(data[4:8], 16))
        # print("packet header leangth : ",int(data[1:2], 16) * 8)
        tcp_packet_length = int(data[4:8], 16) - (int(data[1:2], 16) * 8)
        # print("tcp packet lemgth : ",tcp_packet_length)
        data = data[(int(data[1:2], 16) * 8):]
        # print("tcp/udp packet",data)

        if protocol == 1:
            data = data[40:]
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
            print("protocol 6 data offset value: ",int(data[24:25], 16))
            data = data[int(data[24:25], 16) * 8:]
            data = data.split("#")
            print(data)
            return int(data[0], 16), int(data[1], 16), int(data[2], 16)

# get x y n from ipv6 packet
def getXYN6(data):
        # next_header = data[12:14]
        data = data[80:]
        if int(data[12:14], 16) == 17 or int(data[12:14], 16) == 58:
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
    # with open("./output.txt", "a") as ofile:
        # ofile.write("sorted value: \n")
        # print("pairs before sorting",pairs)
        sortedPairs=[]
        sortedPairs = sorted(pairs, key=lambda x: x[0])
        # ofile.write("sorted value: \n")
        # ofile.write(str(sortedPairs))
        # ofile.write("\n")
        # print("sorted value: \n",sortedPairs)
        return sortedPairs

def getSvalues(y,n,a):
    with open("./output.txt", "a") as ofile:
        s= int(floor(sqrt(n)))
        ofile.write("using s = square root of n: ")
        ofile.write(str(s))
        ofile.write("\n")
        ofile.write("\n")
        # print("using s = suare root of n: ",s)
        # print(s)
        Svalues = []
        for r in range(s):
            Svalues.append([(y*pow(a,r))%n,r])
            # print("in for")
        # print("in file writes")
        # ofile.write("\n")
        ofile.write("S, (y* (a to the power r) % n, r)\n")
        ofile.write(str(Svalues))
        ofile.write("\n")
        ofile.write("\n")
        # ofile.write("\n")
        print("S, (y* (a to the power r) % n, r)\n", Svalues)
        sortedSvalues = getSorted(Svalues)
        ofile.write("sorted S: \n")
        ofile.write(str(sortedSvalues))
        ofile.write("\n")
        ofile.write("\n")
        return sortedSvalues

def getTvalues(y,n,a):
    s= int(floor(sqrt(n)))
    with open("./output.txt", "a") as ofile:
        Tvalues = []
        for x in range(1,int(s+1)):
            Tvalues.append([(pow(a,x*s))%n,x*s])
        ofile.write("T, (a to the power r*s) % n, r*s)\n")
        ofile.write(str(Tvalues))
        ofile.write("\n")
        ofile.write("\n")
        print("T, (a to the power r*s) % n, r*s)\n", Tvalues)
        sortedTvalues = getSorted(Tvalues)
        ofile.write("sorted T: \n")
        ofile.write(str(sortedTvalues))
        ofile.write("\n")
        ofile.write("\n")
        return sortedTvalues
# 
def solve(y, n, x):
        S = getSvalues(y,n,x)
        T = getTvalues(y,n,x)
        with open("./output.txt", "a") as ofile:
            Results = []
            ofile.write("comparing y*(a^r) from S to a^(t*s) from T\n")
            ofile.write("\n")
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
                ofile.write("\n")
                Yvalue  = pow(x[1],r) % n
                # print("y : " , Yvalue)
                # ofile.write("\nThe value of y is\n")
                # ofile.write(str(Yvalue))

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
