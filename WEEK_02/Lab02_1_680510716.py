#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab02_1
# 204111 Sec 003

import math


def CalculateArea(A: float, B: float, C: float) -> int:

    SemiPerimeter: float = (A + B + C) / 2

    # Prevent error in math.sqrt function when SemiPerimeter < a, b, or c, returning a negative integer
    # a: int | float = min(posA, SemiPerimeter - 1)
    # b: int | float = min(posB, SemiPerimeter - 1)
    # c: int | float = min(posC, SemiPerimeter - 1)

    # Main calculation
    TriangleArea: int | float = math.sqrt(
        SemiPerimeter * (SemiPerimeter - A) * (SemiPerimeter - B) * (SemiPerimeter - C)
    )

    return int(math.ceil(TriangleArea))


a: float = float(input("a: "))
b: float = float(input("b: "))
c: float = float(input("c: "))
Area: str = str(CalculateArea(a, b, c))

print("area: " + Area)
