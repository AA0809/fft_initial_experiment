import math

# fourier.py
# A module for FFT-based polynomial multiplication and frequency analysis.
# Public functions: fft, inversefft
# Private functions (prefixed with _): _fftCall, _omega, _po2, _zeroPad


def fft(a, n = None):
    if not n:
        n = len(a)
    N = _po2(n)
    return _fftCall(_zeroPad(a, N), _omega(N), N)


def inversefft(a):
    # only works on a set of evaluations of length N where N is a _po2, and these evaluations are done using the root of unity. does order matter? idk tbh to think about
    n = len(a)
    return list(map(lambda x: x / n, _fftCall(a, _omega(-n), n)))


def _fftCall(a, unityRoot, n):
    if len(a) == 1:
        return a

    # something i really struggled to realise, aEven is not the polynomial function, it is a point representation of said polynomial
    aEven = _fftCall(a[::2], unityRoot ** 2, n // 2)
    aOdd = _fftCall(a[1::2], unityRoot ** 2, n // 2)
    aOut = [0] * n
    x = 1
    # mult odd by the appropriate root of unity and add even
    for i in range(0, n):
        j = i % (n // 2)
        aOut[i] = aEven[j] + aOdd[j] * x
        x *= unityRoot
    return aOut


def _omega(n):
    # using euler's formula on the first nth root of unity
    angle = 2 * math.pi / n
    return math.cos(angle) + 1j * math.sin(angle)


def _po2(x):
    num = 1
    while num < x:
        num *= 2
    return num

def _zeroPad(a, n):
    return a + [0] * (n - len(a))