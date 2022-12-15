#Adding In The Catalog

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_price = 254.00 #cost of 1 seat

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_price = 180.50 #cost of 1 settee

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15 #cost of 1 lamp

sales_tax = 0.088 # sales tax

#Our First Customer

customer_one_total = 0

customer_one_itemization = ""

customer_one_total += lovely_loveseat_price #cost of total customer purchases of the lovely_loveseat

#print(customer_one_total)

customer_one_itemization += lovely_loveseat_description

#print(customer_one_itemization)

customer_one_total += luxurious_lamp_price

#print(customer_one_total)

customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

#print(customer_one_tax)

customer_one_total += sales_tax

print("Customer One Items: ")
print(customer_one_itemization)
print("Customer One Total: ")
print(customer_one_total)

# John Stewart | Lovely Love Seat | Codecademy | 15/12/2022