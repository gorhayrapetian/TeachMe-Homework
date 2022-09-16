class Triangle:
    right_triangle = True

    def __init__(self, a, b, c):
        self.a = a  # altitude
        self.b = b  # base
        self.c = c  # hypotenuse

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        return (self.a + self.b) / 2


triangle_1 = Triangle(3, 4, 5,)
triangle_2 = Triangle(8, 6, 10)

print('The area of triangle 1 is', triangle_1.area())
print('the perimeter of triangle 2 is', triangle_2.perimeter())