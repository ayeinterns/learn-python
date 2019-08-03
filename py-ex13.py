#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
a = 1.234
b = -5.678
c = a
d = b
print c, d
print c + d
print `c` + `d`
c = str(a)
d = str(b)
print c, d
print c + d
c = repr(a)
d = repr(b)
print c, d
print c + d
