import math

# Test polynomials, should give [1, 4, 10, 20, 35, 56, 84, 120, 147, 164, 170, 164, 145, 112, 64], when multiplied
acoeff = [1,2,3,4,5,6,7,8]
bcoeff = [1,2,3,4,5,6,7,8]

apoints = [1,2,3,4,5,6,7,8]
bpoints = [1,2,3,4,5,6,7,8]



def coefficientMultiply(a, b):
    # my own algorithm for multiplication of two polynomials. systematically multiplys every number by every other number, and adds the result into the correct list index
    # I initially compared degrees to make sure they were equal, which is necessary for fft, but i realised its not necessary here
    
    n1 = len(a)
    n2 = len(b)
    outputCoeff = [0] * (n1 + n2 -1)
    for i in range(n1):
        for j in range(n2):
            mult = a[i] * b[j]
            outputCoeff[i + j] += mult
            
    return outputCoeff

def pointMultiply(a,b):
    if len(a) != len(b):
        raise ValueError("equal number of points required for point multiply")
    return [x := a[i] * b[i] for i in range(len(a))]

# I need to give omega because it would be dumb to calculate it each time.
# similar for n though it is much easier to calculate n
def fft(a, unityRoot, n):
    if len(a) == 1:
        return a
    
    # something i really struggled to realise, aEven is not the polynomial function, it is a point representation of said polynomial)
    aEven = fft(a[::2], unityRoot **2, n//2)
    aOdd = fft(a[1::2], unityRoot **2, n//2)
    aOut = [0] * n
    x = 1
    # mult odd by the appropriate root of unity and add even
    for i in range(0, n):
        j = i % (n//2)
        aOut[i] = aEven[j] + aOdd[j] * x
        x *= unityRoot
    return aOut

    # to summarise my understanding - for each polynomial, it evaluates two polynomials of half size, and half the points, but gets double the points by multiplying by all of the nth unity roots against a doubled set of the points (because j and j+n/2 evaluate the same for the previous polynomial because their square is the same)
    # crap explanation but i just about understand. perhaps i will write up a better intuitive explanation.
    
def fftCall(a,n):
    N = nearestPO2(n)
    return fft(zeroPad(a,N), omega(N), N)

def nearestPO2(x):
    po2 = 1
    while po2 < x:
        po2 *= 2
    return po2

def zeroPad(a,n):
    a += [0] * (n-len(a))
    return a
    
def omega(n):
    #using euler's formula on the first nth root of unity
    angle = 2 * math.pi / n
    return math.cos(angle) + 1j * math.sin(angle)
    
def inverseFFt(a):
    # only works on a set of evaluations of length N where N is a po2, and these evaluations are done using the root of unity. does order matter? idk tbh to think about
    n = len(a)
    return list(map(lambda x: x / n, fft(a,omega(-n), n)))

def fftMult(a,b):
    n = len(a) + len(b) - 1
    c = pointMultiply(fftCall(a,n), fftCall(b,n))
    return inverseFFt(c)

print(coefficientMultiply(acoeff,bcoeff))
print(pointMultiply(apoints,bpoints))
print(fftMult(acoeff,bcoeff))
print(omega(4))