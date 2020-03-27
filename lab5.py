#Vivian Zhu
#Lab 5

class RomanNum():
    def __init__(self):
        self.ones = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")
        self.tens = ("", "X", "XX","XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
        self.hundreds = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M")

    def convertNum(self, num):
        hundredindex = num // 100;
        tenindex = (num - hundredindex*100) // 10
        oneindex = num - hundredindex*100 - tenindex*10

        romannumeral = self.hundreds[hundredindex] + self.tens[tenindex] + self.ones[oneindex]
        return romannumeral   

r = RomanNum()
rc = r.convertNum(123)
print(rc)
