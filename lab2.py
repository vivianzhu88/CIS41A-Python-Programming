#Vivian Zhu
#Lab 2

import turtle
g = turtle.Turtle()

class Line():
    def __init__(self, x1, y1, x2, y2):
        self.X1 = x1
        self.Y1 = y1
        self.X2 = x2
        self.Y2 = y2
        
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

class Square():
    def __init__(self, x, y, l):
        self.X = x
        self.Y = y
        self.L = l
        
    def getX(self):
        return self.X
        
    def getY(self):
        return self.Y
        
    def getL(self):
        return self.L

    def Draw(self):
        g.color("green")
         
        l1 = Line(self.X, self.Y, self.X + self.L, self.Y)
        l2 = Line(self.X + self.L, self.Y, self.X + self.L, self.Y - self.L)
        l3 = Line(self.X + self.L, self.Y - self.L, self.X, self.Y - self.L)
        l4 = Line(self.X, self.Y - self.L, self.X, self.Y)

        l1.Draw()
        l2.Draw()
        l3.Draw()
        l4.Draw()

class Triangle():
    def __init__(self, x, y, w, h):
        self.X = x
        self.Y = y
        self.W = w
        self.H = h
        
    def getX(self):
        return self.X
        
    def getY(self):
        return self.Y
        
    def getW(self):
        return self.W

    def getH(self):
        return self.H

    def Draw(self):
        g.color("blue")
        
        l1 = Line(self.X, self.Y, self.X + self.W/2, self.Y - self.H)
        l2 = Line(self.X + self.W/2, self.Y - self.H, self.X - self.W/2, self.Y - self.H)
        l3 = Line(self.X - self.W/2, self.Y - self.H, self.X, self.Y)

        l1.Draw()
        l2.Draw()
        l3.Draw()

class Circle():
    def __init__(self, x, y, r):
        self.X = x
        self.Y = y
        self.R = r

    def getX(self):
        return self.X
        
    def getY(self):
        return self.Y
        
    def getR(self):
        return self.R

    def Draw(self):
        g.penup()
        g.goto(self.X, self.Y)
        g.color("magenta")
        g.pendown()
        g.circle(self.R)

class Star():
    def __init__(self, x, y, l):
        self.X = x
        self.Y = y
        self.L = l
        
    def getX(self):
        return self.X
        
    def getY(self):
        return self.Y
        
    def getL(self):
        return self.L

    def Draw(self):
        g.penup()
        g.goto(self.X, self.Y)
        g.color("pink")
        g.pendown()
        
        g.forward(self.L)
        g.right(144)
        g.forward(self.L)
        g.right(144)
        g.forward(self.L)
        g.right(144)
        g.forward(self.L)
        g.right(144)
        g.forward(self.L)
        g.right(144)
        
def main():
    s = Square(100, 200, 100)
    s.Draw()

    t = Triangle(-150, 200, 100, 100)
    t.Draw()

    c = Circle(-150, -150, 50)
    c.Draw()

    s = Star(100, -100, 100)
    s.Draw()

main()

