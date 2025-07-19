#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW04_2
# 204111 Sec 003

DEBUG: bool = False


def test_calculate_exp() -> None:
    assert calculate_exp(1, 12) == 1000
    assert calculate_exp(2, 12) == 1000
    assert calculate_exp(2, 22) == 2000
    assert calculate_exp(1, 55) == 1000
    assert calculate_exp(3, 33) == 3000
    assert calculate_exp(1, 0) == 0
    assert calculate_exp(-1, -1) == 0
    print(":>")


# FUNCTIONS

def calculate_exp(p: int, c: int) -> int:
    if (p < 1) or (p + c < 13): return 0

    DEFAULT_EVOLUTION_COST: int = 12
    DEFAULT_REWARD_EXP: int = 1000

    amount: int = p or 0
    candy: int = c or 0
    exp: int = 0

    max_candy: int = (candy + amount) // (DEFAULT_EVOLUTION_COST -1)
    evolutions: int = min(amount, max_candy)
    exp = DEFAULT_REWARD_EXP * evolutions

    if DEBUG:
        print("EXP:", exp)
        print(" ")

    return exp


# MAIN
if __name__ == "__main__":
    test_calculate_exp()
