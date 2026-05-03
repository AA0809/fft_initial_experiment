# Log

## 2/5/26
I decided to try less robust documentation (compared to my previous maths engine project) as that was a bit too much and honestly detracting from the actual project

- Researched how fft works
- Updated plan.md with initial aims/scope
- Coded coeff and point mults. 
- Found out python handles imaginary numbers correctly (using j)
- coded fft

## 3/5/26
Successfully coded inverse fft, omega function, zero padding to the next po2, and tested and bugfixed. It works! I tested by comparing to my coefficient multiplication and they gave the same output (albeit with some noise from the floating points numbers)

I started researching how this applies to sound. From my understanding, by taking a sample buffer and running it through fft, evaluating at roots of unity, and finding the magnitude of the complex outputs, we get the magnitudes of different frequencies, plus a mirror. As of time of writing, I don't really understand how we know which frequencies they are (ie sample buffer size vs sample rate calculations). additionally i do not know why this works. But for the most part i understand this to be an application of the fft function. I will try code this, and also read up on they why behind the fourier analysis. 
