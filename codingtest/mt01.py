from itertools import permutations
N = int(input())

disp = [6,2,5,5,4,5,6,3,7,5]
ds = []
for x in range(9):
    if disp[x] <= N:
        ds.append(x)
n = len(ds)
maxn = max(ds)
lists = list(permutations(ds, N//2))
for x in lists:
    strs = ""
    sum = 0
    for y in x:
        strs += str(y)
        sum += disp[y]
    if sum <= N:
        maxn = (maxn,int(strs))

print(maxn)