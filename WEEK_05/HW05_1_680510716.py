#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW05_1
# 204111 Sec 003


def test_replace_in_range() -> None:
    assert replace_in_range("Happy birthday", 3, 10, "p", "e") == "Hapey birthday"
    assert replace_in_range("Happy birthday", 3, 10, "z", "e") == "Happy birthday"
    assert replace_in_range("Happy birthday", 0, 14, "h", "w") == "Wappy birtwday"
    assert replace_in_range("Happy birthday", 3, 10, "y", "i") == "Happi birthday"
    assert replace_in_range("Happy birthday", -9, 14, "y", "i") == "Happy birthdai"
    assert replace_in_range("Happy birthday", 3, 14, "y", "i") == "Happi birthdai"
    assert replace_in_range("Happy birthday", -100, 100, "y", "i") == "Happi birthdai"
    print(":>")


def replace_in_range(text: str, start: int, stop: int, old_c: str, new_c: str) -> str:

    raw_text: str = text.strip()
    before_text: str = raw_text[:start]
    ranged_text: str = raw_text[start:stop]
    after_text: str = raw_text[stop:]

    # Find the uppercase of the old character then replaced it with the new character with uppercase
    # Likewise for the lowercase
    replaced_text: str = ranged_text.replace(old_c.upper(), new_c.upper()).replace(old_c.lower(), new_c.lower())
    final_text: str = before_text + replaced_text + after_text

    #print(final_text, replaced_text)

    return final_text


if __name__ == "__main__":
    test_replace_in_range()
