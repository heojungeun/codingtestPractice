def solution1(n):
    sqrt_5 = 5 ** (1/2)
    ans = 1/sqrt_5 *(((1+sqrt_5)/2)**(n+1) - ((1-sqrt_5)/2)**(n+1))
    return int(ans) % 1000000007

def solution(n):
    a,b= 0,1
    for i in range(n):
        a, b = b, a+b
    return b % 1000000007
num = 7
print(solution(num))