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
def evolve(amount: int, candy: int, candy_per_evolution: int) -> tuple[int, int, int] | None:
    if candy < candy_per_evolution: return

    evolution_counts: int = min(amount, candy // (candy_per_evolution-amount))
    total_candy_required: int = candy_per_evolution * evolution_counts

    reward_candy: int = evolution_counts
    reward_exp: int = evolution_counts * 1000

    return reward_exp, reward_candy, total_candy_required


def calculate_reward(amount: int, candy: int) -> tuple[int, int]:
    EVOLUTION_COST: int = 12

    current_candy: int = candy
    current_exp: int = 0

    reward_exp, reward_candy, required_candy = evolve(amount, current_candy, EVOLUTION_COST) or (0, 0, 0)
    current_exp += reward_exp
    current_candy -= required_candy
    current_candy += reward_candy

    return current_exp, current_candy


def calculate_exp(p: int, c: int) -> int:
    if (p <= 0) or (c < 12): return 0 
    
    remaining_amount: int = 0
    if p: remaining_amount = p

    current_candy: int = 0
    current_exp: int = 0
    if c: current_candy = c
    
    current_exp, current_candy = calculate_reward(p, c)

    if (remaining_amount > 0) and (current_candy == 11):
        remaining_amount -= 1
        current_candy += 1

        retured_exp, retured_candy = calculate_reward(remaining_amount, current_candy)
        current_candy += retured_candy
        current_exp += retured_exp

    return current_exp


# MAIN
if __name__ == "__main__":
    test_calculate_exp()
