def solution(heights):
    answer = []
    prev = 0
    for i, x in enumerate(heights):
        if prev == 0:
            answer.append(0)
        else:
            if prev <= x:
                tmp = answer[i-1]
                if tmp == 0:
                    answer.append(0)
                else:
                    for j in range(tmp-1,-1,-1):
                        if heights[j] > x:
                            answer.append(j+1)
                            break
                    else:
                        answer.append(0)
            else:
                answer.append(i)
        prev = x
    return answer

def solution1(h):
    answer = [0] * len(h)
    for i in range(len(h)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                answer[i] = j+1
                break
    return answer

def solution2(h):
    answer = [0] * len(h)
    stack = []
    for i in reversed(range(len(h))):
        while stack and stack[-1][1] < h[i]:
            idx, height = stack.pop()
            answer[idx] = i+1
        stack.append((i,h[i]))
    return answer

h_= [1,5,3,6,7,6,5]
print(solution2(h_))