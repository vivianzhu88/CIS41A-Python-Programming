#Vivian Zhu
#Exercise 3

def is_triangle(a, b, c):
    if ((a + b > c) and (b + c > a) and (a + c > b)):
        print("Yes")
    else:
        print("No")

def input_three():
    print("Input three sides of a triangle to check if it is valid")
    a = int(input("Enter the first side: "))
    b = int(input("Enter the second side: "))
    c = int(input("Enter the third side: "))
    is_triangle(a, b, c)
    
#tests
is_triangle(3, 4, 5) #Yes
is_triangle(10, 4, 5) #No
is_triangle(3, 9, 5) #No
is_triangle(3, 4, 8) #No

input_three()
