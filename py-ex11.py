#(C) Copyright 2019 Abhishek Choudhary, Dr Srija Katta
#Under GNU GPL v2 license only
f = open("contacts.txt","w")
print "Adding contact info"
name = raw_input("Name: ")
phone = raw_input("Phone: ")
email = raw_input("Email: ")
f.write("%s,%s,%s\n" % (name,phone,email))
f.close()
