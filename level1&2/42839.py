def solution(numbers):
    import itertools
    answer = 0
    news = list(numbers)
    for r in range(2, len(numbers)+1):
        x = list(itertools.permutations(numbers,r))
        for row in x:
            s = "".join(row)
            # if s[0]=='0':
            #     s = s[1:]
            news.append(s)
    sets = list(set([int(x) for x in news]))
    num = max(sets)+1
    seive = [False, False] + [True] * (num - 1)
    for k in range(2, int(num ** 0.5 + 1.5)):
        if seive[k]:
            seive[k * 2::k] = [False] * ((num - k) // k)
    for x in sets:
        if seive[x]:
            answer += 1
    return answer

# def primesupto(n):
#     seive = [False, False] + [True] * (n-1)
#     for k in range(2, int(n**0.5 + 1.5)):
#         if seive[k]:
#             seive[k*2::k] = [False] * ((n-k)//k)
#     return seive[n]

n = "17"

print(solution(n))