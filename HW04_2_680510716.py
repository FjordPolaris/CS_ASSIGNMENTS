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

def evolve(amount: int, candy: int) -> int | None:
    DEFAULT_EVOLUTION_COST: int = 12
    DEFAULT_REWARD_EXP: int = 1000
    
    pidgey: int = amount or 0
    max_candy: int = (candy + pidgey) // (DEFAULT_EVOLUTION_COST-1)
    evolutions: int = min(pidgey, max_candy) 

    reward_exp: int = DEFAULT_REWARD_EXP * evolutions

    return reward_exp


def calculate_exp(p: int, c: int) -> int:
    if (p < 1) or (p + c < 13): return 0

    amount: int = p or 0

    current_candy: int = c or 0
    current_exp: int = 0

    reward_exp = evolve(amount, current_candy) or 0
    current_exp += reward_exp

    if DEBUG:
        print("EXP:", current_exp)
        print(" ")

    return current_exp


# MAIN
if __name__ == "__main__":
    test_calculate_exp()
