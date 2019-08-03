#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
a = 3.141593
b = 1.414213
print a,b
def fna():
    a = 1
    a = a ** a
    return a
print a,b
def fnb():
    global b
    b = b ** 2
    return b
print a,b
print fna()
print a,b
print fnb()
print a,b
def rettup(x,y):
    return(y,x)
q = rettup(2,3)
print q
s, t = rettup(7,9)
print s, t
