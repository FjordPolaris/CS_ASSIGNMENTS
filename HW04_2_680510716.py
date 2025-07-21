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
    assert calculate_exp(10, 100) == 10000

    assert calculate_exp(0, 12) == 0
    assert calculate_exp(12, 0) == 0
    assert calculate_exp(30, -12) == 1000
    print(":>")


# FUNCTIONS

def calculate_exp(p: int, c: int) -> int:
    if (p < 1) or (p + c < 13): return 0

    DEFAULT_EVOLUTION_COST: int = 12
    DEFAULT_REWARD_EXP: int = 1000

    amount: int = int(p) or 0
    candy: int = int(c) or 0
    exp: int = 0
   
    if (amount) and (candy) > 0:
        max_evolutions: int = min(
            amount,
            candy // (DEFAULT_EVOLUTION_COST -2)      
        )
        exp += abs(DEFAULT_REWARD_EXP * max_evolutions)
    else:
        if (candy < 0):
            remaining_amount: int = amount + candy  # CANDY = 0
            remaining_amount -= (DEFAULT_EVOLUTION_COST)
            candy = (candy + (amount-1))
            if remaining_amount < 0: return 0
            print(remaining_amount, candy// 11)
            
            max_evolutions: int = min(
                remaining_amount,
                candy // (DEFAULT_EVOLUTION_COST-1)
            )
            exp += abs(DEFAULT_REWARD_EXP * max_evolutions)

    if DEBUG:
        print("EXP:", exp)
        print(" ")

    return exp


# MAIN
if __name__ == "__main__":
    test_calculate_exp()
