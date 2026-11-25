class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * (22/7)

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())