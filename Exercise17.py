from sys import argv
from os.path import exists

script, from_file, to_file = argv

print (f"Does file {from_file} exists:? {exists(from_file)}.")
input_file = open(from_file,'w')
print (f"Contents of input {from_file} file are:")

line1 = input(">")
input_file.write(line1) 

indata = input_file.read()

print (f"copying the contents to new file {to_file}.")

output_file = open(to_file, 'w')
output_file.write(indata)

 

#output_file.close()
#input_file.close()
