#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# HW05_2
# 204111 Sec 003


def test_transform_name() -> None:
    assert transform_name("elizabeth andre") == "Andre.Elizabeth"
    assert transform_name("    lena Eive") == "Eive.Lena"
    assert transform_name("Toyoakini shidai") == "Shidai.Toyoakin"
    assert transform_name("lala Divesdentinala") == "Divesdenti.Lala"
    assert transform_name("Yoshimasa Ohmotoyoshi") == "Ohmotoyos.Yoshi"
    assert transform_name("TSe micheLangelo") == "Michelangel.Tse"
    assert transform_name("Hello Wor1d") == None
    print(":>")


def transform_name(name: str) -> str | None:
    import string

    if name.isdigit(): return

    full_name: str = string.capwords(str.strip(name))
    _lastname, _firstname = str.split(full_name)
    
    if not _lastname.isalpha() or not _firstname.isalpha(): return

    firstname: str = ""
    lastname: str = ""
    username: str = ""

    length: int = 14 - (len(_firstname) + len(_lastname))
    
    # BELOW PREDEFINED LIMIT - NO NEED TO WORRY ABOUT LENGTH
    if length >= 0:
        firstname = _firstname
        lastname = _lastname
    
    # EXCEEDS PREDEFINED LIMIT
    if length < 0:
        if len(_firstname) > 9 and len(_lastname) > 5:
            firstname = _firstname[0:9]
            lastname = _lastname[0:5]

        elif len(_firstname) > 9 and len(_lastname) < 5:
            length_diff: int = 14 - len(_lastname)
            firstname = _firstname[0:length_diff]
            lastname = _lastname[0:5]

        elif len(_firstname) < 9 and len(_lastname) > 5:
            length_diff: int = 14 - len(_firstname)
            firstname = _firstname[0:9]
            lastname = _lastname[0:length_diff]

    username = f"{firstname}.{lastname}"

    if len(username) > 15:
        print("**** ERROR ****")

    #print(username)

    return username


if __name__ == "__main__":
    test_transform_name()
