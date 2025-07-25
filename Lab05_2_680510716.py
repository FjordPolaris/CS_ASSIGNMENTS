#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab05_2
# 204111 Sec 003


def test_palindrome_without() -> None:
    assert palindrome_without("Banana", "b") == True
    assert palindrome_without("Swap of paws", "f") == True
    assert palindrome_without("T", "t") == False
    print(":>")

def palindrome_without(text: str, c: str) -> bool:
    p_text: str = str.lower(text)
    replacement: str = str.lower(c)

    p_text = p_text.replace(replacement, "")

    if (p_text == p_text[::-1]) and (len(p_text) > 0):
        return True

    return False

if __name__ == "__main__":
    test_palindrome_without()
