def print_one (*args):
    arg1, arg2 =args
    print (f"arg1 : {arg1}, arg2 : {arg2}")

def print_two (arg1,arg2):
     print (f"arg1 : {arg1}, arg2 : {arg2}")

def print_three (arg1):
    print (f"arg1 :{arg1}.")
    
def none ():
    print ("I got nothing")

print_one (21,"Harshad")
print_two ("harshad","bhangale") 
print_three ("qwerty")
none ()