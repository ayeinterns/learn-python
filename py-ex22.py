#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
class stack(list):
    def push(self,object):
        self.append(object)
    def len(self):
        return len(self)
s = stack()
s.push(1)
s.push(2)
s.push(3)
print s.pop()
print s.len()
