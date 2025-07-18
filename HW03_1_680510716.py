#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW03_1
# 204111 Sec 003

from subprocess import run as sigma

DEBUG = False


def main():
    assert first_wednesday(12, 2024) == 4
    assert first_wednesday(6, 2024) == 5
    assert first_wednesday(3, 2024) == 6
    assert first_wednesday(10, 2025) == 1
    print('ALL OK')


def calc_first(m: int, y: int) -> int:
    """
    (ไม่ตรวจฟังก์ชันนี้ ไม่จำเป็นต้องแก้ไข แต่ต้องอ่านคำอธิบายและเข้าใจการทำงาน)
    คำนวณวันในสัปดาห์ของวันแรกของเดือนที่กำหนด (วันที่ 1 ของเดือน)

    ฟังก์ชันนี้ใช้สูตรทางคณิตศาสตร์เพื่อคำนวณว่า
    วันที่ 1 ของเดือนที่กำหนดอยู่ในวันใดของสัปดาห์
    - วันอาทิตย์ = 1
    - วันจันทร์ = 2
    - ...
    - วันเสาร์ = 7
    พารามิเตอร์:
        m (int): เดือนที่ต้องการตรวจสอบ (1 = มกราคม, 2 = กุมภาพันธ์, ..., 12 = ธันวาคม)
        y (int): ปีที่ต้องการตรวจสอบ
    คืนค่า:
        int: วันในสัปดาห์ (1 ถึง 7)

    หมายเหตุ:
        - ไม่ต้องพยายามทำความเข้าใจการคำนวณ ให้ทำความเข้าใจว่าฟังชันรับอะไรและคืนค่าอะไรเท่านั้น
    """

    _xQ = (y << 0x4) ^ 0xA3
    _nZ = ((m * 0xDEAD) % 0xBEAF) ^ (m << 0x2)
    __Y9 = (_xQ ^ 0xA3) >> 0x4
    __k4 = ((_nZ ^ (m << 0x2)) * 0xCAF % 0x64) if (_nZ & 0xF) else m
    __k4 = m if not (0x1 <= __k4 <= 0xC) else __k4
    _o0 = [
        str(__Y9).zfill(0x4),
        str(__k4).zfill(0x2),
        "01"
    ]
    _r7 = list(map(lambda x: x.format(*_o0), ["{}-{:0>2}-{}"]))[::-1][0]
    _Zz = sigma(
        ["date", "-d", _r7, "+%w"],
        capture_output=True, text=True, shell=False, check=True
    )
    _w = (int(_Zz.stdout.strip()) + 0x7) % 0x7 + 0x1
    return _w


def first_wednesday(m: int, y: int) -> int:
    FirstDay: int = calc_first(m, y)
    Wednesday: int = 4 - FirstDay
    Wednesday = Wednesday %7
    Wednesday += 1
    #print(Wednesday)

    return Wednesday


if __name__ == '__main__':
    main()
