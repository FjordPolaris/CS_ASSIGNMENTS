#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW06_1
# 204111 Sec 003


def test_same_letters():
    assert same_letters("your reader", "You are ready.") == True
    assert same_letters("WelCome", "weldoNe") == False
    assert same_letters("annA bell", "Ballean") == True
    assert same_letters("4i2r3o{l3n}6mtG7o8d9 ", "GooLm#tdM4498orn23ing") == True
    assert same_letters("reST334RoOm344home56 ", "256889HBbro455om55s") == False
    assert same_letters("hi  =       ====", "hi=") == True
    print(":>")


def same_letters(str1: str, str2: str) -> bool:
    msg_1: str = ''.join(filter(str.isalpha, str1.lower().strip()))
    msg_2: str = ''.join(filter(str.isalpha, str2.lower().strip()))
    #print(msg_1, msg_2)

    list_msg_1: list = list(map(lambda x: x if x not in msg_2 else None, msg_1))
    list_msg_2: list = list(map(lambda y: y if y not in msg_1 else None, msg_2))
    list_msg_1 = list(filter(lambda z: z is not None, list_msg_1))
    list_msg_2 = list(filter(lambda m: m is not None, list_msg_2))
    #print(list_msg_1, list_msg_2)

    if list_msg_1 == list_msg_2:
        return True
    
    return False


if __name__ == "__main__":
    test_same_letters()
