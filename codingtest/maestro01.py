
# N, K = map(int,input().split())
# arr = list(map(int,input().split()))
#
# answer = 0
# if (N-K)%(K-1) == 0:
#     answer = (N-K)//(K-1)+1
# else:
#     answer = (N-K)//(K-1)+2
# print(int(answer))

# 37 4
# 31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 17 33
# 출력 12

# N, K = map(int,input().split())
# arr = list(map(int,input().split()))
# if N==K:
#     print(1)
# else:
#     print((N-2)//(K-1)+1)

N, K = map(int,input().split())
arr = list(map(int,input().split()))
s1 = (N-K)//(K-1)
s2 = (N-K)%(K-1)
if s2 == 0:
    s1 += 1
else:
    s1 += 2
print(s1)