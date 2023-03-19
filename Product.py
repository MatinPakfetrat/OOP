"""This is the Product Class File and it defines the product."""

import random

class Product:

    def __init__(self, code, name, price, cost, stock, units):
        """Constructs products."""
        self.code = code
        self.name = name
        self.price = price
        self.cost = cost
        self.stock = stock
        self.manufacture_units = units
