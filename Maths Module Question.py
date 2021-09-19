""" 1. Area of an equilateral triangle can be computed as (root 3/4) * a ** 2 where a is its side. Write a program to
       obtain side form user and print the area of equilateral triangle with side a."""
"""
import math
side = float(input("Enter the side of the triangle: "))
Area = (math.sqrt(3)/4) * side * side
print(f"Area of Triangle is {Area}")
"""

""" 2. Area of a polygon can be computed as: (1/2) * n * sin(360 degree / n) * s ** 2
       Where n = number of sides  and s = length from centre to a corner.
       Write a program to obtain values n and s form user and print area of polygon."""

import math
def polygonarea(n,s):
    area = (1 / 2) * n * (math.sin(360 / n) * s ** 2)
    print(f"Area of a polygon is {area}")

s = float(input("Enter Length from centre to a coner: "))
n = int(input("Enter number of sides: "))
