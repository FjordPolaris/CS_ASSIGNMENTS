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
    assert is_valid_license("") == False
    assert is_valid_license("99999999") == False
    assert is_valid_license("9aaaaa") == False
    assert is_valid_license("1AA") == True 
    assert is_valid_license("a") == False
    print(":>")


def is_valid_license(license_str: str) -> bool:
    # Preliminary validations
    if (len(license_str) > 7 or 
        len(license_str) < 1 or 
        str.isdigit(license_str) or 
        str.islower(license_str)): 
        return False
    
    if str.isdigit(license_str[1]) == False and len(license_str) > 1:
        # Alphabet validations
        if str.isdigit(license_str[0]):
            if not str.isdigit(license_str[1:3]) and not len(license_str) > 3:
                return True
            elif not str.isdigit(license_str[1:3]) and len(license_str) > 3 and str.isdigit(license_str[3:]):
                return True
        else:
            if not str.isdigit(license_str[0:2]) and not len(license_str) > 2:
                return True
            if len(license_str) > 2 and str.isdigit(license_str[2:]):
                return True

    elif str.isdigit(license_str[0:]):
        return True
    else:
        return False

    return False


if __name__ == "__main__":
    test_is_valid_license()
