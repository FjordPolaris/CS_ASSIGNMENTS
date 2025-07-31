#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW03_3
# 204111 Sec 003

import math

def main():
    assert(kth_digit(789, 0) == 9)
    assert(kth_digit(789, 2) == 7) 
    assert(kth_digit(789, 3) == 0)
    assert(kth_digit(0, 0) == 0)

    assert(set_kth_digit(2343, 2, 7) == 2743)
    assert(set_kth_digit(51, 0, 2) == 52)
    assert(set_kth_digit(1, 2, 5) == 501)
    print("Ok")

def kth_digit(number: int, k: int) -> int:
    AbsoluteNum: int = abs(number)
    Digit: int = math.floor(AbsoluteNum / (10**k) % 10) 
    return Digit

def set_kth_digit(number: int, k: int, value: int) -> int:
    num: int = number
    digit: int = kth_digit(number, k)
    digit *= 10**k
    num -= digit
    num += value * (10**k)
    #print(num)
    return num

if __name__ == "__main__":
    #set_kth_digit(1234, 2, 5)
    main()
