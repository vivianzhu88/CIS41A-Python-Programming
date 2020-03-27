#Vivian Zhu
#Lab 3

import math

def shiftBits(number):
    log10 = math.log(number+1)
    log2 = log10 / math.log(2)
    shifts = math.ceil(log2)
    return shifts

#1 for loop
def bitPatternFOR(number):
    for i in range (shiftBits(number)-1, -1, -1):
        if (number & (1 << i) > 0):
            print(1, end = "")
        else:
            print(0, end = "")

#2 while loop
def bitPatternWHILE(number):
    i = shiftBits(number)
    while i > 0:
        i -= 1
        if (number & (1 << i) > 0):
            print(1, end = "")
        else:
            print(0, end = "")

bitPatternFOR(10)
print()
bitPatternWHILE(10)
