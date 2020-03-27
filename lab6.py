#Vivian Zhu
#Lab 6

class Person():
    def __init__(self, line):
        s = line.rstrip()
        ss = s.split(",")
        self.first = ss[0]
        self.last = ss[1]
        self.room = ss[2]
    def __str__(self):
        return self.last + ", " + self.first + " : Room " + self.room
    def __lt__(self, rhs):
        return self.last + self.first < rhs.last + rhs.first
    def __eq__(self, rhs):
        return self.last + self.first == rhs.last + rhs.first

class Hotel():
    def __init__(self, filename):
        self.filename = filename
        self.directory = {}
    
    def read(self):
        handle = open(self.filename)
        for line in handle:
            person = Person(line)
            self.directory[int(person.room)] = person

    def printRoomOrder(self):
        print("HOTEL IN ROOM ORDER")
        print("___________________")
        for i in range (1, len(self.directory)+1):
            print (self.directory[i])

    def getKey(self, name):
        return [k for k,v in self.directory.items() if (name == (v.last + ", " + v.first))]
                
    def printNameOrder(self):
        print("HOTEL IN NAME ORDER")
        print("___________________")
        [print (v) for k,v in sorted(self.directory.items(), key=lambda item: item[1])]

    def search(self, name):
        room = self.getKey(name)
        print(name, "is in Room", room)
        
h = Hotel("Hotel.csv")
h.read()
h.printRoomOrder()
print()
h.printNameOrder()
print()
h.search("Zhu, Vivian")
    
