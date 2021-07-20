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
        label_bitcoin.configure(text = result)
    elif option.get() == "" or entry_cur.get() == "":
        label_bitcoin.configure(text = 'ERROR, pls check your input again!')
    else:       # Not input anything
        label_bitcoin.configure(text='ERROR, pls check your input again!')

def discard():
    exit()

# Create an object to access class CurrencyRates
b = BtcConverter()
label_symbol = Label(mainWindow, text = 'Amount to Bitcoin Conversion' + " (" + b.get_symbol()+")",
                     fg = '#B3816E', bg = '#DED2AA', font = ('Cooper Std Black', 30)).grid(row = 1, column = 1)

Label(mainWindow, text = '1.] Choose currency => ',
      fg = '#B2A6BD', font = ('Cooper Std Black', 25)).grid(row = 2, column = 0)

Label(mainWindow, text = '2.] Input money below (NO Comma!)',
      fg='#C7A26B', font=('Cooper Std Black', 25)).grid(row = 3, column = 0)

label_cur = Label(mainWindow, text = 'Currency', fg = '#C7A26B',
      font = ('Cooper Std Black', 25)).grid(row = 4, column = 0)

Label(mainWindow, text = 'Bitcoin', fg = '#C7A26B',
      font = ('Cooper Std Black', 25)).grid(row = 4, column = 1)

label_bitcoin = Label(mainWindow, text = 'XXX',
                      fg='#963A2F', font=('Cooper Std Black', 25))
label_bitcoin.grid(row = 5, column = 1)

# Combobox Creation
n = StringVar()
option = Combobox(mainWindow, width = 20,
                  font = ('Cooper Std Black', 20), textvariable = n)
option['values'] = ('BGN', 'EUR',
                    'GBP', 'IDR',
                    'ILS', 'INR',
                    'PHP', 'THB',
                    'USD', 'ZAR')
option.grid(row = 2, column = 1)
entry_cur = Entry(mainWindow, fg = '#C7A26B',
                  font = ('Cooper Std Black', 20), width = 15)
entry_cur.grid(row = 5, column = 0)

# Create button to process
but_process = Button(mainWindow, text = 'Calculate',
                 fg = '#FFFEE9', bg = '#ABA676', font = ('Cooper Std Black', 20), width = 30)
but_process.grid(row = 6, column = 0)       # Using grid here, so it can call 'bind function'

# Exit Button
Button(mainWindow, text = 'Exit', command = discard,
       fg = '#FFFEE9',  bg = '#963A2F',
       font = ('Cooper Std Black', 20), width = 30).grid(row = 6, column = 1)

# Get values from but_process
but_process.bind('<Button-1>', leftClickButton)
mainloop()


# Compare deal TBA - THB and USD, which is higher/lower?, recommendation part
# Add another currency below, then compare box1 and box2 when click calculate (change calculate to compare button)
