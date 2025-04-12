class Product : 
    def __init__(self , type , price) :
        self.type = type 
        self.price = price
class DiscountCalculator:
    def calculate_discount(self , product) :
        if product.type == "electronic" : 
            return product.price * 0.10
        elif product.type == "fashion" : 
            return product.price * 0.20
        else :
            return 0.0

# Usage
electronic = Product("electronic", 1000)
fashion = Product("fashion", 500)

calculator = DiscountCalculator()
print(calculator.calculate_discount(electronic))  # Output: 100.0
print(calculator.calculate_discount(fashion))    # Output: 100.0

# Problem: To add a new product type, we must modify the DiscountCalculator class.