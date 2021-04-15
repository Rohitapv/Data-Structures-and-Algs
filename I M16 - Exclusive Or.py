Sample Input 0

11011
10101
Sample Output 0

01110

"""
a = int(input(), 2)  
b = int(input(), 2)  
c=a ^ b
print(bin(c).replace("b",""))
"""

def addZeros(strr, n):
    for i in range(n):
        strr = "0" + strr
    return strr

def getXOR(a, b):

    # Lengths of the given strrings
    aLen = len(a)
    bLen = len(b)

    if (aLen > bLen):
        b = addZeros(b, aLen - bLen)
    elif (bLen > aLen):
        a = addZeros(a, bLen - aLen)

    lenn = max(aLen, bLen);

    res = ""
    for i in range(lenn):
        if (a[i] == b[i]):
            res += "0"
        else:
            res += "1"

    return res

a = input()
b = input()

print(getXOR(a, b))
