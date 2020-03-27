#Vivian Zhu
#Lab 4

class MorseCode():
    def __init__(self, s):
        ss = s.rstrip()
        data = ss.split(",")         
        self.alpha = data[0]
        self.morse = data[1]
        
    def getAlpha(self):
        return self.alpha
    
    def getMorse(self):
        return self.morse

def createTranslator(filename):
    handle = open(filename)
    translator = []
    for line in handle:
        translator.append(MorseCode(line))

    return translator

def translateSent(sent, translator):
    tranSent = ""
    count = 0
    for i in range (0, len(sent)):
        if (sent[i] == " "):
            tranSent += "/ "
        else:
            while sent[i] != translator[count].getAlpha():
                count += 1
            tranSent += translator[count].getMorse() + " "
            count = 0
    print (tranSent)

t = createTranslator("MorseCode.csv")
translateSent("THE QUICK BROWN POODLE JUMPED OVER THE LAZY FOX 123 TIMES", t)

    

