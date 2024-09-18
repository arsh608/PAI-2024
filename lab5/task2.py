from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def area(self, length, width):
        return length*width

class triangle(shape):
    def area(self, base, height):
        return (0.5*base*height)

class square(shape):
    def area(self, length):
        return length*length

a= rectangle()
b= triangle()
c= square()

print(f" The area of rectangle length 5 and width 2 is: {a.area(5,2)}")
print(f" The area of triangle base 3 and height 8 is: {b.area(3,8)}")
print(f" The area of square with side 4 is: {c.area(4)}")
