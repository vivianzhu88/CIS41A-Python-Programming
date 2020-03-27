#Vivian Zhu
#Lab 0
#Exercise 2.2 #1-3

import math

#Question 1
radius = 5
pi = math.pi
volume = (4 / 3) * pi * (radius ** 3)
print("The volume of a sphere with radius", radius, "is", volume)

#Question 2
price = 24.95
bookstorePrice = price * (1.0 - 0.4)
numBooks = 60
shipping =  3 + 0.75 * (numBooks - 1)
total = (bookstorePrice * 60) + shipping
print("The total price is $", total)

#Question 3
timeLeft = ((6 * 60) + 52) * 60
easyPace = (8 * 60) + 15
tempoPace = (7 * 60) + 12
timeRan = easyPace + (3 * tempoPace) + easyPace
finalTime = timeLeft + timeRan
finalHrs = finalTime // (60 * 60)
finalMins = (finalTime // 60) - (finalHrs * 60)
finalSecs = finalTime - (finalHrs * 60 * 60) - (finalMins * 60)
print("The time you get home is", finalHrs, ":", finalMins, ":", finalSecs, "AM")

