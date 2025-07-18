#!/usr/bin/env python3
# ธีรวิทย์ คำลืลือ (แทน)
# 680510716
# Lab02_2
# 204111 Sec 003

import math

def Convert(Time_Millisec: int) -> None:
    Sec: int = Time_Millisec // 1000
    Minute: int = Sec // 60
    Hour: int = Minute // 60

    Day: int = Hour // 24
    remainingHours: int = Hour % 24
    remainingMinutes: int = Minute % 60
    remainingSeconds: int = Sec % 60
    remainingMillisec: int = Time_Millisec % 1000

    print(f"{Day} day(s), {remainingHours} hour(s), {remainingMinutes} minute(s), {remainingSeconds} second(s), {remainingMillisec} millisec(s)")

inputTime: int = int(input("Input milliseconds: "))
Convert(inputTime)
