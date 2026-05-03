import fourier

# Test polynomials, should give [1, 4, 10, 20, 35, 56, 84, 120, 147, 164, 170, 164, 145, 112, 64], when multiplied
a = [1,2,3,4,5,6,7,8]
b = [1,2,3,4,5,6,7,8]


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
    return [a[i] * b[i] for i in range(len(a))]

def fftMult(a,b):
    n = len(a) + len(b) - 1
    c = pointMultiply(fourier.fft(a,n), fourier.fft(b,n))
    return fourier.inversefft(c)

print(coefficientMultiply(a,b))
print(fftMult(a,b))