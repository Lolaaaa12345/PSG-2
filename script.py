from colorama import Fore, Style
import json
import os

#variables
#load in the stored data
#quantity_set_one = [25, 350, 50]- the old method
if os.path.exists("inventory.json"):
    with open("inventory.json", "r") as inventory_file_save:
        inventory_data = json.load(inventory_file_save)
        quantity_set_one = inventory_data["quantity_set_one"]
        quantity_set_two = inventory_data["quantity_set_two"]
        quantity_set_three = inventory_data["quantity_set_three"]
        quantity_set_four = inventory_data["quantity_set_four"]

#from 22g IV to 10mL NaCl Flush Syringe
full_name_set_one = ["22g IV", "24g IV", "IV starter kits", "Patient Belonging Bag", "Patient Gowns", "Socks", "Sterile Urine Cups", "Table Drapes", "Pillow Cases", "10ml NaCl Flush Syringe"]
order_when_set_one = [15, 30, 45, 30, 30, 30, 5, 15, 30, 1]

#from Gloves L to Alcohol Wipes
full_name_set_two = ["Gloves Large", "Gloves Medium", "Gloves Small", "Blood Glucose Strips (50/box)", "Blood Glucose Monitoring System", "Safety Lancets", "hCG Pregnancy Test strips", "Tegaderm", "4x4 Gauze", "Alcohol Wipes"]
order_when_set_two = [1, 1, 1, 50, 0, 10, 10, 0, 2, 30]

#from cold snares to RiteClip 11mm
full_name_set_three = ["10mm Cold Snares", "20mm Firm Snares", "Radial Jaw Biopsy Forceps Standard capacity", "Radial Jaw Biopsy Forceps Large capacity", "OrcaPod", "Blox(Bite Block w/Elastic Strap, 60F)", "Hydra Water Bottle Cap System w/CO2", "Hydra Irrigation Tubing System", "Hedgehog Cleaning brushes", "11m RiteClip"]
order_when_set_three = [10, 5, 15, 15, 5, 10, 2, 2, 25, 5]

#from RiteClip 16mm to Rapide Multistage Dilation Balloon Catheter 15-18
full_name_set_four = ["16mm RiteClip", "25g PinPoint Injection Needle", "10mL EndoINK Endoscopic Marker", "10mL BlueBoost Submucosal Interjectable Solution", "In-Line Suction Polyp Trap", "Speedband Superview Super 7", "10% Neutral Buffered Formalin (24/pack) Specimen Jars", "10-12 Rapide Multistage Dilation Balloon Catheter", "12-15 Rapide Multistage Dilation Balloon", "15-18 Rapide Multistage Dilation Balloon"]
order_when_set_four = [3, 3, 2, 4, 10, 1, 3, 0, 0, 0]

#from Rapide Multistage Dilation Balloon Catheter 18-20 to Soft Guedel Airway (90mm, Size 4)
full_name_set_five = ["18-20 Rapide Multistage Dilation Balloon Catheter", "Koala CLeaning Sponge + Pure Enzymatic", "Basin", "70% Isopropyl Alcohol", "1200 cc Collection container", "1200 Collection caps + tubing (set)", "60mm soft guedel airway", "70mm soft guedel airway", "80mm soft guedel airway", "90mm soft guedel airway"]
order_when_set_five = []

#from underpad(30x36in) to Polypropylene Pleated Filter Cartridge
full_name_set_six = ["30x36 Underpad", "1 Gal Enzymatic Detergent", "QD x Pathology GPP Plus", "5oz AquaGel Lubricating Gel", "Metricide OPA Plug(ortho-phthalaldehyde sol", "hydrogen and methane Breath test (sibo 10 tube lactulose", "CO2 cannisters", "Yankauer with bulb tip", "20mL Syringe (Luer-Lock tip) monoject", "polypropylene pleated filter cartridge"]
order_when_set_six = []

#from O2 masks to Naloxone Hydrochloride Injection 0.4mg
full_name_set_seven = ["O2 Masks", "CO2 7inch Cannula", "blunt tip needles (100/box", "laryngeal mask size 5", "MedGel General Monitoring ECG Electrode (60/pack)", "500ml Lactated Ringer Injection USP", "200mg per 20ml (10mg/mL) Propofol (20/box)", "50mL 8.4% sodium bicarbonate", "glycopyrrolate", "0.4mg Naloxone Hydrochloride Injection"]
order_when_set_seven = []

