#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
a = 6
b = 6
if not (a < b or b < a):
    print "Both numbers are equal"
elif a < b:
    print "In ascending order"
else:
    print "Not in ascending order"
