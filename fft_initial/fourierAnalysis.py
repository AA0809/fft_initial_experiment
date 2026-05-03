import fourier

buffer = [1,0,-1,0]

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

def prettyPrint(freqs):
    for x in freqs:
        print(str(x[0]) + "Hz: " + str(x[1]))

prettyPrint(getFreqs(buffer))