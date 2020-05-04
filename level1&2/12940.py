from math import gcd
def solution(n, m):
    return [gcd(n,m),n*m//gcd(n,m)]

n1, n2 = 3, 12
print(solution(n1,n2))