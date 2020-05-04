def solution(array, commands):
    answer = []
    for x in commands:
        i,j,k = x
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer

arr = [1, 5, 2, 6, 3, 7, 4]
cmd = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(arr,cmd))