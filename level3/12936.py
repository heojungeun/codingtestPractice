def solution(n, k):
    from math import factorial
    answer = []
    tmp = [i for i in range(1,n+1)]
    # tmp = list(range(1,n+1))
    while n>0:
        n -= 1
        q,r = divmod(k,factorial(n))
        if not r: q -= 1
        answer.append(tmp[q])
        tmp.remove(tmp[q])
        k = r
    return answer

num =3
k_ = 5
print(solution(num,k_))