from Barcode import Barcode

barcode = Barcode('a')
print(barcode.toString())

barcode.generateBarcode()

barcode.calculateCheckDigit()