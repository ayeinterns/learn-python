#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
prin = 10000
rate = 0.05
numy = 5
year = 1
while year <= numy:
    prin = prin * (1 + rate)
    print year, prin
    year += 1
