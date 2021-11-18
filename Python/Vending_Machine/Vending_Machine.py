##############################
# Name: Alexander Valler
# Section: ?
# Project: Gremlin Vending Machine
# Description:
##############################
# Variables #
state = "A"
total_inserted = 0 #The amount of money the user has inserted
cost = 0.99 #The price of each item in the machine
item_1 = 4 #This will hold the number of items in the machine of type 1
item_2 = 2 #This will hold the number of items in the machine of type 2
item_3 = 3 #This will hold the number of items in the machine of type 3
B_input = "A"
gremlin = 0
import random

###############################
# State A Start or Idle #
start_check = input("Type start to begin or anything else to exit: ")
while (start_check == "start"):
    while(state == "A"):
        print()
        print("Hello")
        A_input = input("Enter I to insert money, S to stock, or G to turn off: ")
        if(A_input == "I"):
            state = "B"
        if(A_input == "S"):
            state = "F"
        if(A_input == "G"):
            state = "Exit"
            start_check = "Exit"

################################
    # State B Insert #
    while(state == "B"):
        print()
        while(B_input == "A"):
            money_inserted = float(input("Please insert coins: "))
            gremlin_take = bool(random.getrandbits(1))
            if(gremlin_take == True):
                money_inserted = (money_inserted - money_inserted)
                print ("The Gremlin stole your coins!")
            total_inserted = (total_inserted + money_inserted)
            print("Your total: {}".format (total_inserted))
            B_input = input("Enter A to add more money, S to make a selection, or R to return your money: ")
            if(B_input == "S"):
                state = "C"
            if(B_input == "R"):
                state = "E"
        B_input = "A"

###############################
    # State C Select #
    while(state == "C"):
        print()
        print("The selection items are:")
        print("item_1, item_2, item_3")
        C_input2 = input("Which item would you like to dispense?: ")
        C_input3 = int(input("How many of that item do you want?: "))
        if(((C_input2 == "item_1") and (C_input3 <= item_1)) or ((C_input2 == "item_2") and (C_input3 <= item_2)) or ((C_input2 == "item_3") and (C_input3 <= item_3))):
            total_cost = (C_input3 * cost)
            print("The cost of your selection will be: {}".format(total_cost))
            if((total_inserted - total_cost) >= 0):
                print("Would you like to continue with your purchase?")
                C_input4 = input("Type yes to continue or no to return your change: ")
                if(C_input4 == "yes"):
                    total_inserted = (total_inserted - total_cost)
                    state = "D"
                else:
                    state = "E"
            if((total_inserted - total_cost) < 0):
                print("You will need more coins to complete the transaction.")
                print()
                state = "B"
        else:
            print("Error, try a new selection")

###############################
    # State D Dispense #
    while(state == "D"):
        print()
        print("Dispensing your items.")
        print("{} x {}".format(C_input3, C_input2))
        print()
        print("Returning Change: {}".format(total_inserted))
        print("Have a nice day.")
        state = "A"

###############################
    # State E Return Change #
    while(state == "E"):
        print()
        print("Returning Change: {}".format(total_inserted))
        total_inserted = 0
        state = "A"

###############################
    # State F Stock #
    while(state == "F"):
        print()
        print("Restocking")
        item_1 = 4
        item_2 = 2
        item_3 = 3
        print("There is now:")
        print("{} of item_1".format(item_1))
        print("{} of item_2".format(item_2))
        print("{} of item_3".format(item_3))
        state = "A"

###################################
# State G #
print("Goodbye")