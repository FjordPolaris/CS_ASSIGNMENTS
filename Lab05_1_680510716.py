#!/usr/bin/env python3
# ธีรวิทย์ คำลือ (แทน)
# 680510716
# Lab05_1
# 204111 Sec 003


def test_is_valid_license() -> None:
    assert is_valid_license("9AB8954") == True
    assert is_valid_license("9999") == False
    assert is_valid_license("CD700") == True
    assert is_valid_license("99D1234") == False
    assert is_valid_license("9ab8954") == False
    assert is_valid_license("2Ab343") == False
    assert is_valid_license("a") == False
    assert is_valid_license("") == False
    print(":>")


def is_valid_license(license_str: str) -> bool:
    _license: str = license_str.strip()

    # Preliminary validations
    if (len(_license) > 7 or 
        len(_license) < 1 or 
        str.isdigit(_license) or 
        not str.isupper(_license)): 
        return False

    if str.isdigit(_license[0]) and str.isalpha(_license[1:3]) and str.isupper(_license):
        if len(_license) > 3 and str.isdigit(_license[3:]):
                return True
    elif str.isalpha(_license[0:2]) and str.isupper(_license):
        if str.isdigit(_license[2:]):
            return True
    else:
        return False

    return False
    

if __name__ == "__main__":
    test_is_valid_license()
