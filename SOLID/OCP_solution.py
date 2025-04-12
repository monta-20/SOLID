from abc import ABC , abstractmethod
class Discountable(ABC):
    @abstractmethod
    def claculate_discount(self):
        pass

class ElectronicProduct(Discountable) : 
    def __init__(self , price):
        self.price = price
    def claculate_discount(self):
        return self.price * 0.10
       
class FashionProduct(Discountable):
    def __init__(self, price):
        self.price = price
    
    def calculate_discount(self):
        return self.price * 0.20

class DiscountCalculator:
    def calculate_discount(self, product: Discountable):
        return product.calculate_discount()

# Usage
electronic = ElectronicProduct(1000)
fashion = FashionProduct(500)

calculator = DiscountCalculator()
print(calculator.calculate_discount(electronic))  # Output: 100.0
print(calculator.calculate_discount(fashion))    # Output: 100.0

"""
Key Improvements:

     Created an abstract Discountable base class with the required interface

     Each product type implements its own discount calculation

     DiscountCalculator doesn't need to change when new product types are added

     New product types can be added by creating new classes that implement Discountable

"""