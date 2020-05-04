def solution(n):
    return bin(n)[2:].count("1")

num = 5000
print(solution(num))