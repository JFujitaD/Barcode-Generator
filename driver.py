from Barcode import Barcode
from tkinter import *

def buttonPressed(text):
    barcode = Barcode(text)
    barcode.generateBarcode()

root = Tk()

label = Label(root, text="Enter your barcode value")
label.pack()
entry = Entry(root)
entry.pack()
button = Button(root, text="Generate Barcode", command= lambda: buttonPressed(entry.get()))
button.pack()

root.mainloop()