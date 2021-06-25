username = input("Username: ")
pwd = input("Password: ")

if username == pwd:
    print("Can't log in, username and password need to be different")
else:
    print("-----------------------------------")
    print("Welcome to Bare bears supermarket!")

# Convert the first digit to capital letter
# [0]. Check first index, and convert it.
# [1]. Concatenate each digit except the first digit.

    firstChar = username[0]
    if firstChar.isupper() == False:
        firstChar = firstChar.upper()

    newStr = ""
    for i in range(len(username)):
        if i != 0:
            newStr += username[i]
    print("Hello Mr./Mrs. "+firstChar+newStr+"!")
    print("-----------------------------------")

    # Print out Menu
    print("")
    print(" => Menu <= ")
    print("1. Ham       15 BB.")
    print("2. Cheese     5 BB")
    print("3. Sausage   10 BB")

    print("")
    print("Enter number list")
    countPros = 1
    # Start Order Here!!! #
    print(" * Enter [Q/q] for quitting the menu. *")


    order = input("What would you like? => ")

    total_PR = 0
    ham_PR = 15
    cheese_PR = 5
    sau_PR = 10

    print("")
    print(" * * Enter [F/f] for continuing next process. * *")

    # Calculate [order] price
    if order == "q" or order == "Q":
        countPros = 3
    elif order == "1" or order == "2" or order == "3":
        while order == "1" or order == "2" or order == "3":
            if order == "1":
                total_PR += ham_PR
                print("Price: ",total_PR)
                order = input("What would you like? [f/F for calculate price]=> ")
                if order == "F" or order == "f":   # Continue next process
                    countPros = 2
                elif order != "1" or order != "2" or order != "3":
                    print("Wrong input")
            elif order == "2":
                total_PR += cheese_PR
                print("Price: ", total_PR)
                order = input("What would you like? [f/F for calculate price]=> ")
                if order == "F" or order == "f":   # Continue next process
                    countPros = 2
                elif order != "1" or order != "2" or order != "3":
                    print("Wrong input")
            elif order == "3":
                total_PR += sau_PR
                print("Price: ", total_PR)
                order = input("What would you like? [f/F for calculate price]=> ")
                if order == "F" or order == "f":   # Continue next process
                    countPros = 2
                elif order != "1" or order != "2" or order != "3":
                    print("Wrong input")
    else: # Other case, not match case
        print("Wrong input")

    if countPros == 2:
        # Check member/not member
        print("")
        print("- Check Member -")
        print("Enter 0 for 'NOT' have member")
        print("Enter 1 for have member")
        checkMember = input("Have Member? => ")
        # If member discount 10 percent of price u buy, if not nothing happen
        if checkMember == "0":   # Correct since first time
            final_price = total_PR
            print("Final Price:", final_price)
            countPros = 3
        elif checkMember == "1":
            final_price = total_PR - ((10 / 100) * total_PR)
            print("Final Price:", final_price)
            countPros = 3
        else:  # Wrong input, not "1" or "0"
            while checkMember != "1" or checkMember != "0":
                checkMember = input("Have Member? => ")
                if checkMember == "1":
                    final_price = total_PR - ((10/100)*total_PR)
                    print("Final Price:",final_price)
                    break
                elif checkMember == "2":
                    final_price = total_PR
                    print("Final Price:", final_price)
                    break
    if countPros == 3:
        print("")
        print("Thank you for purchasing!")
        print("Hope to see u again")
        print("-----------------------------------")