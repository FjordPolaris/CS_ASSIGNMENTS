#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW05_3
# 204111 Sec 003

from datetime import timedelta, timezone

DEBUG = False


def convert_time(delta: timedelta) -> tuple[int, int, int, int]:
    total_seconds: int = int(delta.total_seconds())
    total_seconds = abs(total_seconds)

    _minutes: int = total_seconds // 60
    _hours: int = _minutes // 60

    days: int = _hours // 24
    hours: int = _hours % 24
    minutes: int = _minutes % 60
    seconds: int = total_seconds % 60

    return days, hours, minutes, seconds


def calculate_timezone(tz: str) -> timezone:
    time_zone_offset: int = 0
    
    # Support UTC+7 or UTC+12 or UTC+0.25
    if tz.startswith("UTC+"):
        time_zone_offset = int(tz[4:])
    elif tz.startswith("UTC-"):
        time_zone_offset = int(tz[4:]) * -1
    else:
        return timezone.utc

    # As timedelta(hours) argument automatically convert hours' decimal into proper minutes
    # There's no need to store digits after decimal and pass minutes argument separately
    re_timezone: timezone = timezone(timedelta(hours = time_zone_offset))
    return re_timezone


def display_post_time(post_time: str, post_tz: str, 
                      view_time: str, view_tz: str) -> str:
    from datetime import datetime

    # Preliminary - converting string into datetime object 
    post_datetime: datetime = datetime.strptime(post_time, "%Y-%m-%d %H:%M:%S")
    view_datetime: datetime = datetime.strptime(view_time, "%Y-%m-%d %H:%M:%S")

    # Initialise Timezone
    post_timezone: timezone = calculate_timezone(post_tz)
    view_timezone: timezone = calculate_timezone(view_tz)

    # Apply Timezone
    post_datetime = post_datetime.replace(tzinfo = post_timezone)
    view_datetime = view_datetime.replace(tzinfo = view_timezone)

    # UTC+0 Standardisation
    neutralised_postdate: datetime = post_datetime.astimezone(timezone.utc)
    neutralised_viewdate: datetime = view_datetime.astimezone(timezone.utc)

    # Apply View's Timezone to the Post
    post_in_view_tz: datetime = post_datetime.astimezone(view_timezone)

    delta: timedelta = abs(neutralised_postdate - neutralised_viewdate)
    days, hours, minutes, _ = convert_time(delta)

    #print(hours, minutes, seconds)

    # Main Logic :<
    if (not hours and minutes and not days):
        return f"{minutes}m"
    elif (hours and hours < 24 and not days):
        return f"{hours}h"
    elif (days and days < 7):
        weekday: str = post_in_view_tz.strftime("%A")
        return weekday
    elif (post_in_view_tz.year == view_datetime.year):
        if hours or minutes or days:
            return post_in_view_tz.strftime("%b %d")
    elif (post_in_view_tz.year != view_datetime.year):
        return post_in_view_tz.strftime("%b %d, %Y")

    return "just now"


def test_display_post_time():
    assert display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-15 10:30:45', 'UTC') == 'just now'
    assert display_post_time('2023-05-15 10:30:00', 'UTC', '2023-05-15 11:15:00', 'UTC') == '45m'
    assert display_post_time('2023-05-15 10:30:00', 'UTC', '2023-05-15 15:45:00', 'UTC') == '5h'
    assert display_post_time('2023-05-15 10:30:00', 'UTC', '2023-05-19 15:45:00', 'UTC') == 'Monday'
    assert display_post_time('2023-05-15 03:30:00', 'UTC+7', '2023-12-19 15:45:00', 'UTC+3') == 'May 14'
    assert display_post_time('2023-05-15 03:30:00', 'UTC+7', '2024-12-19 15:45:00', 'UTC+4') == 'May 15, 2023'
    assert display_post_time('2023-05-15 10:30:00', 'UTC', '2023-05-15 18:15:00', 'UTC+7') == '45m'
    assert display_post_time('2023-09-01 12:00:00', 'UTC-10', '2023-09-05 00:00:00', 'UTC+2') == 'Saturday'
    assert display_post_time('2023-01-01 00:00:01', 'UTC+14', '2023-12-31 09:59:59', 'UTC') == 'Dec 31, 2022'
    print('ALL OK')


if __name__ == '__main__':
    test_display_post_time()
