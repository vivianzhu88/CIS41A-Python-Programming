#Vivian Zhu
#Exercise 2

import turtle
g = turtle.Turtle()

class Line():
    def __init__(self, x1, y1, x2, y2):
        self.X1 = x1
        self.Y1 = y1
        self.X2 = x2
        self.Y2 = y2
        self.Draw()
        
    def getX1(self):
        return self.X1
        
    def getY1(self):
        return self.Y1
        
    def getX2(self):
        return self.X2
        
    def getY2(self):
        return self.Y2
    
    def Draw(self):
        g.penup()
        g.goto(self.X1, self.Y1)
        g.pendown()
        g.goto(self.X2, self.Y2)

def main():
    l = Line(90, 50, 90, 200)
    l.Draw()

main()

