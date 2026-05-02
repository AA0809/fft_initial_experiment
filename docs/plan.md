# Plan

## Aims
I plan to use fft for my a-level cs project as its a complex project that appeals to me because of the applications with music and pitch-detection. 

This project specifically is called initial because it is my initial experimenting with fft, something rough to go alongside my reading of how it works.

Right now I plan to keep this maths focused, just because that is the context in which I am learning the algorithm (specifically multiplying polynomials)

I plan to code the coefficient method of polynomial multiplication, point method, and then implement fft to convert from coefficient to point representation (and back using the inverse version of this, not currently sure how different they are but i assume they are fairly similar). 

Also I will probably not use oop for now as this is just experimentation. I will naturally still use functions. I may also need numpy. not sure rn but I will give it a go without first

## Future plans
- I will possibly compare these two methods if I do a full test and can figure out how to collect information on run length
- I may from here, try and figure out pitch detection on my own. I already have an idea (by maintaining coefficients but switching to sinx, sin2x, etc. essentially stacking frequencies instead, i should be able to do the same thing with evaluation to convert to a sampled wave, and vice versa)