#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW05_3
# 204111 Sec 003

from typing import Tuple
from datetime import timedelta, timezone

DEBUG = False


def convert_time(delta: timedelta) -> Tuple[int, int, int]:
    total_seconds = int(delta.total_seconds())
    total_seconds = abs(total_seconds)

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return hours, minutes, seconds


def calculate_timezone(tz: str) -> timezone:
    offset_hour: int = 0
    re_timezone: timezone = timezone.utc
    
    if tz.startswith("UTC+"):
        offset_hour = int(tz[4:5])
    elif tz.startswith("UTC-"):
        offset_hour = int(tz[4:5]) * -1

    re_timezone = timezone(timedelta(hours = offset_hour))
    return re_timezone


def display_post_time(post_time: str, post_tz: str, 
                      view_time: str, view_tz: str) -> str:
    from datetime import datetime, timezone

    post_datetime: datetime = datetime.strptime(post_time, "%Y-%m-%d %H:%M:%S")
    view_datetime: datetime = datetime.strptime(view_time, "%Y-%m-%d %H:%M:%S")

    post_timezone: timezone = calculate_timezone(post_tz)
    view_timezone: timezone = calculate_timezone(view_tz)

    post_datetime = post_datetime.replace(tzinfo=post_timezone)
    view_datetime = view_datetime.replace(tzinfo=view_timezone)

    delta: timedelta = view_datetime.astimezone(timezone.utc) - post_datetime.astimezone(timezone.utc)
    hours, minutes, seconds = convert_time(delta) or (0, 0, 0)

    #print(hours, minutes, seconds)

    if not hours and minutes:
        return f"{minutes}m"
    elif hours and hours < 24:
        return f"{hours}h"

    return "just now"


def test_display_post_time():
    assert display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-15 10:30:45', 'UTC') == 'just now'
    assert display_post_time('2023-05-15 10:30:00', 'UTC', '2023-05-15 11:15:00', 'UTC') == '45m'
    assert display_post_time('2023-05-15 10:30:00', 'UTC', '2023-05-15 15:45:00', 'UTC') == '5h'
    print('ALL OK')


if __name__ == '__main__':
    test_display_post_time()
