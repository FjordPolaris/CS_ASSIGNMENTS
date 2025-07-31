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

    assert calculate_exp(0, 12) == 0
    assert calculate_exp(12, 0) == 0

    assert calculate_exp(36, -12) == 2000
    print(":>")


# FUNCTIONS

def calculate_exp(p: int, c: int) -> int:
    if (p < 1) or (p + c < 13): return 0
    
    DEFAULT_EVOLUTION_COST: int = 11
    DEFAULT_REWARD_EXP: int = 1000

    amount: int = int(p) or 0
    candy: int = int(c) or 0
    exp: int = 0

    if amount + candy > 12:
        max_evolutions: int = ((amount + candy) - 2) // DEFAULT_EVOLUTION_COST
        exp = min(
            (max_evolutions) * DEFAULT_REWARD_EXP,
            amount * DEFAULT_REWARD_EXP
        )

    if DEBUG:
        print("EXP:", exp)
        print(" ")

    return exp


# MAIN
if __name__ == "__main__":
    test_calculate_exp()
