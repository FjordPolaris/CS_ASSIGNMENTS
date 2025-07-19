#!/usr/bin/env python3
# @Author: kk
# @Date:   2025-06-15 08:03:41

def simulate_operations(x, y, z, start, operations_str, last_pos=False):
    sections = [x, y, z]
    assert sum(sections) % 3 == 0

    operations_str = operations_str.strip()
    if operations_str.endswith(','):
        operations_str = operations_str[:-1]

    pos = {'A': 0, 'B': 1, 'C': 2}[start]
    operations = [op.strip() for op in operations_str.split(',') if op.strip()]

    for op in operations:
        if op == "LEFT":
            if pos == 0:
                return f"{sections[0]} {sections[1]} {sections[2]} {'ABC'[pos]}\nERROR"
            pos -= 1
        elif op == "RIGHT":
            if pos == 2:
                return f"{sections[0]} {sections[1]} {sections[2]} {'ABC'[pos]}\nERROR"
            pos += 1
        elif op.startswith("PUSH_LEFT "):
            try:
                amount = int(op.split()[1])
                assert amount > 0
            except:
                return f"{sections[0]} {sections[1]} {sections[2]} {'ABC'[pos]}\nERROR"
            if pos not in (1, 2):
                return f"{sections[0]} {sections[1]} {sections[2]} {'ABC'[pos]}\nERROR"
            left = pos - 1
            if sections[left] <= amount:
                return f"{sections[0]} {sections[1]} {sections[2]} {'ABC'[pos]}\nERROR"
            sections[left] -= amount
            sections[pos] += amount
        elif op.startswith("PUSH_RIGHT "):
            try:
                amount = int(op.split()[1])
                assert amount > 0
            except:
                return f"{sections[0]} {sections[1]} {sections[2]} {'ABC'[pos]}\nERROR"
            if pos not in (0, 1):
                return f"{sections[0]} {sections[1]} {sections[2]} {'ABC'[pos]}\nERROR"
            right = pos + 1
            if sections[right] <= amount:
                return f"{sections[0]} {sections[1]} {sections[2]} {'ABC'[pos]}\nERROR"
            sections[right] -= amount
            sections[pos] += amount
        else:
            return f"{sections[0]} {sections[1]} {sections[2]} {'ABC'[pos]}\nERROR"

    if last_pos:
        return f"{sections[0]} {sections[1]} {sections[2]} {'ABC'[pos]}"
    else:
        return f"{sections[0]} {sections[1]} {sections[2]}"