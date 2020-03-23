def is_num(num):
    try:
        num = float(num)
        return True
    except:
        return False

print(is_num(5.6))