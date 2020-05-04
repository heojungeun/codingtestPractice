# # 런타임 에러
# def solution(w,h):
#     if w==1 or h==1:
#         return 0
#     answer = 0
#     for i in range(1,w):
#         y = int(h - (h/w)*i)
#         answer += y
#     return answer*2

import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))

we = 8
he = 12
print(solution(we, he))