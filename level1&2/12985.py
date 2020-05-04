def solution(n,a,b):
    import math
    answer = 3
    if a > b:
        a, b = b, a
    while n>1:
        half = n//2
        if a<= half and half < b:
            return int(math.log2(n))
        elif half<= a and half <= b:
            n = n//2
            a, b = a%half, b%half
            b = half if b==0 else b
        else:
            n = n//2
    return 1

def solution1(n,a,b):
    return ((a-1)^(b-1)).bit_length()

num = 8
anum = 5
bnum = 8
print(solution(num,anum,bnum))