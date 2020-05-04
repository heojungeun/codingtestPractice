from itertools import product
def solution(n, m, k):
    answer = 0
    maxk = m//2
    if n > m: return 0
    if n*k < m: return 0
    lenp = maxk if k>=maxk else k
    plist = [x for x in range(1,lenp+1)]
    perm = product(plist,repeat=n)
    plist = []
    for x in perm:
        if m==sum(x) and sum(x[0::2]) == maxk and sum(x[1::2]) == maxk:
                plist.append(x)
    answer = len(plist)*2 % 1000000007
    return answer

nout = 50
mout = 150
kout = 20
print(solution(nout,mout,kout))