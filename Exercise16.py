from sys import argv

script,filename = argv

print (f"We'r going to erase {filename}.")
print ("If you don't want that, hit CTRL-C (^c).")
print ("If you do want that, hit RETURN")

input("?")

print ("Opening the file")
target = open(filename,'w')

#print ("Contents of file are")
#print (target.read())

print ("Deleting the content of the file")
target.truncate()

line1 =input("line1: ")
line2 =input("line2: ")
line3 =input("line3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print ("Closing file")
target.close()

