#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
a = {
        "un" : "ac",
        "id" : 1234
    }
print a
print a["id"]
if a.has_key("name"):
    pass
else:
    print "No name given"
name = a.get("name", "No key name")
print name
un1 = a.get("un", "No un")
print un1
print a.keys()
del a["id"]
print a
