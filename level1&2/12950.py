def solution(arr1, arr2):
    answer = []
    # for x, y in zip(arr1, arr2):
    #     tmp = []
    #     for i, j in zip(x,y):
    #         tmp.append(i+j)
    #     answer.append(tmp)
    answer = [[i+j for i, j in zip(x, y)] for x, y in zip(arr1, arr2)]
    return answer

a1, a2 = [[1]], [[3]]
print(solution(a1,a2))