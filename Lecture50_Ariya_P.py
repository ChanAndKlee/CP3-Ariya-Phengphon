# Basic Function in Python
def addNumber(x,y):
    print(x,"+",y,"=",x+y)

def minusNumber(x,y):
    print(x,"-",y,"=",x-y)

def multiplyNumber(x,y):
    print(x,"*",y,"=",x*y)

def diviNumber(x,y):
        print(x,"/",y,"=",x/y)

a = int(input("x: "))
b = int(input("y: "))
addNumber(a,b)
minusNumber(a,b)
multiplyNumber(a,b)
diviNumber(a,b)