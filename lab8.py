#Vivian Zhu
#Lab 8

class Set():
    def __init__(self, theSet):
        s = theSet.split(",")
        self.one = int(s[0])
        self.two = int(s[1])
        
    def getOne(self):
        return self.one
    
    def getTwo(self):
        return self.two

    def __str__(self):
        return self.one + "," + self.two

class Circle():
    def __init__(self):
        self.section = 360/16
        self.hexDict = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        
    def degToHex(self, n):
        h = self.hexDict[n//self.section]
        return h
        
    def translate(self, setsList):
        hexes = []
        for s in setsList:
            hex1 = self.degToHex(s.getOne())
            hex2 = self.degToHex(s.getTwo())
            hexes.append(hex1 + hex2)
        return hexes

class AsciiTranslator():
    def __init__(self):
        self.c = Circle()

    def hexToDec(self, hexList):
        decs = []
        for h in hexList:
            for i in range(0, len(self.c.hexDict)):
                if h[0] == self.c.hexDict[i]:
                    dec1 = i
            for i in range(0, len(self.c.hexDict)):
                if h[1] == self.c.hexDict[i]:
                    dec2 = i
            decs.append(dec1*16 + dec2)
        return decs
    
    def decToAsc(self, decList):
        ascs = []
        ascs = list(map(lambda x:chr(x), decList))
        return ascs
        
        
class Device():
    def  __init__(self, filename):
        self.filename = filename
        self.setsList = []
        self.hexList = []
        self.decList = []
        self.ascList = []
        
    def read(self):
        handle = open(self.filename)
        rawData = []
        for line in handle:
            h = line.split("),")
            h.pop() #last element of list is " " so pop() is getting rid of it
            rawData += h
        nums = list(map(lambda x: x[1:], rawData))
        self.setsList = list(map(lambda x: Set(x), nums))


    def theText(self):
        c = Circle()
        self.hexList = c.translate(self.setsList)
        a = AsciiTranslator()
        self.decList = a.hexToDec(self.hexList)
        self.ascList = a.decToAsc(self.decList)

        [print(i, end = "") for i in self.ascList]
    
d = Device("Martian.csv")
d.read()
d.theText()
