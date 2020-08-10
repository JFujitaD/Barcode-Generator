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
    def calculateCheckDigit(self):
        return  barval.BARCODE_VALUES[0]

    # Print barcode pattern in console
    def generateBarcode(self):
        for b in self.barcodeValues:
            print(b.pattern, end='')

    # Print the barcode value
    def toString(self):
        return 'Barcode: ' + self.text