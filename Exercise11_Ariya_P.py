num = int(input("Enter number: "))
# Triangle [HAVE SPACE]
for a in range(1,num+1):            # 1 2 3 ระหว่าง 1-เลขนั้นๆ
    for b in range(num,a,-1):       # (3 2) (3) space
        print(" ",end=" ")
    print("* "*(2*a-1))             # Star

# Upside down Triangle [HAVE SPACE]
for i in range(num,0,-1):           # 3 2 1
    for j in range(num-i):          # (3-3) (3-2) (3-1)
        print(" ",end=" ")          # Space
    print("* "*(2*i-1))

print()

# Triangle [NO SPACE]
space = num - 1
star = 1
for x in range(num):
    print(" "*space,end=" ")
    print("*"*star)
    space-=1
    star+=2

# Upside down Triangle [NO SPACE]
sp = 0
st = num + (num-1)
for y in range(num):
    print(" "*sp,end=" ")
    print("*"*st)
    sp+=1
    st-=2