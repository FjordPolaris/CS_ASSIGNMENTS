#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW04_2
# 204111 Sec 003

def test_calculate_exp() -> None:
    assert calculate_exp(1, 12) == 1000
    assert calculate_exp(2, 12) == 1000
    assert calculate_exp(2, 22) == 2000
    assert calculate_exp(1, 55) == 1000
    assert calculate_exp(3, 33) == 3000
    assert calculate_exp(10, 100) == 10000
    assert calculate_exp(1, 0) == 0
    assert calculate_exp(-1, -1) == 0
    print(":>")


# FUNCTIONS
def evolve(amount: int, candy: int, required_candy: int) -> tuple[int, int, int] | None:
    if candy < required_candy: return
    
    evolution_counts: int = min(amount, candy // (required_candy - amount))
    total_candy_required: int = required_candy * evolution_counts

    reward_candy: int = evolution_counts
    reward_exp: int = evolution_counts * 1000

    return reward_exp, reward_candy, total_candy_required


def calculate_exp(p: int, c: int) -> int:
    if (p <= 0) or (c < 12): return 0 

    REQUIRED_CANDY: int = 12
    
    current_exp: int = 0
    current_candy: int = 0

    if c: current_candy = c

    reward_exp, reward_candy, required_candy = evolve(p, current_candy, REQUIRED_CANDY) or (0, 0, 0)
    if reward_exp > 0:
        current_exp += reward_exp
        current_candy -= required_candy
        current_candy += reward_candy

    return current_exp


# MAIN
if __name__ == "__main__":
    test_calculate_exp()
