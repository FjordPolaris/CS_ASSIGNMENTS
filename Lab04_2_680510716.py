#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab04_2
# 204111 Sec 003

def main() -> None:
    assert my_min_mid_max(1, 2, 3) == '1 2 3'
    assert my_min_mid_max(1, 3, 2) == '1 2 3'
    assert my_min_mid_max(2, 1, 3) == '1 2 3'
    assert my_min_mid_max(2, 3, 1) == '1 2 3'
    assert my_min_mid_max(3, 1, 2) == '1 2 3'
    assert my_min_mid_max(3, 2, 1) == '1 2 3'
    assert my_min_mid_max(1, 1, 1) == '1 1 1'
    print(":>")


def less_than(x: int, y: int) -> bool:
    return x < y


def my_min_mid_max(a: int, b: int, c: int) -> str:
    min_ = mid = max_ = -1
   
    # Preliminary
    if less_than(a, b):
        min_ = a
        max_ = b
    else:
        min_ = b
        max_ = a
    
    # Correcting max_ and assigning mid
    if less_than(c, min_):
        # According to the condition, since c < min_, therefore the previous value assigned is greater
        mid = min_ 
        min_ = c

    elif less_than(c, max_):
        # Due to the failure of the previous condition :< | This condition will be evaluated
        # From the previous condition, c is clearly > min_ 
        # From this condition, c is < max_
        mid = c

    else:
        mid = max_
        max_ = c

    #print(min_, mid, max_, "|", a, b, c)
    return f'{min_} {mid} {max_}'


if __name__ == '__main__':
    main()
