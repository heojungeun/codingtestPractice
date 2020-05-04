def solution(baseball):
    answer = 0
    import itertools
    cardlist = list(itertools.permutations([1,2,3,4,5,6,7,8,9],3))
    for i in cardlist:
        strike = 0
        ball = 0
        for x in baseball:
            tmpx = str(x[0])
            for j in range(0,3):
                for k in range(0,3):
                    if tmpx[j]==str(i[k]) and j==k:
                        strike += 1
                    elif tmpx[j]==str(i[k]) and j!=k:
                        ball += 1
            if x[1]!=strike or x[2]!=ball:
                strike =-1
                break
            strike =0
            ball = 0
        if strike != -1:
            answer +=1
    return answer

def solution1(baseball):
    answer = 0
    for i in range(111,999):
        tmp = str(i)
        if '0' in tmp or (tmp[0]==tmp[1] or tmp[0]==tmp[2] or tmp[1]==tmp[2]):
            continue
        strike = 0
        ball = 0
        for x in baseball:
            tmpx = str(x[0])
            for j in range(0,3):
                for k in range(0,3):
                    if tmpx[j]==tmp[k] and j==k:
                        strike += 1
                    elif tmpx[j]==tmp[k] and j!=k:
                        ball += 1
            if x[1]!=strike or x[2]!=ball:
                strike =-1
                break
            strike =0
            ball = 0
        if strike != -1:
            answer +=1
    return answer

base = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(base))