from sys import argv

name, age, city = argv

print ("The name of customer is:",name)
print ("Age of customer is:",age)
print ("City in which customer lives is:",city)

print ("The name of customer is:", end = ' ')
name1 = input()
name2 = input("Name of customer is:")

print (f"The name of customer is {name} and other customer is {name1} and third is {name2}.") 