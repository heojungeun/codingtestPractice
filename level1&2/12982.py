def solution(d, budget):
    answer = 0
    cnt = 0
    tmp_d = sorted(d)
    for x in tmp_d:
        if cnt+x <= budget:
            cnt += x
            answer += 1
        else:
            break
    return answer

deb= [2,2,3,3]
b = 10
print(solution(deb,b))