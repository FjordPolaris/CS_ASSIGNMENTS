#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW04_1
# 204111 Sec 003


# INITIALISATION

TIME_CONVERSION_RATE: int = 12
DEBUG: bool = False

# FUNCTIONS

def test_minute_diff() -> None:
    assert minute_diff(8, 23, "AM", 8, 24, "AM") == 1
    assert minute_diff(8, 23, "AM", 1, 24, "PM") == 301
    assert minute_diff(1, 24, "PM", 8, 23, "AM") == 301
    assert minute_diff(11, 59, "AM", 12, 00, "PM") == 1
    print(":>")


def calculate_total_minute(hour: int, minute: int, isPM: bool = False) -> int:
    total_minute: int = 0

    _hour: int = hour %12
    minute = minute % 60

    if minute > 59:
        _hour = hour + (minute // 60)
        minute = minute % 60

    if isPM:
        total_minute = (_hour + TIME_CONVERSION_RATE) *60
        total_minute += minute
    else:
        total_minute = (_hour *60) + minute

    return total_minute


def convert_time(h1: int, m1: int, p1: str, 
                 h2: int, m2: int, p2: str):

    suffix_1: str = str.lower(p1)
    suffix_2: str = str.lower(p2)

    if (suffix_1 == "am"):
        time_1 = calculate_total_minute(h1, m1)
    else:
        time_1 = calculate_total_minute(h1, m1, True)

    # ===== TIME_2 =====

    if (suffix_2 == "am"):
        time_2 = calculate_total_minute(h2, m2)
    else:
        time_2 = calculate_total_minute(h2, m2, True)

    # **** DEBUG ****
    if DEBUG:
        print(time_1, time_2)

    return time_1, time_2


def minute_diff(h1: int, m1: int, p1: str, 
                h2: int, m2: int, p2: str) -> int:
    
    time_1, time_2 = convert_time(
        h1, m1, p1,
        h2, m2, p2
    )

    minute_difference: int = 0
   
    if time_1 and time_2:
        minute_difference = abs(time_2 - time_1)

    # **** DEBUG **** #
    if DEBUG:
        print(minute_difference, "Diff")

    return minute_difference


# MAIN

if __name__ == "__main__":
    test_minute_diff()
