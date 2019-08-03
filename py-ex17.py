#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
s=set([1,2,3,4])
print s
#print s[1]
t =set("Hello")
print t
t.add(5)
print t
s.add(5)
print s
#a = t + s
b = t - s
print b
c = t | s
print c
d = t & s
print d
e = t ^ s
print e
print min(s)
print max(s)
print t
t.update([7,8,9])
print t
t.remove(5)
print t
