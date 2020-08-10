# Code-128 Values
from BarcodeValue import BarcodeValue

# Functions
def findUsingSymbol(symbol):
    for s in BARCODE_VALUES:
        if s.symbol == symbol:
            return s 
    return 0

def findUsingValue(value):
    for v in BARCODE_VALUES:
        if v.value == value:
            return v
    return 0
        

# Array of barcode values
BARCODE_VALUES = (
    # Functional Characters
    BarcodeValue('START', 104, '11010010000'),
    BarcodeValue('STOP', 0, '1100011101011'),

    # Special Characters
    BarcodeValue(' ', 1, '11011001100'),
    BarcodeValue('!', 1, '11001101100'),
    BarcodeValue('"', 2, '11001100110'),
    BarcodeValue('#', 3, '10010011000'),
    BarcodeValue('$', 4, '10010001100'),
    BarcodeValue('%', 5, '10001001100'),
    BarcodeValue('&', 6, '10011001000'),
    BarcodeValue("'", 7, '10011000100'),
    BarcodeValue('(', 8, '10001100100'),
    BarcodeValue(')', 9, '11001001000'),
    BarcodeValue('*', 10, '11001000100'),
    BarcodeValue('+', 11, '11000100100'),
    BarcodeValue(',', 12, '10110011100'),
    BarcodeValue('-', 13, '10011011100'),
    BarcodeValue('.', 14, '10011001110'),
    BarcodeValue('/', 15, '10111001100'),

    BarcodeValue(':', 26, '11100100110'),
    BarcodeValue(';', 27, '11101100100'),
    BarcodeValue('<', 28, '11100110100'),
    BarcodeValue('=', 29, '11100110010'),
    BarcodeValue('<', 30, '11011011000'),
    BarcodeValue('?', 31, '11011000110'),
    BarcodeValue('@', 32, '11000110110'),

    BarcodeValue('[', 59, '11100011010'),
    BarcodeValue('\\', 60, '11101111010'),
    BarcodeValue(']', 61, '11001000010'),
    BarcodeValue('^', 62, '11110001010'),
    BarcodeValue('_', 63, '10100110000'),
    BarcodeValue('`', 64, '10100001100'),

    BarcodeValue('{', 91, '11110110110'),
    BarcodeValue('|', 92, '10101111000'),
    BarcodeValue('}', 93, '10100011110'),
    BarcodeValue('~', 94, '10001011110'),

    # Numerical Values
    BarcodeValue('0', 16, '10011101100'),
    BarcodeValue('1', 17, '10011100110'),
    BarcodeValue('2', 18, '11001110010'),
    BarcodeValue('3', 19, '11001011100'),
    BarcodeValue('4', 20, '11001001110'),
    BarcodeValue('5', 21, '11011100100'),
    BarcodeValue('6', 22, '11001110100'),
    BarcodeValue('7', 23, '11101101110'),
    BarcodeValue('8', 24, '11101001100'),
    BarcodeValue('9', 25, '11100101100'),

    # Letters
    BarcodeValue('A', 33, '10100011000'),
    BarcodeValue('B', 34, '10001011000'),
    BarcodeValue('C', 35, '10001000110'),
    BarcodeValue('D', 36, '10110001000'),
    BarcodeValue('E', 37, '10001101000'),
    BarcodeValue('F', 38, '10001100010'),
    BarcodeValue('G', 39, '11010001000'),
    BarcodeValue('H', 40, '11000101000'),
    BarcodeValue('I', 41, '11000100010'),
    BarcodeValue('J', 42, '10110111000'),
    BarcodeValue('K', 43, '10110001110'),
    BarcodeValue('L', 44, '10001101110'),
    BarcodeValue('M', 45, '10111011000'),
    BarcodeValue('N', 46, '10111000110'),
    BarcodeValue('O', 47, '10001110110'),
    BarcodeValue('P', 48, '11101110110'),
    BarcodeValue('Q', 49, '11010001110'),
    BarcodeValue('R', 50, '11000101110'),
    BarcodeValue('S', 51, '11011101000'),
    BarcodeValue('T', 52, '11011100010'),
    BarcodeValue('U', 53, '11011101110'),
    BarcodeValue('V', 54, '11101011000'),
    BarcodeValue('W', 55, '11101000110'),
    BarcodeValue('X', 56, '11100010110'),
    BarcodeValue('Y', 57, '11101101000'),
    BarcodeValue('Z', 58, '11101100010'),

    BarcodeValue('a', 65, '10010110000'),
    BarcodeValue('b', 66, '10010000110'),
    BarcodeValue('c', 67, '10000101100'),
    BarcodeValue('d', 68, '10000100110'),
    BarcodeValue('e', 69, '10110010000'),
    BarcodeValue('f', 70, '10110000100'),
    BarcodeValue('g', 71, '10011010000'),
    BarcodeValue('h', 72, '10011000010'),
    BarcodeValue('i', 73, '10000110100'),
    BarcodeValue('j', 74, '10000110010'),
    BarcodeValue('k', 75, '11000010010'),
    BarcodeValue('l', 76, '11001010000'),
    BarcodeValue('m', 77, '11110111010'),
    BarcodeValue('n', 78, '11000010100'),
    BarcodeValue('o', 79, '10001111010'),
    BarcodeValue('p', 80, '10100111100'),
    BarcodeValue('q', 81, '10010111100'),
    BarcodeValue('r', 82, '10010011110'),
    BarcodeValue('s', 83, '10111100100'),
    BarcodeValue('t', 84, '10011110100'),
    BarcodeValue('u', 85, '10011110010'),
    BarcodeValue('v', 86, '11110100100'),
    BarcodeValue('w', 87, '11110010100'),
    BarcodeValue('x', 88, '11110010010'),
    BarcodeValue('y', 89, '11011011110'),
    BarcodeValue('z', 90, '11011110110')
)

