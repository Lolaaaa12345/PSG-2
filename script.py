from colorama import Fore, Style
import json
import os

# variables
#load in the stored data
#quantity_set_one = [25, 350, 50]- the old method
if os.path.exists("inventory.json"):
    with open("inventory.json", "r") as inventory_file_save:
        inventory_data = json.load(inventory_file_save)
        quantity_set_one = inventory_data["quantity_set_one"]


full_name_set_one = ["22g IV", "24g IV", "IV starter kits"]
order_when_set_one = [16, 30, 45]

taking_out = True
found_match = False
end = False

# welcome to the program
print("--------------------------------------------------------------------------------")
print(Fore.GREEN + "Hello! Welcome to PSG's Inventory Manager" + Style.RESET_ALL)
print("If you want to switch modes, write 'put in' in or 'take out'")
print("When you are done, write exit when it prompts you to enter another item")
print("--------------------------------------------------------------------------------")

while not end:
    if taking_out == True:
        print()
        item_input = input("What item will you be taking out? ")
        if item_input.lower() == "put in":
            taking_out = False
            item_input = input("What item are you restocking? ")
    else:
        print()
        item_input = input("What item are you restocking? ")
        if item_input.lower() == "take out":
            taking_out = True
            item_input = input("What item will you be taking out? ")

    item_input = item_input.lower()

    #if the user wants to end
    if item_input == "exit":
        end = True
        continue

    # looking for the abbreviated item to match the full one
    for index, element in enumerate(full_name_set_one):
        element = element.lower()
        if item_input in element.lower():
            item_full_name = element
            number_place = element
            found_at = index
            found_match = True
            break

    #if the item entered is not found anywhere
    if not found_match:
        print("Sorry, the item you are looking for is not in the inventory")
        continue

    # confirm the selection
    print("You have selected: " + item_full_name)

    #for when you're taking out items
    if taking_out == True:
        number = input("How many of " + item_full_name + " are you taking out? ")
        quantity_set_one[found_at] = (int(quantity_set_one[found_at]) - int(number))
        print("Ok! Now you have " + str(quantity_set_one[found_at]) + " of " + item_full_name)
        if quantity_set_one[found_at] <= order_when_set_one[found_at]:
            print(Fore.RED + "It is time to order " + item_full_name)
            if quantity_set_one[found_at] < order_when_set_one[found_at]:
                print("You are " + str(abs(quantity_set_one[found_at] - order_when_set_one[found_at])) + " below the minimum amount " + str(order_when_set_one[found_at]) + Style.RESET_ALL)
            else:
                print("You are exactly at the quantity to reorder")

    #for when you're putting in items
    else:
        number = input("How many of " + item_full_name + " are you restocking? ")
        quantity_set_one[found_at] = (int(quantity_set_one[found_at]) + int(number))
        print("Ok! Now you have " + str(quantity_set_one[found_at]) + " of " + item_full_name)

#outside of the loop- when the user ends the program
inventory_data = {
    "quantity_set_one": quantity_set_one,
}
with open("inventory.json", "w") as inventory_file_save:
    json.dump(inventory_data, inventory_file_save)