"This file contains the functions for input validation."

def pcode_valid():
    "This function gets the product code and validates it."

    while True:  #This loop will keep running until a valid input has been given.
        code = int(input("Please enter the product code(from 100 to 1000): "))
        if 100 < code < 1000:
            return code
        print("Input is invalid!")

def pname_valid():
    "This function gets the product name and validates it."

    while True:  #This loop will keep running until a valid input has been given.
        name = input("Please enter the product name: ")
        if name.isalpha():
            return name
        print("Input is invalid!")

def price_valid():
    "This function gets the product sale price and validates it."        

    while True:
        price = float(input("Please enter the product sale price: "))
        if price > 0:
            return price
        print("Input is invalid!")

def cost_valid():
    "This function gets the product manufacture cost and validates it."        

    while True:
        cost = float(input("Please enter the product manufacture cost: "))
        if cost > 0:
            return cost
        print("Input is invalid!")

def stock_valid():
    "This function gets the product stock level and validates it."        

    while True:
        stock = int(input("Please enter the product stock level: "))
        if stock > 0:
            return stock
        print("Input is invalid!")

def units_valid():
    "This function gets the product estimated monthly units manufactured and validates it."        

    while True:
        units = int(input("Please enter the product estimated monthly units manufactured: "))
        if units >= 0:
            return units
        print("Input is invalid!")    