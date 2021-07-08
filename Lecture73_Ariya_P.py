# Input Menu, calculate price automatically
systemMenu = {'เนื้อปิ้ง':15,'หมูปิ้ง':10,'ไก่ปิ้ง':10,'ข้าวเหนียว':5}  # All available Menu
menuList = []    # Customer's Menu List

def showSlipt():
    print("--- My Food ---")
    totalPrice = 0
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        totalPrice += menuList[i][1]
    return totalPrice

def printMenu():
    print("==> Menu here <==")
    print("1. เนื้อปิ้ง     15 Baht")
    print("2. หมูปิ้ง     10 Baht")
    print("3. ไก่ปิ้ง      10 Baht")
    print("4. ข้าวเหนียว   5 Baht")

# Main Function
printMenu()
while True:
    menu = input("Enter menu : ")   # Input Menu from customer
    if menu.lower() == "exit":
        break
    else:
        menuList.append([menu,systemMenu[menu]])         # Add List in List   [[1,2],[3,4]]
# print(systemMenu.get('ข้าวเหนียว'))                       # Get Value by using key
# print(menuList)
print("Total Price :",showSlipt(),"Baht")
print("Thank you!")