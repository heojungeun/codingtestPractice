# 거스름돈
def solution1(n, money):
    coin = [[0 for col in range(n+1)] for row in range(len(money))]
    coin[0][0] = 1
    for i in range(money[0], n+1, money[0]):
        coin[0][i] = 1
    for m in range(1, len(money)):
        for maxc in range(n+1):
            if maxc >= money[m]:
                coin[m][maxc] = (coin[m-1][maxc] + coin[m][maxc-money[m]])
            else:
                coin[m][maxc] = coin[m-1][maxc]
    return coin[-1][-1] % 1000000007

def solution(total, coin):
    arr = (total+1)*[0]
    coin.sort()
    for x in coin:
        arr[x] += 1
        for i in range(x+1,total+1):
            arr[i] += arr[i-x]
    return arr[total]%1000000007;
num = 5
my = [1,2,5]
print(solution(num,my))