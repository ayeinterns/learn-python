#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
for i in range(1,10):
    for j in range(1,10):
        print "%d * %d = %d" % (i, j, i*j)
    print
a = range(10)
print a
b = range(1,5)
print b
c = range(0,10,2)
print c
d = range(10,0,-1)
print d
e = xrange(10)
print e
f = xrange(0,100,10)
print f
def fib(mx):
    a = 1
    b = 1
    while mx >= a:
        yield a
        t = a
        a = b
        b = a + t
    return
for n in fib(100):
    print n
m = fib(10000)
for n in range(20):
    print m.next()
