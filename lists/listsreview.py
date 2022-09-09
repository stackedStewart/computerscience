 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]

#Adding Depak' size to list with Medium.
preferred_size.append("Medium")#Added to list
print(preferred_size)

#Creating a 2D list to help with each Customer' size
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]

print(customer_data)

#Chani wants Shipping changed
customer_data[2][2] = False
#Ben isn't sure yet
customer_data[1].remove(False)
#Amit and Karim want to be added to the list.
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]] #This will be added to end of customer data
print(customer_data_final)

# John Stewart | CS Python Lists Review | Codecademy | 09/09/2022
