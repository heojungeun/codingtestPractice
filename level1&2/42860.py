def solution(name):
    import re
    answer, idx = 0, 0
    lenn = len(name)
    p = re.compile("[B-Z]")
    while True:
        m = p.search(name)
        if m:
            num = ord(name[idx])
            answer += min(num-65,91-num)
            name = name[:idx]+'A'+name[idx+1:]
            right, left = idx, idx
            for i in range(lenn):
                if right >= lenn:
                    right = 0
                if left < 0:
                    left = lenn - 1
                if name[right] != 'A':
                    idx = right
                    answer += i
                    break
                if name[left] != 'A':
                    idx = left
                    answer += i
                    break
                right += 1
                left -= 1
        else:
            break
    return answer

n = "JAN"
print(solution(n))