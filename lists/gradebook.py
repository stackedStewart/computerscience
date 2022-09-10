last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#print(gradebook)

#Add More Subjects

gradebook.append(["computer science", 100])#Adds Computer Science to end of the List
#gradebook.append(100)

#print(gradebook)

gradebook.append(["visual arts", 93])#Adds visual arts to end of list

#print(gradebook)

#Modify the Gradebook
gradebook[-1][1] = 98 # Will Change Physics to a 98 score

#print(gradebook)

gradebook[2].remove(85) #removes poetry score

#print(gradebook)

gradebook[2].append("Pass") #Changes Poetry score to a pass

#print(gradebook)

#One Big Gradebook
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)#Prints whole gradebook

# John Stewart | Computer Science Career Path | Gradebook | Codecademy | 09/10/2022