#Vivian Zhu
#Midterm Review

class Student():
    def __init__(self, last, first, room):
        self.last = last
        self.first = first
        self.room = room
    def getLast(self):
        return self.last
    def getFirst(self):
        return self.first
    def getRoom(self):
        return self.room

class Rooms():
    def __init__(self, filename):
        self.filename = filename
        self.directory = {}
    
    def sorter(self):
        handle = open(self.filename)
        for line in handle:
            s = line.rstrip()
            ss = s.split(",")
            student = Student(ss[0], ss[1], ss[2])
            self.directory[int(ss[2])] = student
            
        for i in range (1, len(self.directory)+1):
            print(self.directory[i].getLast(), self.directory[i].getFirst(), self.directory[i].getRoom())
        
r = Rooms("Room.csv")
r.sorter()
    
        
            
            
