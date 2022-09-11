weight = 8.4

#GROUND SHIPPING

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Cost of shipping with that weight: $", cost_ground)

#GROUND SHIPPING PREMIUM

cost_ground_premium = 125.00

print("Cost of Premium Shipping with that weight: $", cost_ground_premium)

#DRONE SHIPPING

if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Cost of Drone Shipping with that weight: $", cost_drone)

# John Stewart | Sal's shipping | Codecademy | 11/09/2022


