# Log in [Input username and password, check matched or not]
def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
# Show all processes that's available for choosing
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
# Select Options above here
def menuSelect():
    userSelected = input(">>")      # unnecessary to covert to string, because no need to compute
    return userSelected
# Calculate vat price [Last Process]
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
# Sum all products [item price only, then send to vatCalculator(..) func]
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    # Directly call vatCalculator(..) to compute, and return result
    return price1 + price2      # I don't want to call vatCalculator cuz they might want 'price order only'

# Sync all processes [Main]
if login() == True:
    # Continue to the next step [showMenu func]
    showMenu()
    choice = menuSelect()
    if choice == "1":
        print("Order Price : ",priceCalculator())        # Enter price order here, then sum and return
    elif choice == "2":
        print("VatPrice : ",vatCalculator(priceCalculator()))   # Call vatPrice by [param comes from priceCalculator()]
else:
    print("Username or Password isn't correct, Pls try again!")