#Imported Library
import random

#SETTING UP
name = "John"

question = "Is it time i got my act together?"

answer = ""

#GENERATING A RANDOM NUMBER
random_number = random.randint(1, 9)
#print(random_number)

#CONTROL FLOW
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Better not tell you now."
elif random_number == 6:
  answer = "My sources say no."
elif random_number == 7:
  answer = "Outlook not so good."
elif random_number == 8:
  answer = "Very Doubtful."
elif random_number == 9:
  answer = "Ask again later."
else:
  answer = "Error" 

#SEEING THE RESULT
#print(name + " asks: " + question)


#EMPTY STRING
if name == "":
  print("Question: " + question) #Will print if empty
else:
  print(name + " asks: " + question) #Will print if not empty

print("Magic 8-ball answer: " + answer) #Print 8-ball answer

#John Stewart | Magic 8-Ball | 30/01/2023