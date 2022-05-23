# Amal Kariyawasam 23/05/2022
#Fun Little program to calculate price of a pizza

print("Welcome to Amals' Pizza Deliveries!") # Welcome text
size = input("What size pizza do you want? S, M, or L ") # Code to capture size of the pizza
add_pepperoni = input("Do you want pepperoni? Y or N ") # Code to capture user preference Pepperoni
extra_cheese = input("Do you want extra cheese? Y or N ") # Code to capture user preference Extra Cheese



cost=0
#Code to capture pizza size
if size == "S":
  cost=15
elif size=="M":
  cost=20
elif size=="L":
  cost=25
# Code logic to determine user preference for Extra Cheese
if extra_cheese=="Y":
  print("Extra cheese added")
  cost +=1
# Code logic to determine user preference for Pepperoni
if add_pepperoni=="Y":
  if size=="S":
    print("Smalll peperoni added")
    cost +=2
  elif size=="M":
    print("Medium peperoni added")
    cost +=3
  elif size=="L":
    print("Large peperoni added")
    cost +=3
#Code to print the final pizza price
print(f"cost of your pizze is ${cost}") 



