def solution(heights):
    answer = []
    heights.reverse()
    lenh = len(heights)
    for i, x in enumerate(heights):
        tmp = 0
        for j, y in enumerate(heights):
            if i > j:
                continue
            if x < y:
                tmp = lenh - j
                break
        answer.append(tmp)
    answer.reverse()
    return answer

h = [1,5,3,6,7,6,5]
print(solution(h))