# for else 문은 for 문이 break 없이 끝나면 수행하는 것.

def nsys(number, base):
    notation = "0123456789ABCDEF"
    q,r = divmod(number,base)
    num = notation[r]
    return nsys(q,base) + num if q else num

a = [1]
print(a[-1])