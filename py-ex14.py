#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
names = ["AC", "SC", "DC", "BC"]
print names
print names[2:]
print names[:2]
print names[1:2]
print names[1]
names[2:4] = ["CC", "VC"]
print names
more = ["DC", "BC"]
tots = names + more
print tots
#print tots - more
tots = [names, more]
print tots
print tots[0][1], tots[1][1]
