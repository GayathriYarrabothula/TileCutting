import sys

def noOfDivisors(n):
    sum1 = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum1 += 1
    return sum1

def createList(area):
    l = []
    for i in range(1, area):
        l.append([i, area - i])
    return l

def noOfPosibilities(area):
    sum2 = 0
    l = createList(area)
    for i in l:
        sum2 += noOfDivisors(i[0]) * noOfDivisors(i[1])
    return sum2

def printMaxm(d):
    maxm = 0
    for k, v in d.items():
        if maxm < v:
            maxm = v
            area = k
    return area, maxm
    
t = int(sys.argv[1])
for i in range(0, 2 * t - 1, 2):
    d = {}
    alow, ahigh = int(sys.argv[i + 2]), int(sys.argv[i + 3])
    for i in range(alow, ahigh + 1):
        d[i] = noOfPosibilities(i)
    print(printMaxm(d)[0], printMaxm(d)[1])
