def solution(n):
    answer = numerial(n)
    return answer

def numerial(qr):
    NUM = '124'
    q, r = divmod(qr, 3)
    if r == 0:
        return numerial(q-1) + '4' if q-1 > 2 else str(q-1) + '4' if q-1 > 0 else '4'
    else:
        return numerial(q) + str(r) if q-1 > 2 else (str(NUM[q - 1]) + str(r) if q-1>-1 else str(r))

def solution2(n):
    NUM = ['1','2','4']
    answer = ''
    while n > 0:
        n -= 1
        answer = NUM[n%3] + answer
        n //= 3
    return answer

num = 16
print(solution2(num))