def solution(prices):
    lenp = len(prices)
    answer = []
    for i in range(lenp):
        num = 0
        for j in range(i+1,lenp):
            num += 1
            if prices[i] > prices[j]:
                break
        answer.append(num)
    return answer

print(solution([1,2,3,2,3]))