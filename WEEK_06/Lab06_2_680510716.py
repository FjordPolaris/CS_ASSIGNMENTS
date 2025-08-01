#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab06_2
# 204111 Sec 003


def test_dest_rotate_list():
    list_a: list[int] = [1, 2, 3, 4]
    
    dest_rotate_list(list_a, 1)
    dest_rotate_list(list_a, 2)
    dest_rotate_list(list_a, 105)
    dest_rotate_list(list_a, -1)
    dest_rotate_list(list_a, -2)


def dest_rotate_list(list_a: list[int], n: int):
    if not n:
        print("output =", list_a),
    
    times: int = n % len(list_a)
    list_a[:] = list_a[-times:] + list_a[:-times]
    
    print("output =", list_a)
    del times
    #return list_alpha


if __name__ == "__main__":
    test_dest_rotate_list()
