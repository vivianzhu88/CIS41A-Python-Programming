class Device():
    def  __init__(self, filename):
        self.filename = filename
        self.sentences = []
        self.text = ""
        self.freq = {}
        self.fT = []
        self.max = ""

    def read(self):
        handle = open(self.filename)
        for line in handle:
            l = line.rstrip()
            self.sentences.append(l)
            self.text += l
        
    def frequency(self):
        for c in self.text:
            self.freq[c] = self.freq.get(c, 0) + 1
        self.fT = list(self.freq.keys())
        self.fT.sort()

    def findMax(self):
        self.max = max(self.freq, key=self.freq.get)

    def find3SpaceSep(self):
        counter = 0
        shift = self.fT.index(" ") - self.fT.index(self.max)
        for i in range(len(self.text)):
            if counter == 0:
                if self.text[i] == self.max:
                    counter += 1
            elif counter > 0 and counter < 4:
                counter += 1
            else:
                l = len(self.fT)
                if (self.text[i] == self.max):
                    if ((self.fT.index("a") - shift)%l == self.fT.index(self.text[i-3])) and ((self.fT.index("n") - shift)%l == self.fT.index(self.text[i-2])) and ((self.fT.index("d") - shift)%l == self.fT.index(self.text[i-1])):
                        return shift
                    elif ((self.fT.index("t") - shift)%l == self.fT.index(self.text[i-3])) and ((self.fT.index("h") - shift)%l == self.fT.index(self.text[i-2])) and ((self.fT.index("e") - shift)%l == self.fT.index(self.text[i-1])):
                        return shift
                    else:
                        counter = 0
                else:
                    counter = 0

    def decrypt(self):
        self.read()
        self.frequency()
        self.findMax()
        shift = self.find3SpaceSep()

        l = len(self.fT)
        for s in self.sentences:
            for c in s:
                i = self.fT.index(c)
                print(self.fT[(i + shift)%l], end = "")
            print()
            

d = Device("Encrypt.txt")
d.decrypt()

