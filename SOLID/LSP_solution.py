from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, size):
        self.size = size
    
    def set_size(self, size):
        self.size = size
    
    def area(self):
        return self.size ** 2

def print_area(shape: Shape):
    print(f"Area: {shape.area()}")

# Usage
rect = Rectangle(5, 4)
sq = Square(5)

print_area(rect)  # Area: 20
print_area(sq)    # Area: 25

"""

Key Improvements:

    Created a common abstract base class Shape

    Both Rectangle and Square implement area() but maintain their own specific behaviors

    Client code (print_area) works with the abstract Shape type

    Subclasses don't violate parent class contracts

"""



#Real Example 

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment for ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment for ${amount}")

class BankTransferProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing bank transfer for ${amount}")

def checkout(processor: PaymentProcessor, amount):
    processor.process_payment(amount)

# Usage
credit_card = CreditCardProcessor()
paypal = PayPalProcessor()
bank_transfer = BankTransferProcessor()

checkout(credit_card, 100)
checkout(paypal, 50)
checkout(bank_transfer, 200)