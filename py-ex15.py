#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
names = ["1", "2", "3", "4"]
print names
print names[2:]
print names[:2]
print names[1:2]
print names[1]
names[2:4] = ["5", "6"]
print names
more = ["7", "8"]
tots = names + more
print tots
#print tots - more
tots = [names, more]
print tots
print tots[0][1], tots[1][1]
vals = [float(n) for n in names]
print vals
print vals + [2]
print min(vals)
print max(vals)
