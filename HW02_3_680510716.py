#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW02_3
# 204111 Sec 003

import math

def Calculate(OldPrice: float) -> int:
    NewPrice: int = math.floor((OldPrice-50) /100)
    NewPrice *= 100

    NewPrice += 98

    return int(NewPrice)

# MAIN

OldPrice: float = float(input("Old Price: "))
NewPrice: int = Calculate(OldPrice)
print("New Price: " + str(NewPrice))
