def solution(arr):
    from math import gcd
    def nlcm(x,y):
        return x*y//gcd(x,y)
    while len(arr)>1:
        arr.append(nlcm(arr.pop(),arr.pop()))
    return arr[0]

def multply(a):
    return eval('*'.join([str(n) for n in a]))
arrrr = [2,6,8,14]
print(solution(arrrr))