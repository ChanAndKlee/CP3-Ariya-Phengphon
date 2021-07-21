# Import library
import tkinter
from tkinter import *
import math
from tkinter.ttk import Combobox
from forex_python.bitcoin import BtcConverter

mainWindow = Tk()
mainWindow.geometry('1600x600')

def leftClickButton(event):
    if option.get() != "":
        result = b.convert_to_btc(int(entry_cur.get()), option.get())
        result2 = b.convert_to_btc(int(entry_cur.get()), optionTwo.get())
        label_cur1.configure(text = option.get())
        label_cur2.configure(text = optionTwo.get())
        label_bitcoin1.configure(text = result)
        label_bitcoin2.configure(text = result2)
    elif option.get() == "" or entry_cur.get() == "":
        label_bitcoin1.configure(text = 'ERROR, pls check your input again!')
    else:       # Not input anything
        label_bitcoin1.configure(text='ERROR, pls check your input again!')

def discard():
    exit()

# Create an object to access class CurrencyRates
b = BtcConverter()
label_symbol = Label(mainWindow, text = 'Amount to Bitcoin Conversion' + " (" + b.get_symbol()+")",
                     fg = '#B3816E', bg = '#DED2AA', font = ('Cooper Std Black', 30)).grid(row = 1, column = 1)

# Choosing currency text 1,2
Label(mainWindow, text = '1.] Choose Currency 1 => ',
      fg = '#B2A6BD', font = ('Cooper Std Black', 25)).grid(row = 2, column = 0)
Label(mainWindow, text = '   Choose Currency 2 => ',
      fg = '#B2A6BD', font = ('Cooper Std Black', 25)).grid(row = 3, column = 0)
# Input money text
Label(mainWindow, text = '2.] Input money (NO Comma!) => ',
      fg='#C7A26B', font=('Cooper Std Black', 25)).grid(row = 4, column = 0)

label_cur1 = Label(mainWindow, text = 'Currency 1 Conversion', fg = '#C7A26B',
      font = ('Cooper Std Black', 25))
label_cur1.grid(row = 5, column = 0)

label_cur2 = Label(mainWindow, text = 'Currency 2 Conversion', fg = '#C7A26B',
      font = ('Cooper Std Black', 25))
label_cur2.grid(row = 5, column = 1)

label_bitcoin1 = Label(mainWindow, text = 'XXX',
                      fg='#963A2F', font=('Cooper Std Black', 25))
label_bitcoin1.grid(row = 6, column = 0)

label_bitcoin2 = Label(mainWindow, text = 'XXY',
                       fg='#963A2F', font=('Cooper Std Black', 25))
label_bitcoin2.grid(row = 6, column = 1)

# Combobox Creation
n = StringVar()
option = Combobox(mainWindow, width = 20,
                  font = ('Cooper Std Black', 20), textvariable = n)
option.grid(row = 2, column = 1)

option['values'] = ('BGN', 'EUR',
                    'GBP', 'IDR',
                    'ILS', 'INR',
                    'PHP', 'THB',
                    'USD', 'ZAR')
n2 = StringVar()
optionTwo = Combobox(mainWindow, width = 20,
                     font = ('Cooper Std Black', 20), textvariable = n2)
optionTwo.grid(row = 3, column = 1)

optionTwo['values'] = ('BGN', 'EUR',
                    'GBP', 'IDR',
                    'ILS', 'INR',
                    'PHP', 'THB',
                    'USD', 'ZAR')

# Input money box
entry_cur = Entry(mainWindow, fg = '#C7A26B',
                  font = ('Cooper Std Black', 20), width = 21)
entry_cur.grid(row = 4, column = 1)

# Create button to process
but_process = Button(mainWindow, text = 'Calculate',
                 fg = '#FFFEE9', bg = '#ABA676', font = ('Cooper Std Black', 20), width = 30)
but_process.grid(row = 7, column = 0)       # Using grid here, so it can call 'bind function'

# Exit Button
Button(mainWindow, text = 'Exit', command = discard,
       fg = '#FFFEE9',  bg = '#963A2F',
       font = ('Cooper Std Black', 20), width = 30).grid(row = 7, column = 1)

# Get values from but_process
but_process.bind('<Button-1>', leftClickButton)
mainloop()