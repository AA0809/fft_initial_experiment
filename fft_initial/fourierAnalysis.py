import fourier
import math
bufferSize = 4096
sampleRate = 44100
freq = 440
buffer = [math.sin(2 * math.pi * freq * i / sampleRate) for i in range(bufferSize)]


def getFreqs(buffer, sampleFreq = None, sorted = True):
    if not sampleFreq:
        sampleFreq = len(buffer)
    f = list(map(abs,fourier.fft(buffer)))
    bufferSize = len(f)
    mult = sampleFreq / bufferSize
    n = bufferSize//2 + 1
    freqs = [None] * n
    for i in range(n):
        freqs[i] = (i*mult, f[i])
    
    if sorted:
        freqs.sort(reverse= True, key= lambda x: x[1])
    return freqs

def prettyPrint(freqs,n = None):
    if not n or n > len(freqs):
        n = len(freqs)
    for x in freqs[:n]:
        print(str(x[0]) + "Hz: " + str(x[1]))

# prettyprint the first n strongest frequencies
prettyPrint(getFreqs(buffer, sampleRate), 10)