print("I have information for the following planets:\n")

print("  1. Venus  2. Mars    3. Jupiter")
print("  4. Saturn 5. Uranus  6. Neptune\n")

weight = 185
planet = 4

#This is what determines what planet has been chosen and what the weight will be.
if planet == 1:
    weight = weight * 0.91
elif planet == 2:
    weight = weight * 0.38
elif planet == 3:
    weight = weight * 2.34
elif planet == 4:
    weight = weight * 1.06
elif planet == 5:
    weight = weight * 0.92
elif planet == 6:
    weight = weight * 1.19

   
'''def planet(i):
    switcher = {
        1: weight = weight * 0.91,
        2: weight = weight * 0.38,
        3: weight = weight * 2.34,
        4: weight = weight * 1.06,
        5: weight = weight * 0.92,
        6: weight = weight * 1.19
    }'''

print("Planet you are on: ", planet)#Will print number of planet you are on.
print("Your weight: ", weight)#Will print Your weight on the chosen planet.

#John Stewart | Littlecody Project | Codecademy | 07/09/2022
#Updating with a python switch 12/14/2022 //NOT FINISHED 