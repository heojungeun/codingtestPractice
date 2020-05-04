def solution(s):
    minnum = 1001
    lens = len(s)
    if lens==1:
        return 1
    for i in range(1,lens//2+1):
        oristr, cnt = s[:i], 1
        j = i
        L = lens
        while True:
            if j+i > lens: break
            if oristr == s[j:j+i]:
                cnt += 1
                L -= i
            else:
                if cnt > 1:
                    L += len(str(cnt))
                oristr = s[j:j+i]
                cnt = 1
            j = j+i
        if cnt > 1:
            L += len(str(cnt))
        minnum = min(minnum, L)
    return minnum

str1="aa"
print(solution(str1))

