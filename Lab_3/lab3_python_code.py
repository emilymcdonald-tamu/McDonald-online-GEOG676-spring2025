
# create classes
class Shape():
    def __init__(self):
        pass

# I added extra spaces over the classes and second defs
# to fix problem "expected 2 blank lines, found 1"

# I changed variable names from single letter to spelled
# out names to fix problem "ambiguous variable name'l'"


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def getArea(self):
        return 0.5 * self.base * self.height


# read txt file
file = open(r'C:\Users\anna2\OneDrive\Documents\GEOG676ClassMaterial\shape.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    components = line.split(',')
    shape = components[0]

    if shape == 'Rectangle':
        rect = Rectangle(int(components[1]), int(components[2]))
        print('Area of Rectangle is: ', rect.getArea())
    elif shape == 'Circle':
        cirl = Circle(int(components[1]))
        print('Area of Circle is: ', cirl.getArea())
    elif shape == 'Triangle':
        tri = Triangle(int(components[1]), int(components[2]))
        print('Area of Triangle is: ', tri.getArea())
    else:
        pass
