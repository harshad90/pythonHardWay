from sys import argv

script, user_name, first, second = argv
newPrompt = '---->>'

print (f"Hi {user_name}, I'm the {script} script.")
print ("I'd like to ask you a few questions.")
print (f"Do you like me {user_name}?")
likes = input(newPrompt)

print (f"Where do you live {user_name}?")
lives = input(newPrompt)

print (f"What kind of computer do {user_name} have?")
computer = input(newPrompt)

print (f''' 
Alright, so you said {likes} about liking me.
You live in {lives}. Not so sure where that is.
And you have a {computer} computer. Nice.
       ''')

print (f"First name in argument of {script} script is: ",first)
print (f"Second name in argument of {script} script and with username {user_name} is: ",second)