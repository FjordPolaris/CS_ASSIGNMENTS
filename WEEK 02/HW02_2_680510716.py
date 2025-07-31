#!/usr/bin/env python3
# ธีรวิทย์ คำลืลือ (แทน)
# 680510716
# HW02_2
# 204111 Sec 003

def _RequestInput() -> int:
    x: int = int(input("x: "))
    y: int = int(input("y: "))

    return x, y

def Calculate() -> int:
    x, y = _RequestInput()
    x -= 1
    sum: int = y*(y+1)*(2*y+1) / 6 - x*(x+1)*(2*x+1) /6 

    return int(sum)

print("sum is: " + str(Calculate()))
