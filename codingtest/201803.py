import numpy as np
import re
from collections import Counter
def solution(str1, str2):
    A = spltwo(str1)
    B = spltwo(str2)

    ac = Counter(A)
    bc = Counter(B)
    inter = sum(list((ac & bc).values()))
    union = sum(list((ac | bc).values()))
    if union == 0:
        return 65536
    answer = int((inter/float(union))*65536)
    return answer

def spltwo(str):
    arr = [str[i:i+2].lower() for i in range(len(str)-1) if re.findall('[a-zA-Z][a-zA-Z]',str[i:i+2])]
    return arr

s1 = 'FRANCE'
s2 = 'french'
print(solution(s1, s2))

# def solution(str1, str2):
#     A = spltwo(str1)
#     B = spltwo(str2)
#     if not A or not B:
#         return 65536
#     x = np.array(A)
#     y = np.array(B)
#     list = np.intersect1d(x, y)
#     cnt = 0
#     for z in list:
#         cnt += min(A.count(z), B.count(z))
#     union = len(A) + len(B) - cnt
#     answer = int((cnt/float(union))*65536)
#     return answer
# def spltwo(str):
#     arr = [(x[0]+x[1]).lower() for x in zip(str, str[1:]) if (x[0]+x[1]).isalpha()]
#     return arr