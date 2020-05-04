def solution(p, s):
    answer = []
    lenp = len(p)
    needday = [int((100-p[i])/s[i]) for i in range(lenp)]
    i = 0
    while i < lenp:
        x = needday[i]
        cnt, tmp = 1, i
        for j in range(i+1, lenp):
            y = needday[j]
            if x >= y:
                tmp = j
                cnt += 1
            else:
                break
        if i==tmp:
            i += 1
        else:
            i = tmp + 1
        answer.append(cnt)
    return answer

pro = [93,30,55]
speeds = [1,30,5]
print(solution(pro,speeds))