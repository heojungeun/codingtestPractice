def solutionNo(budgets, M):
    lenb = len(budgets)
    sumb = sum(budgets)
    if sumb <= M:
        return max(budgets)
    minavg = M//lenb
    maxavg = sumb//lenb
    answer = minavg
    budgets.sort()
    for maxcost in range(minavg+1,maxavg):
        tmp = 0
        for i in range(lenb):
            if budgets[i] > maxcost:
                tmp += maxcost*(lenb-i)
                if tmp > M:
                    break
                else:
                    answer = maxcost
                    break
            else:
                tmp += budgets[i]
        else:
            answer = maxcost
    return answer

def solution(budgets, M):
    mins, maxs = 0, max(budgets)
    answer = 0
    while mins <= maxs:
        mid = (mins + maxs) // 2 # mid <- 상한가
        tmp = [i if i < mid else mid for i in budgets]
        if sum(tmp) > M:
            maxs = mid - 1
        elif sum(tmp) <= M:
            answer = mid
            mins = mid + 1
    return answer

def solution1(budgets, M):
    budgets.sort()
    lenb = len(budgets)
    cap = 0
    for i, b in enumerate(budgets):
        tmpsum = (b - cap) * (lenb - i)
        if tmpsum <= M:
            cap = b
            M -= tmpsum
        else:
            cap += M // (lenb - i)
            break
    return cap

bg = [120, 110, 140, 150]
m = 485
print(solution1(bg,m))