from tkinter import *
import math
main = Tk()
main.geometry('600x180')
def leftClickButton(event):
    bmi = float(weight_entry.get())/math.pow(float(height_entry.get())/100,2)
    ans_label.configure(text=bmi)   # display on screen, replace text to new text
    # Criteria BMI
    if bmi < 18.50:
        textAns_label.configure(text="[You are 'Underweight'!]")
    elif bmi > 18.50 and bmi < 24.99:
        textAns_label.configure(text="[You are Average.]")
    elif bmi > 25.00 and bmi < 29.99:
        textAns_label.configure(text="[You are Mildly Increased.]")
    elif bmi > 30.00:
        textAns_label.configure(text="[You are Obese!]")
    # textAns_label.configure(text=)
# Input weight and height from user
weight_label = Label(main, text = 'Weight (kg) : ',fg = '#51A2DA',bg = '#F5D788', font = ('Cooper Black',20)).grid(row = 0, column = 0)
weight_entry = Entry(main, fg = '#51A2DA', font = ('Cooper Black',20))
weight_entry.grid(row = 0, column = 1)    # set value by method, add grid, can't directly pull (old way) it's non type

height_label = Label(main, text = 'Height (cm) : ',fg = '#51A2DA',bg = '#F5D788', font = ('Cooper Black',20)).grid(row = 1, column = 0)
height_entry = Entry(main, fg = '#51A2DA', font = ('Cooper Black',20))
height_entry.grid(row = 1, column = 1)    # set value by method, add grid, can't directly pull (old way) it's non type

cal_but = Button(main, text = 'Calculate BMI', fg = '#F8EFD4',bg = '#BA3F24', font = ('Cooper Black',20))
cal_but.grid(row = 2, column = 0)
cal_but.bind('<Button-1>', leftClickButton)           # Button-1 > press left mouse, leftClickButton > tell this button what to do when click left

ans_label = Label(main, text = '<Ans>', fg = '#2C6B96', font = ('Cooper Black',20))
ans_label.grid(row = 2, column = 1)

textAns_label = Label(main, text = 'Based on BMI Criteria', fg = '#2C6B96', font = ('Cooper Black',20))
textAns_label.grid(row = 3, column = 1)

main.mainloop()