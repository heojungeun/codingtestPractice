def solution(prices):
    answer = []
    lenp = len(prices)
    for i in range(lenp):
        time = 0
        for j in range(i+1,lenp):
            time += 1
            if prices[i] > prices[j]:
                break
        answer.append(time)
    return answer

p = [1, 2, 1, 2, 3]
print(solution(p))