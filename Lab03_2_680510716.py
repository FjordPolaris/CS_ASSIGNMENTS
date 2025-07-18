#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab03_2
# 204111 Sec 003

import math

def main():
    assert(square_area(5.25) == 11.249999999999998)
    print("All OK")

def square_area(x: float) -> float:
    # By using pythagorean theorem, C^2 = A^2 + B^2 -> C = sqrt( x^2 + (2x)^2 )
    # C = sqrt(x^2 + 4x^2) -> sqrt(5x^2) -> sqrt(5) * sqrt(x^2)
    # Ultimately, the Hypotenuse formula is square root of 5 times x 
    Hypotenuse = math.sqrt(5) * x

    # In order to get the height of the triangle, area of the triangle is required for solving the equation
    TriangleArea: float = (x * (2*x)) /2 

    # Finding the height of the big triangle in order to compare between 2 similar triangles
    Height: float = (TriangleArea * 2) / Hypotenuse
    
    # Oops!
    # Compare 2 triangles; Hypotenuse/s = h/(h-s); 
    # Base of big triangle / base of a small one above the sqre = Height of big triangle / Height of the small one
    # Eventually when the equation is solve, s = x*sqrt(5) *h / h+(x*sqrt(5))
    s = (math.sqrt(5)*x *Height) / (Height + math.sqrt(5)*x)

    area: float = float(s * s)
    #print(area)
    return area


if __name__ == "__main__": 
    main()
