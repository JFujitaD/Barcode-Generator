from barcode_value import BarcodeValue
import barcode_values as barval
from tkinter import *


# Pixel size of each bar
BAR_SIZE = 5
QUIET_SIZE = 30

"""A model representation of a barcode, including various functions."""
class Barcode:
    def __init__(self, text):
        self.text = text
        self.text_array = ()
        self.barcode_values = []

        # Save characters in text as individual elements in text_array
        self.text_array = (ch for ch in text)
        
        # For every character in text_array, find the correct barcode value
        self.barcode_values.append(barval.findUsingSymbol('START'))

        for c in self.text_array:
            self.barcode_values.append(barval.findUsingSymbol(c))

        self.barcode_values.append(self.calculateCheckDigit())    
        self.barcode_values.append(barval.findUsingSymbol('STOP'))

    # Calculate the check digit for the barcode
    # Step 1: Use value of start Code B = 104
    # Step 2: Multiply character values by their position (Starting at 1)
    # Step 3: Add them all together
    # Step 4: total % 103
    def calculateCheckDigit(self) -> BarcodeValue:
        """Calculates the check digit for the barcode
        
            Returns:
                BarcodeValue: Barcode value information
        """
        total = 104
        i = 0
        for b in self.barcode_values:
            total += b.value * i
            i += 1 
        return barval.findUsingValue(total % 103)

    def generateBarcode(self):
        """Generate visual pattern from collected data"""
        pattern = ''
        for b in self.barcode_values:
            pattern += b.pattern
        print(pattern)

        # GUI Setup
        root = Tk()
        root.title('Barcode Generator')
        width = (len(pattern) * BAR_SIZE) + (QUIET_SIZE * 2)
        height = width / 3

        label = Label(root, text=self.text, font=("Courier", 16))
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
