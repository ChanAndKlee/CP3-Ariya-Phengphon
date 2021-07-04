def calVAT(price):
    finalPrice = price + ((7 / 100) * price)
    return finalPrice


price = int(input("Price: "))
print("Final Price (VAT included): ", calVAT(price))
