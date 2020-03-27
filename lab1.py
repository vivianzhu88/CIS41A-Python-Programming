#Vivian Zhu
#Lab 1

#Exercise 2.2  #1-3 ********************************************************
#Question 1--------------------
import math
def sphereVol(radius):
    pi = math.pi
    volume = (4 / 3) * pi * (radius ** 3)
    print('The volume of a sphere with radius', radius, 'is', volume)
    
#Question 2--------------------
def discountTotal(price, discount, numBooks):
    discounted = price * (1 - discount) * numBooks
    return discounted
    
def shipTotal(numBooks):
    shipping =  3 + 0.75 * (numBooks - 1)
    return shipping
    
def totalPrice(price, discount, numBooks):
    total = (discountTotal(price, discount, numBooks)) + shipTotal(numBooks)
    print('The total price is $', total)

#Question 3--------------------
def easyPace(miles):
    time = ((8 * 60) + 15) * miles
    return time
    
def tempoPace(miles):
    time = ((7 * 60) + 12) * miles
    return time

def timeReturned(hourLeft, minLeft, secLeft, eMiles, tMiles):
    timeLeft = (((hourLeft * 60) + minLeft) * 60) + secLeft
    timeRan = easyPace(eMiles) + tempoPace(tMiles)
    finalTime = timeLeft + timeRan
    finalHrs = finalTime // (60 * 60)
    finalMins = (finalTime // 60) - (finalHrs * 60)
    finalSecs = finalTime - (finalHrs * 60 * 60) - (finalMins * 60)
    print('The time you get home is', finalHrs, ':', finalMins, ':', finalSecs, 'AM')

#Calling functions--------------------
sphereVol(5)
totalPrice(24.95, 0.4, 60)
timeReturned(6,52,0,2,3)

#p.27 #3.1, 3.2, 3.3 ********************************************************
#Question 3.1--------------------
def right_justify(s):
    spaces = ' ' * (70 - len(s))
    print(spaces + s)
    
right_justify('monty')
    
#Question 3.2--------------------
#part 1, 2
def do_twice(f, g):
    f(g)
    f(g)
    
def print_spam():
    print('spam')
    
#do_twice(print_spam) #this does not work anymore because I changed do_twice(f) to do_twice(f, g)
#part 3
def print_twice(g):
    print(g)
    print(g)
#part 4
do_twice(print_twice, 'spam')
#part 5
def do_four(f, g):
    do_twice(f, g)
    do_twice(f, g)

#Question 3.3--------------------
#part 1 two by two grid
def twoTimes(f):
    f()
    f()
    
def fourTimes(f):
    twoTimes(f)
    twoTimes(f)
      
def edge():
    print('+ - - - -', end = ' ')
    
def middle():
    print('|        ', end = ' ')

def twoCol():
    twoTimes(middle)
    print('|')

def twoRow():
    twoTimes(edge)
    print('+')
    fourTimes(twoCol)
    
def twoByTwo():
    twoTimes(twoRow)
    twoTimes(edge)
    print('+')

#part 2 four by four grid
def fourCol():
    fourTimes(middle)
    print('|')

def fourRow():
    fourTimes(edge)
    print('+')
    fourTimes(fourCol)
    
def fourByFour():
    fourTimes(fourRow)
    fourTimes(edge)
    print('+')

#printing the grids
twoByTwo()
print()
fourByFour()
    
    



