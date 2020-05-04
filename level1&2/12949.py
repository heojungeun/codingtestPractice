def solution(arr1, arr2):
    lenr = len(arr1)
    lenk = len(arr2)
    lenc = len(arr2[0])
    answer = [[0 for col in range(lenc)] for row in range(lenr)]
    for i in range(lenr):
        for j in range(lenc):
            for k in range(lenk):
                answer[i][j] += arr1[i][k]*arr2[k][j]
    return answer

def sol(A,B):
    return [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

a1, a2 = [[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]
print(solution(a1,a2))