#from Ondansetron injection 2mL to Albuterol Sulfate Inhalation Solution 2.5mg/3mL
full_name_set_eight = ["2mL ondansetron injection", "ketorolac tromethamine (25 vials/box)", "05mg/mL Flumazenil", "atropine sulfate injection USP 0.1", "metoprolol tartrate (10/box)", "200mg/20mL Lidocaine hydrochloride injection 1%", "9mL amlodpine hydrochloride (10/box)", "50mg/mL Diphenhydramine Injection", "Epinephrine Injection (10/box)", "2.5mg/3mL Albuterol Sulfate Inhalation Solution"]
order_when_set_eight = []

#from Albuterol Sulfate Inhalation Aerosol 90mcg to small trash bags
full_name_set_nine = ["90mcg Albuterol Sulfate Inhalation Aerosol", "25mg/50mL Dextrose 50%", "graham crackers", "apple juice (8/pack)", "paper towels", "brown paper towels", "cups", "hand soap", "toilet paper", "purple wipes", "tissue boxes", "small trash bags"]
order_when_set_nine = []

taking_out = True
end = False

# welcome to the program
print("--------------------------------------------------------------------------------")
print(Fore.GREEN + "Hello! Welcome to PSG's Inventory Manager" + Style.RESET_ALL)
print("If you want to switch modes, write 'put in' in or 'take out'")
print("When you are done, write exit when it prompts you to enter another item")
print("--------------------------------------------------------------------------------")

while not end:

    #for telling the program which list index to look inside
    list_one = False
    list_two = False
    list_three = False
    list_four = False
    list_five = False
    list_six = False
    list_seven = False
    list_eight = False
    list_nine = False

    #to stop the search
    found_match = False

    print([quantity_set_one])
    print([quantity_set_two])

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
        break

    # look for match in list 1
    for index, element in enumerate(full_name_set_one):
        element = element.lower()
        if item_input in element.lower():
            item_full_name = element
            number_place = element
            found_at = index
            found_match = True
            list_one = True
            break

    # look for match in list 2
    if found_match == False:
        for index, element in enumerate(full_name_set_two):
            element = element.lower()
            if item_input in element.lower():
                item_full_name = element
                number_place = element
                found_at = index
                found_match = True
                list_two = True

    #if the item entered is not found anywhere
    if not found_match:
        print("Sorry, the item you are looking for is not in the inventory")
        continue

    # confirm the selection
    print("You have selected: " + item_full_name)

    #for when you're taking out items
    if taking_out == True:
        number = input("How many of " + item_full_name + " are you taking out? ")

        #list one
        if list_one == True:
            quantity_set_one[found_at] = (int(quantity_set_one[found_at]) - int(number))
            print("Ok! Now you have " + str(quantity_set_one[found_at]) + " of " + item_full_name)
            if quantity_set_one[found_at] <= order_when_set_one[found_at]:
                print(Fore.RED + "It is time to order " + item_full_name)
                if quantity_set_one[found_at] < order_when_set_one[found_at]:
                    print("You are " + str(abs(quantity_set_one[found_at] - order_when_set_one[found_at])) + " below the minimum amount " + str(order_when_set_one[found_at]) + Style.RESET_ALL)
                else:
                    print("You are exactly at the quantity to reorder" + Style.RESET_ALL)

        #list 2
        elif list_two == True:
            quantity_set_two[found_at] = (int(quantity_set_two[found_at]) - int(number))
            print("Ok! Now you have " + str(quantity_set_two[found_at]) + " of " + item_full_name)
            if quantity_set_two[found_at] <= order_when_set_two[found_at]:
                print(Fore.RED + "It is time to order " + item_full_name)
                if quantity_set_two[found_at] < order_when_set_two[found_at]:
                    print("You are " + str(abs(quantity_set_two[found_at] - order_when_set_two[found_at])) + " below the minimum amount " + str(order_when_set_two[found_at]) + Style.RESET_ALL)
                else:
                    print("You are exactly at the quantity to reorder" + Style.RESET_ALL)

    #for when you're putting in items
    else:
        number = input("How many of " + item_full_name + " are you restocking? ")
        if list_one == True:
            quantity_set_one[found_at] = (int(quantity_set_one[found_at]) + int(number))
            print("Ok! Now you have " + str(quantity_set_one[found_at]) + " of " + item_full_name)
        elif list_two == True:
            quantity_set_two[found_at] = (int(quantity_set_two[found_at]) + int(number))
            print("Ok! Now you have " + str(quantity_set_two[found_at]) + " of " + item_full_name)

#outside of the loop- when the user ends the program
inventory_data = {
    "quantity_set_one": quantity_set_one,
    "quantity_set_two": quantity_set_two,
}
with open("inventory.json", "w") as inventory_file_save:
    json.dump(inventory_data, inventory_file_save)