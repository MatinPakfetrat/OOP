"This is the Application Class File and it performs all the interactions."

from Product import Product
from Validate import *

class Application:
    
    def run(self):
        """Runs the program."""
        p = Product(pcode_valid(), pname_valid(), price_valid(), cost_valid(), stock_valid(), units_valid())
        p.display()

prog = Application()
prog.run()        