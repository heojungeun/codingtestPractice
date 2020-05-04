def solution(n, t, m, p):
    answer, total = '', ''
    tmp = [i for i in range(0,t*m)]
    for x in tmp:
        res = nsys(x,n)
        total += res
        if len(total) >= t*m:
            break
    tmp = [p+m*(i-1) for i in range(1,t+1)]
    for x in tmp:
        answer += total[x-1]
    return answer

def nsys(number, base):
    notation = "0123456789ABCDEF"
    q,r = divmod(number,base)
    num = notation[r]
    return nsys(q,base) + num if q else num

print(solution(16,16,2,1))
