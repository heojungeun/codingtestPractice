def solution(road, n):
    answer = -1
    zerocnt = road.count('0')
    if zerocnt <= n:
        return len(road)

    return answer

r= "111011110011111011111100011111"
num = 3
print(solution(r,num))