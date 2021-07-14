# Corgi Farm GUI
# import tkinter
from tkinter import *               # Import all
# import tkinter                    # Connect with user interface (another way, above is easier)
def welcome():
    name = input("ใส่ชื่อเล่นของคุณ: ")
    print("สวัสดีคุณ "+name)
def login():
    name = name_var.get()           # Returns the entry's current text as a string
    numOrder = num_var.get()
    if name == "" or numOrder == "0":
        print("Pls enter your name and order first!")
    else:
        print("---------------------------------------")
        print("<< Welcome user! >>")
        print("Name: "+name)
        price = 0
        price = 30000 * int(numOrder)
        print("Pay >>",int(price),"Baht")
        print("Thank you for trusting our farm!")
        print("---------------------------------------")
def discard():
    exit()                          # Exit the program

# Create and set window size
mainWindow = Tk()                   # Create window name is mainWindow
mainWindow.geometry('1200x600')      # set size of window

Label(mainWindow, text = "Welcome to Corgi Farm!",  fg = "#989CED", bg = "#F1E3F5", font =("BoonTook Mon Ultra",30)).grid(row = 1, column = 0)
name_var = StringVar()              # Declaring variables for storing input
textOk_label = Label(mainWindow, text = "คุณชื่ออะไร? (ชื่อเล่น)",height=1, fg = "#541E18", bg = "#EE8070", font=("BoonTook Mon Ultra",30)).grid(row = 2, column = 0)
name_entry = Entry(mainWindow,textvariable = name_var, fg = "#2C6B96", bg = "#F8EFD4", font=("BoonTook Mon Ultra",30)).grid(row=2, column = 1)          # text box (The entry widget)

# login and discard button
need_but = Button(mainWindow, text = "ตกลง", command = login, fg = "#F5D788", bg = "#469D8B", font=("BoonTook Mon Ultra",30)).grid(row = 4, column = 0)
noNeed_but = Button(mainWindow, text = "ยกเลิก", command = discard, fg = "#F5D788", bg = "#E12E4B", font=("BoonTook Mon Ultra",30)).grid(row = 4, column = 1)
# Button(mainWindow, image = corgi, compound = CENTER, bg = "#F9D6C0").grid(row = 4, column = 1)

# Main
num_var = StringVar()
ask_label = Label(mainWindow, text = "> ต้องการคอร์กี้ (/ตัว)",fg = "#541E18", bg = "#EBB8BD", font=("BoonTook Mon Ultra",30)).grid(row = 3, column = 0)
spinbox = Spinbox(mainWindow, from_=0, to=10, textvariable = num_var, fg = "#2C6B96", bg = "#F8EFD4",font=("BoonTook Mon Ultra",30)).grid(row = 3, column = 1)

# Picture

# print this screen out
# mainWindow.mainloop()
mainloop()
