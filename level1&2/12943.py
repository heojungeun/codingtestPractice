def solution(num):
    answer = 0
    if num==1: return 0
    while answer<500:
        if num%2 == 0:
            num = num/2
        else:
            num = num*3+1
        if num == 1:
            return answer+1
        answer += 1
    return -1

num = 626331
print(solution(num))