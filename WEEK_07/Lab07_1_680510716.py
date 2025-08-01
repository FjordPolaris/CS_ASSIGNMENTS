#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab07_1
# 204111 Sec 003

DEBUG = False


def trekking_seq(student_ids: list[str]) -> list[str]:
    
    _year: str = str(sorted(student_ids[2:4], reverse=True))
    result: list[str] = sorted(student_ids, key=lambda x: (x[2:4], _year, x[4:]))
    #print(result)

    return result


if __name__ == '__main__':
    assert trekking_seq(['672110355', '671510555']) \
        == ['671510555', '672110355']

    assert trekking_seq(['610510623', '620510113']) \
        == ['620510113', '610510623']

    assert trekking_seq(['661610623', '661610713']) \
        == ['661610623', '661610713']

    assert trekking_seq(['610510623', '672110555', '620510113', '620510112']) \
        == ['620510112', '620510113', '610510623', '672110555', ]

    print('ALL OK')
