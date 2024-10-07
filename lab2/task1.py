import math
def trapezoid(base1, base2, height):
    return ((base1 + base2) / 2) * height

area1 = trapezoid(5, 7, 10)
print(f"Area of the trapezoid: {area1}")

def parallelogram(base, height):
    return base * height

area2 = parallelogram(8, 5)
print(f"Area of the parallelogram: {area2}")

def cylinder(radius, height):
    return math.pi * radius * radius* height

def cylinder_sa(radius, height):
    return 2 * math.pi * radius * (radius + height)

volume = cylinder(3, 7)
surface_area = cylinder_sa(3, 7)
print(f"Volume of the cylinder: {volume}")
print(f"Surface area of the cylinder: {surface_area}")
