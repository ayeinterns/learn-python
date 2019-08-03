#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
class statmeth(object):
    a = 0
    b = 0
    @staticmethod
    def gcount(self):
        global self.b
        self.b += 1
        return self.b
    def count(self):
        self.a += 1
        return self.a
a = statmeth()
b = statmeth()
c = statmeth()
print a.count(),statmeth.gcount(),b.count(),b.gcount()
print a.gcount(),b.gcount()
print c.gcount()
