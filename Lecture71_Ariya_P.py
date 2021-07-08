# Menu and Total price for food store
# Practice using [List], some functions

menuList = []
priceList = []

def showSlipt():
    print("--- My Food ---")
    totalPrice = 0
    for i in range(len(menuList)):
        print(menuList[i],":",priceList[i],"Baht")
        totalPrice += int(priceList[i])
    return totalPrice

# Main Function
while True:
    menu = input("Enter menu : ")
    if menu.lower() == "exit":
        break
    else:
        price = input("Price : ")
        menuList.append(menu)
        priceList.append(price)
print("Total Price :",showSlipt(),"Baht")
print("Thank you!")