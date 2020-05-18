def solutionFail(n):
    queen(n)
    return count

def queen(N):
    chess = [[-1] for _ in range(N)]
    backtrack(chess,0)

def backtrack(q, n):
    lenn = len(q)
    if n == lenn:
        global count
        count += 1
    else:
        for i in range(lenn):
            q[n] = i
            if isPossible(q, n):
                backtrack(q, n+1)

def isPossible(ch, lev):
    for i in range(lev):
        if ch[i]==ch[lev]: return False
        if abs(ch[i] - ch[lev]) == abs(lev - i ): return False
    return True
count = 0
def solution(n):
    for i in range(n):
        nqueen([i], n)
    return count

def nqueen(col, N):
    global count
    lenc = len(col)
    if lenc == N:
        count += 1
        return
    cand = list(range(N))
    for i in range(lenc):
        if col[i] in cand:
            cand.remove(col[i])
        dist = lenc - i
        if col[i] + dist in cand:
            cand.remove(col[i] + dist)
        if col[i] - dist in cand:
            cand.remove(col[i] - dist)
    if cand != []:
        for i in cand:
            col.append(i)
            nqueen(col, N)
            col.pop()
    else:
        return

num = 4
print(solution(num))