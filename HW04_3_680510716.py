#!/usr/bin/env python3
# ชื่อ นามสกุล (ชื่อเล่น)
# 6XXXXXXXX
# HW04_3
# 204111 Sec 00B

def divide_plot(x: int, y: int, z: int, start: str) -> str:
    ops = ''
    # แนะนำให้ใช้ฟังก์ชัน concat_ops() เพื่อนำสองชุดคำสั่งมาต่อกันแล้วคั่นด้วย comma
    # ไม่ควรทำ string concatenate แล้วบันทึกลงตัวแปรเดิม เช่น
    # ops += 'RIGHT' หรือ ops = ops + 'RIGHT' (ศึกษาได้จาก slide เรื่อง String)

    start_pos: str = str.lower(start)
    common: int = (x + y + z) // 3

    x_adjustment: int = abs(common - x)
    y_adjustment: int = abs(common - y)
    z_adjustment: int = abs(common - z)

    if start_pos == "a":
        if x_adjustment > 0 and y_adjustment < 0 and z_adjustment < 0:
            return concat_ops(f"PUSH_RIGHT {str(x_adjustment)}", "")
        elif x_adjustment > 0 and y_adjustment > 0:
            return concat_ops(concat_ops(f"PUSH_RIGHT {str(x_adjustment)}", "RIGHT"), f"PUSH_RIGHT {str(y_adjustment)}")
        elif x_adjustment > 0 and z_adjustment > 0:
            return concat_ops(concat_ops(f"PUSH_RIGHT {str(x_adjustment)}", "RIGHT"), f"PUSH_RIGHT {str(z_adjustment)}")
        else:
            return concat_ops("RIGHT")
        
        if z_adjustment > 0:
            print("HI")
            sub_ops_3 = concat_ops(concat_ops("RIGHT", "RIGHT"), f"PUSH_LEFT {str(z_adjustment)}")

    # ไม่แก้บรรทัดนี้
    return ops.strip(', ')


def concat_ops(op1: str, op2: str) -> str:
    """
    ต่อข้อความคำสั่งสองชุดเข้าด้วยกันโดยเว้นด้วยเครื่องหมายคอมมาและเว้นวรรค

    ฟังก์ชันนี้จะรับข้อความคำสั่งสองชุด (เช่น "LEFT", "PUSH_RIGHT 3") แล้วรวมเข้าด้วยกัน
    ด้วยเครื่องหมายคอมมาและช่องว่าง (", ") อย่างถูกต้อง ถ้าชุดใดชุดหนึ่งว่างเปล่า
    จะคืนค่าอีกชุดหนึ่งแทนโดยไม่เติมคอมมา หากทั้งสองชุดว่างเปล่า จะคืนค่าว่าง

    พารามิเตอร์:
        op1 (str): ข้อความคำสั่งชุดแรก
        op2 (str): ข้อความคำสั่งชุดที่สอง

    คืนค่า:
        str: ข้อความคำสั่งที่ถูกรวมเข้าด้วยกันอย่างถูกต้อง

    ตัวอย่าง:
        >>> concat_ops("LEFT", "PUSH_RIGHT 3")
        'LEFT, PUSH_RIGHT 3'
        >>> concat_ops("", "RIGHT")
        'RIGHT'
        >>> concat_ops("LEFT", "")
        'LEFT'
        >>> concat_ops("", "")
        ''
    """
    if not op1 and not op2:
        return ''
    if not op1:
        return op2
    if not op2:
        return op1

    return ', '.join([op1, op2])



if __name__ == '__main__':
    from HW04_3_helper import simulate_operations
    ops = divide_plot(5, 8, 2, 'A')
    result = simulate_operations(2, 5, 8, 'A', ops)
    print(ops)
    print(result)
