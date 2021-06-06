from barcode import Barcode
from tkinter import *
from tkinter import messagebox


def buttonPressed(text):
    try:
        if len(text) == 0:
            raise Exception()
        barcode = Barcode(text)
        barcode.generateBarcode()
    except:
        messagebox.showerror(title="Error", message="Please enter something in the box")

root = Tk()
root.title('Barcode Generator')

label = Label(root, text="Enter your barcode value", font=("Courier", 16))
label.pack()
entry = Entry(root, font=("Courier", 16))
entry.pack()
button = Button(root, text="Generate Barcode", command= lambda: buttonPressed(entry.get()), font=("Courier", 16))
button.pack()

root.mainloop()