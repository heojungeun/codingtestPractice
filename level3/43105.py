def solution1(D):
    lend = len(D)
    for i in range(1,lend):
        lenx = len(D[i])
        for j in range(lenx):
            if j == 0:
                D[i][j] += D[i-1][j]
            elif j == lenx-1:
                D[i][j] += D[i-1][-1]
            else:
                D[i][j] += max(D[i-1][j-1],D[i-1][j])
    answer = max(D[-1])
    return answer

solution = lambda t, arr = []: max(arr) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([[0]+arr, arr+[0], t[0]])])

tri = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(tri))