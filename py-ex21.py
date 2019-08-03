#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
class queue(object):
    def __init__(self):
        self.queue = []
    def add(self,object):
        self.queue.append(object)
    def len(self):
        return len(self.queue)
    def rem(self):
        t=self.queue[0]
        l=len(self.queue)
        self.queue=self.queue[1:l]
        return t;
q = queue()
q.add("A")
q.add("Hello")
q.add([1,2,3])
print q.len(),q.rem(),q.len()
while 0 < q.len():
    print q.rem()
print q.len()
