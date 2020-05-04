def solution(n):
    cntone = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == cntone:
            break
    return n
num = 1
print(solution(num))