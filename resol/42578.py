def solutionFail(clothes):
    from itertools import combinations
    answer = 0
    cdic = {}
    for c, g in clothes:
        cdic[g] = cdic.get(g, 0) + 1
    for i in range(1, len(cdic.keys()) + 1):
        clist = list(combinations(cdic.values(), i))
        for x in clist:
            if i == 1:
                answer += x[0]
            else:
                answer += multiply(x)
    return answer


def multiply(arr):
    from functools import reduce
    return reduce(lambda x, y: x * y, arr)


def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([g for c, g in clothes])  # 분류에 따른 옷 개수가 중요함
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer


c_ = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],
      ["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(c_))
