money = 3000

while money > 0:
    usage_fee = 100
    menu = "shrimp, Cookie,Pizza,chicken,sushi"

    name = input("What's your name?")

    if name == "Ben" or name == "Patrica": 
        evil_status = input("Are you evil? ")
        good_deeds = int(input("How many good things have you done today? "))
        if evil_status == "Yes" and good_deeds < 4: 
            print("I am " + name + "phobic, please get out.")
            continue
    else:
        print("Hello " + name + ", thank you for shopping at Food Emporium.")
    
    print("Here is the menu : ")
    print(menu)
    
    order = input("What would you like to order? ")

    if order == "Shrimp":
        usage_fee = 100
    elif order == "Cookie":
        usage_fee = 20000
    elif order == "Pizza":
        usage_fee = 10
    elif order == "chicken":
        usage_fee = 3000
    elif order == "Sushi":
        usage_fee = 200000
    else:
        print("Invalid selection. Please try again.")
        continue

    if usage_fee > money:
        print("Sorry, you do not have enough money to make this purchase.")
        continue

    money -= usage_fee
    print("You bought " + order + " for " + str(usage_fee) + " credits.")
    print("You have " + str(money) + " credits left.")

print("Sorry, you are out of money. Please come back later.")
# read the name from file or ask for it if file doesn't exist
filename = "names.txt"
name = input("Enter your name: ")

with open(filename, "a") as f:
    f.write(name + "\n")

print("Name added to file.")

