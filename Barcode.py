import barcode_values as barval
from tkinter import *

# Pixel size of each bar
BAR_SIZE = 3
QUIET_SIZE = 10

class Barcode:

    def __init__(self, text):
        self.text = text
        self.textArray = ()
        self.barcodeValues = []

        # Save characters in text as individual elements in textArray
        self.textArray = (ch for ch in text)
        
        # For every character in textArray, find the correct barcode value
        self.barcodeValues.append(barval.findUsingSymbol('START'))

        for c in self.textArray:
            self.barcodeValues.append(barval.findUsingSymbol(c))

        self.barcodeValues.append(self.calculateCheckDigit())    
        self.barcodeValues.append(barval.findUsingSymbol('STOP'))

    # Calculate the check digit for the barcode
    # Step 1: Use value of start Code B = 104
    # Step 2: Multiply character values by their position (Starting at 1)
    # Step 3: Add them all together
    # Step 4: total % 103
    def calculateCheckDigit(self):
        total = 104
        i = 0
        for b in self.barcodeValues:
            total += b.value * i
            i += 1 
        return barval.findUsingValue(total % 103)

    # Generate visual pattern from collected data using Tkinter
    def generateBarcode(self):
        pattern = ''
        for b in self.barcodeValues:
            pattern += b.pattern
        print(pattern)

        # GUI Setup
        root = Tk()
        width = (len(pattern) * BAR_SIZE) + (QUIET_SIZE * 2)
        height = width / 3

        label = Label(root, text=self.text)
        label.pack()

        # Draw on Canvas
        canvas = Canvas(root, width=width, height=height)
        patternArray = (ch for ch in pattern)
        x = QUIET_SIZE
        y = QUIET_SIZE / 2

        for b in patternArray:
            if(b == '1'):
                canvas.create_rectangle(x, y, x + BAR_SIZE, height - y, fill='#000000')
            x += BAR_SIZE
        canvas.pack()

        root.mainloop()


    # Print the barcode value
    def toString(self):
        return 'Barcode: ' + self.text