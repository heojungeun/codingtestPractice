def solution(n, lost, reserve):
    answer = n-len(lost)
    lostmp = [x for x in lost]
    for x in lost:
        if x in reserve:
            answer += 1
            reserve.remove(x)
            lostmp.remove(x)
    lost = lostmp
    for x in lost:
        for y in reserve:
            if y == x-1 or y == x+1:
                answer += 1
                reserve.remove(y)
                break

    return answer

num = 10
l = [1,3,4,5,9]
reser = [1,2,3,4,5,7,8,9]
print(solution(num,l,reser))