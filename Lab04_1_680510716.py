#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab04_1
# 204111 Sec 003


# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function circle_intersect()

import math

def main():
    test_circle_intersect()

def circle_intersect(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float, epsilon=10**-6) -> int:

    Distance: float = math.sqrt( ((x1 - x2)**2) + ((y1 - y2)**2) )
    CombinedRadius: float = r1 + r2
    DistanceOffset: float = abs(Distance - CombinedRadius)
    #print(DistanceOffset, Distance, CombinedRadius)
    
    if Distance == CombinedRadius or DistanceOffset < epsilon:
        return 0
    elif Distance < CombinedRadius:
        return 1
    elif Distance > CombinedRadius and DistanceOffset >= epsilon:
        return -1
    else:
        print("SHOULD NOT BE PRINTED")
        return 2


def test_circle_intersect():
    assert circle_intersect(2, 3, 5, 5, 7, 1) == 1
    assert circle_intersect(0, 0, 2.5, 3, 4, 2.5) == 0
    assert circle_intersect(1, 1, 5, 6, 17, 7) == -1

    # now using specified epsilon
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=1.5) == 0
    print("all ok!")


if __name__ == '__main__':
    main()


