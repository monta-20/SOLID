class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
    
    def set_width(self, width):
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.width = height
        self.height = height

def test_rectangle(rectangle):
    rectangle.set_width(5)
    rectangle.set_height(4)
    expected = 20
    actual = rectangle.area()
    assert expected == actual, f"Expected {expected}, got {actual}"

# This works fine with Rectangle
rect = Rectangle(1, 1)
test_rectangle(rect)  # Passes

# This fails with Square even though it's a subclass
sq = Square(1)
test_rectangle(sq)  # Fails (Expected 20, got 16)


"""

Problem: Square inherits from Rectangle but changes the behavior of set_width/set_height, 
violating the LSP. Code that expects Rectangle behavior breaks when given a Square.

"""