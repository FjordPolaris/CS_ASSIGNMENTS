#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab06_1
# 204111 Sec 003






def square_frame(n: int, sep: str = "") -> None:
    _end: int = n ** 2
    nums_alpha: list = list(range(1, _end))
    
    nums_beta: list = list(map(lambda x: str(list(range(1, x + 1))), nums_alpha))
    print(nums_beta)


if __name__ == "__main__":
    square_frame(3)
