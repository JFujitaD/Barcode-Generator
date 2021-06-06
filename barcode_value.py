"""A model for a barcode value.

    Attributes:
        symbol: A character such as !, 3, A, START, etc.
        value: Decimal value for each character/symbol.
        pattern: The binary pattern for the character/symbol.
"""
class BarcodeValue:
    def __init__(self, symbol, value, pattern):
        self.symbol = symbol
        self.value = value
        self.pattern = pattern