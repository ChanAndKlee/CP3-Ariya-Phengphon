# Operates two variables with operators

x = int(input("x: "))
y = int(input("y: "))
print(x,"+",y,"=",x+y)
print(x,"-",y,"=",x-y)
print(x,"*",y,"=",x*y)
print(x,"/",y,"=",x/y)


"""
!! Beware of ... !!
- (+) can't sfuse with two different data types like int and str
ex: x = "1"
    y = 5
    z = x + y
    print(z)        // Error => Runtime Error because you can't concatenate two variables that's not same type.
                    // Can fix by => Change to same type (int int, str str)
                                     ex: x = int("1")  or
                                         y = str(5)
"""