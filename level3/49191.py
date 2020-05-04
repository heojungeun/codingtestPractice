# 순위, 플로이드 마샬
def solution1(n, results):
    wins,loses = {}, {}
    for i in range(1, n+1):
        wins[i],loses[i] = set(),set()
    for i in range(1, n+1):
        for bat in results:
            if bat[0] == i: # i가 이긴 선수
                wins[i].add(bat[1])
            elif bat[1] == i: # i가 진 선수
                loses[i].add(bat[0])
        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])
    answer = 0
    for i in range(1,n+1):
        if len(wins[i])+len(loses[i])==n-1:
            answer += 1
    return answer

def solution(n, results):
    from collections import defaultdict
    answer = 0
    wins, loses = defaultdict(set), defaultdict(set)
    for result in results:
        wins[result[0]].add(result[1]) # 0번째 선수에게 1번째 선수가 졌다 -> 0번째 선수가 이긴 선수들
        loses[result[1]].add(result[0]) # 1번째 선수가 패배한 선수들
    for i in range(1, n+1):
        for winner in loses[i]:wins[winner].update(wins[i]) # i에게 이긴 선수 winner는 i에게 진 선수들 wins[i]을 무조건 이긴다
        for loser in wins[i]:loses[loser].update(loses[i]) # i에게 진 선수 loser는 i에게 이긴 선수들 loses[i]에게 무조건 진다
    for i in range(1, n+1):
        if len(wins[i])+len(loses[i]) == n-1:
            answer += 1
    return answer

num = 5
res = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(num,res))