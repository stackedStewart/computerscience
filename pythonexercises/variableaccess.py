# This function will print a hardcoded count of how many locations we have.
favorite_locations = "Paris, Norway, Iceland"

def print_count_locations():
  #favorite_locations = "Paris, Norway, Iceland" #Having this here will only be accessible here.Moved to outside scope.
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

#show_favorite_locations()
print_count_locations()
show_favorite_locations()