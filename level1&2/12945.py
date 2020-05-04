def solution(n):
    D = [0,1]
    for i in range(2,n+1):
        D.append(D[i-1]+D[i-2])
    return D[n]%1234567

def fibo(n):
    a,b = 0,1
    for i in range(n):
        a, b = b, a+b # [n-2], [n-1]
        print(a,b)
    return a

num = 9
# print(solution(num))
print(fibo(num))