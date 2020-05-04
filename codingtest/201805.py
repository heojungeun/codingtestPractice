import collections
import re

def solution1(cacheSize, cities):
    answer = 0
    cache = [0]
    arr = [i.lower() for i in cities]

    if cacheSize==0:
        cache[0] = len(cities)
    else:
        for x in arr:
            cache = LRU(cache,cacheSize,x)

    miss = cache[0]
    answer = (len(cities)-miss) + miss*5
    return answer

def LRU(cache, pcsize, pct):
    if len(cache)<pcsize+1:
        if cache.count(pct)==1: #cache hit
            cache.remove(pct)
            cache.insert(1,pct)
        else: #cache miss
            cache.insert(1,pct)
            cache[0] += 1
    else:
        if cache.count(pct)==1: #cache hit
            cache.remove(pct)
            cache.insert(1,pct)
        else: #cache miss
            cache.pop()
            cache.insert(1,pct)
            cache[0] += 1
    return cache

def solution(cacheSize, cities):
    d = collections.deque(maxlen=cacheSize)
    answer = 0
    for x in cities:
        x.lower()
        if x in d: # hit
            d.remove(x)
            d.append(x)
            answer += 1
        else: # miss
            d.append(x)
            answer += 5
    return answer

csize = 0
cts = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(csize, cts))