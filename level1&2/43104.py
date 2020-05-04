def solution(board, moves):
    answer = 0
    st = []
    lenb = len(board)
    for i in moves:
        x = i - 1
        for y in range(lenb):
            ele = board[y][x]
            if ele != 0:
                if len(st) > 0 and st[-1] == ele:
                    st.pop()
                    answer += 1
                else:
                    st.append(ele)
                board[y][x] = 0
                break
    return answer*2

b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
m = [1,5,3,5,1,2,1,4]
print(solution(b,m))