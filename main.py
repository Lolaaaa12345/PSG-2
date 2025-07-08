#variables
full_name_set = ["22g IV", "24g IV", "IV starter kits"]
quantity_set = [25, 350, 50]
taking_out = True
found_match = False

#welcome to the program
print("Hello! Welcome to PSG's Inventory Manager")
print("If you want to switch modes, write 'put in' in or 'take out'")
print("")

while end == False:
  if taking_out == True:
    item_abr = input("What item will you be taking out? ")
    if item_abr.lower() == ("put in"):
      taking_out = False
      item_abr = input("What item are you restocking? ")
  else: 
    item_abr = input("What item are you restocking? ")
    if item_abr.lower() == ("take out"):
      taking_out = True
      item_abr = input("What item will you be taking out? ")
  
  item_abr = item_abr.lower()
  
  #looking for the abriviated item to match the full one 
  for index, element in enumerate(full_name_set):
    element = element.lower()
    if element[:3] == item_abr:
      item_full = element
      number_place = element
      found_at = (index)
      break
  
  #Now ask for quantity
  print("You have selected: " + item_full)
  number = input("How many of " + item_full + " are you taking out? ")
  print("Ok! Now you have " + str((int(quantity_set[found_at]) - int(number))) + " " + item_full)
  
