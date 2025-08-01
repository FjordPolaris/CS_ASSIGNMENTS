#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab06_2
# 204111 Sec 003


def dest_rotate_list(list_a: list[int], n: int):
    times: int = n % len(list_a)
    list_a[:] = list_a[-times:] + list_a[:-times]
    
    del times
    #return list_alpha


if __name__ == "__main__":
    list_a = [1, 2, 3, 4]
    dest_rotate_list(list_a, 1)
    print('output =', list_a)

    list_a = [1, 2, 3, 4]
    dest_rotate_list(list_a, 105)
    print('output =', list_a)
