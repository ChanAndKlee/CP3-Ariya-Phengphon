# List in List
menuList = []
def showSlipt():
    print("--- My Food ---")
    totalPrice = 0
    for i in range(len(menuList)):
        print(menuList[i][0],":",menuList[i][1])    # Normally menuList[i] refers to one big block in list like [1,2]
        totalPrice += int(menuList[i][1])           # menuList[i][0] -> refers to 'first word' in one block
    return totalPrice

# Main Function
while True:
    menu = input("Enter menu : ")
    if menu.lower() == "exit":
        break
    else:
        price = input("Price : ")
        menuList.append([menu,price])       # Add List in List   [[1,2],[3,4]]
print(menuList)
print("Total Price :",showSlipt(),"Baht")
print("Thank you!")