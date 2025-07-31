#!/usr/bin/env python3
# ธีรวิทย์ คำลืลือ (แทน)
# 680510716
# HW02_1
# 204111 Sec 003

def _RequestUserInput() -> float:
    Slope_1: float = float(input("m1: "))
    yIntercept_1: float = float(input("b1: "))

    Slope_2: float = float(input("m2: "))
    yIntercept_2: float = float(input("b2: "))

    Slope_3: float = float(input("m3: "))
    yIntercept_3: float = float(input("b3: "))

    return Slope_1, yIntercept_1, Slope_2, yIntercept_2, Slope_3, yIntercept_3

def _FindIntersectionPoints() -> float:
    Slope_1, yIntercept_1, Slope_2, yIntercept_2, Slope_3, yIntercept_3 = _RequestUserInput()

    X1: float = (yIntercept_2 - yIntercept_1) / (Slope_1 - Slope_2)
    Y1: float = Slope_1 * X1 + yIntercept_1

    X2: float = (yIntercept_3 - yIntercept_1) / (Slope_1 - Slope_3)
    Y2: float = Slope_1 * X2 + yIntercept_1

    X3: float = (yIntercept_3 - yIntercept_2) / (Slope_2 - Slope_3)
    Y3: float = Slope_2 * X3 + yIntercept_2

    return X1, Y1, X2, Y2, X3, Y3

def FindArea() -> float:
    X1, Y1, X2, Y2, X3, Y3 = _FindIntersectionPoints()
    Area: float = round( abs( X1*(Y2-Y3) + X2*(Y3-Y1) + X3*(Y1-Y2) ) / 2, 3)
    return Area

TriangleArea: float = FindArea()
print(f"{TriangleArea:.3f}")
