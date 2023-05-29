

def calculate_price(typeoffroyo, froyosize):
    totalprice = 0
    order = []
    discountnumber = 0
    
    if typeoffroyo =="vanilla":
        totalprice = 5.25
        order.append("vanilla froyo")
        discountnumber += 1
    elif typeoffroyo =="chocolate":
        totalprice = 5.75
        order.append("chocolate froyo")
        discountnumber += 1
    elif typeoffroyo =="peanut butter":
        totalprice = 6.25
        order.append("peanut butter froyo")
        discountnumber += 1
    else:
        print("that is not on our menu")
        return 0, []

    if froyosize =="small":
        megasizedanswer = input("would you like a mega sized froyo? ")
        if (megasizedanswer == "yes"):
            print("you got a mega sized froyo for the price of a small")
            order.append(" a mega sized froyo")
        if (megasizedanswer == "no"):
            print("You declined the mega size discount")
        order.append(" a small froyo")
    elif froyosize =="medium":
        totalprice += .75
        order.append(" a medium froyo")
    elif froyosize =="large":
        totalprice += 1.25
        order.append(" a large froyo")
    else:
        print("that is not on our menu")
        return 0, []

    # Add drink to order
    beverageyesno = input("Would you like a beverage? ")
    if (beverageyesno == "yes"):
        discountnumber += 1
        drinkinput = input("""What size would you like we have    
        small $1.00
        medium $1.75
        large $2.25""")
        
        if drinkinput =="small":
            totalprice += 1
            order.append(" a small drink")
        elif drinkinput =="medium":
            totalprice += 1.75
            order.append(" a medium drink")
        elif drinkinput =="large":
            totalprice += 2.25
            order.append(" a large drink")
        else:
            print("that is not on our menu")
            return 0, []
        
        print("you choose ", order[-1], )
        print("your current total is $", totalprice )
    elif (beverageyesno == "no"):
        print("You chose no drink")
    else:
        print("that is not on our menu")
        return 0, []

    # Add cherries to order
    numofcherries = int(input("how many cherries would you like? They are 25 cents each. "))
    totalprice +=numofcherries*.25
    if numofcherries > 4:
        print("you can only have up to 4 cherries on your froyo")
        totalprice -=numofcherries*.25
        numofcherries = int(input("how many cherries would you like? They are 25 cents each. "))
        totalprice +=numofcherries*.25
    order.append(" and "+str(numofcherries)+ " cherries")

    # Apply discount if applicable
    if discountnumber >= 3:
        totalprice += -1

    return totalprice, order

# Initialize an empty list to store all the orders
all_orders = []

# Call the function with different arguments using a loop
neworderyesno = True
while neworderyesno == True:
    typeoffroyo = input("What type of froyo would you like? ")
    froyosize = input("""What size would you like we have    
    small (same price)
    medium (+$.75)
    large (+$1.25)""")
    totalprice, order = calculate_price(typeoffroyo, froyosize)
    if totalprice == 0:
        continue
    print("your total price is $", totalprice)
    print("you ordered ", end='')
    print(*order, sep=',' )
    all_orders.append(order)
    neworderyesno = input("Would you like to start a new order? ") 
    if neworderyesno == "yes":
        continue 

# Print all the orders placed by the user
print("All orders placed:")
for order in all_orders:
    print(*order, sep=', ')


