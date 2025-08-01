#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab06_1
# 204111 Sec 003


def square_frame(n: int, sep: str = "") -> None:
    size: int = n * n
    padding_space: int = len(str(size))
    nums: list = list(map(lambda x: int(str(x).zfill(padding_space)), range(1, size + 1)))
    print("NUMS:", nums)
    
    rows: list = list(map(lambda y: str(nums[y*n:(y+1)*n]), range(n)))
    print("ROWS:", rows)

    list_a: list = list(map(lambda r: r.strip('[]'), rows))
    print("LIST:", list_a)

    result = '\n'.join(list_a).replace(',', '')
    print(result)


if __name__ == "__main__":
    square_frame(3)
