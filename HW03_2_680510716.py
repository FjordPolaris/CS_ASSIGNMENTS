#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW03_2
# 204111 Sec 003

import math

def main():
    assert(kth_digit(789, 0) == 9)
    assert(kth_digit(789, 2) == 7) 
    assert(kth_digit(789, 3) == 0)
    assert(kth_digit(0, 0) == 0)
    print("Ok")


def kth_digit(number: int, k: int) -> int:
    AbsoluteNum: int = abs(number)
    Digit: int = math.floor(AbsoluteNum / (10**k) % 10) 
    return Digit
    
if __name__ == "__main__":
    main()
