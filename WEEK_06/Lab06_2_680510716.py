#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab06_2
# 204111 Sec 003


def test_dest_rotate_list():
    list_a: list[int] = [1, 2, 3, 4]
    
    assert dest_rotate_list(list_a, 1) == [4, 1, 2, 3]
    assert dest_rotate_list(list_a, 105) == [4, 1, 2, 3]
    assert dest_rotate_list(list_a, -1) == [2, 3, 4, 1]
    del list_a
    print(":>")


def dest_rotate_list(list_a: list[int], n: int):
    if not n:
        print("output = ", list_a)

    list_alpha: list[int] = list_a.copy()
    times: int = n % len(list_alpha)

    list_alpha = list_alpha[-times:] + list_alpha[:-times]
    
    print("output = ", list_alpha)
    #return list_alpha
    del list_alpha, times


if __name__ == "__main__":
#test_dest_rotate_list()
