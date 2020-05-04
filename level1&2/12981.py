def solution1(n, words):
    from collections import Counter
    answer = []
    c = Counter(words).most_common(1)[0]
    if c[1] > 1:
        idx = words.index(c[0], words.index(c[0])+1)
        answer = [idx%n+1, idx//n+1]
    else:
        tmp = ""
        for i, x in enumerate(words):
            if i==0:
                tmp = x[-1]
            else:
                if tmp != x[0]:
                    answer = [i%n+1, i//n+1]
                    break
                else:
                    tmp = x[-1]
        if not answer:
            answer = [0,0]
    return answer

def solution(n, words):
    nset = set([words[0]])
    prev = words[0]
    for i in range(1,len(words)):
        if prev[-1]!= words[i][0] or words[i] in nset:
            return [(i%n)+1, (i//n)+1]
        nset.add(words[i])
        prev = words[i]
    return [0,0]

def sol(n,words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]: return [i%n+1, i//n+1]
    return [0,0]
num = 2
wordsarr= ["hello", "one", "bven"]
print(solution(num,wordsarr))