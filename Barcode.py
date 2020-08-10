import barcode_values as barval

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

    # Print barcode pattern in console
    def generateBarcode(self):
        for b in self.barcodeValues:
            print(b.pattern, end='')

    # Print the barcode value
    def toString(self):
        return 'Barcode: ' + self.text