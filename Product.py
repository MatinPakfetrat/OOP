"""This is the Product Class File and it defines the product."""

import random

class Product:

    def __init__(self, code, name, price, cost, stock, units):
        """Constructs the product."""
        self.code = code
        self.name = name
        self.price = price
        self.cost = cost
        self.stock = stock
        self.manufacture_units = units

    def display(self):
        """Displays monthly production and sale of the product and the net profit."""

        print("Product code:", self.code)
        print("Product name:", self.name)
        print("Sale price:", self.price, "CAD")
        print("Manufacture cost:", self.cost, "CAD")
        print("Monthly production:", self.manufacture_units, "(Approx.)")

        total_sold = 0  #This is to calculate the total of sold units.

        for i in range(1, 13):
            self.stock += self.manufacture_units
            sold = random.randrange(self.manufacture_units-10, self.manufacture_units+11)  #This is a randomly generated amount of sold units.

            if self.stock >= sold:  #This ensures that the stock never goes negative as it only sells as many units as are availablein the stock.
                self.stock -= sold
            else:
                sold = self.stock
                self.stock = 0    

            print("Month {}:".format(i))
            print("     Manufactured:", self.manufacture_units)
            print("     Sold:", sold)
            print("     Stock:", self.stock)
            total_sold += sold
        net_profit = ((total_sold*self.price)-(self.manufacture_units*12*self.cost))   #This calculates the net profit. 
        print("Net profit: {:.2f} CAD".format(net_profit))    
