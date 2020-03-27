#Vivian Zhu
#Final Review

class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def getQuantity(self):
        return self.quantity

class Device():
    def __init__(self, filename):
        self.filename = filename
        self.products = {}

    def readfile(self):
        handle = open(self.filename)
        for line in handle:
            s = line.rstrip()
            ss = s.split(",")
            self.products[ss[0]] = Product(ss[0], ss[1], ss[2])

    def search(self, name):
        for k in self.products:
            if k == name:
                print ("The price of " + name + " is $" + self.products[k].getPrice())

d = Device("Products.csv")
d.readfile()
d.search("Paper towels")
