def solution(files):
    answer = []
    tmp = []
    cnt = 0
    for x in files:
        tmp.append(trisplit(x,cnt))
        cnt += 1
    tmp.sort(key= lambda x:(x[0],x[1],x[3]))
    for x in tmp:
        answer.append(files[x[3]])
    return answer

def trisplit(st, idx):
    lens = len(st)
    h,n,t = 0,0,0
    for i in range(lens):
        if h==0 and st[i].isdigit():
            h = i
        elif h and not st[i].isdigit():
            n = i
            break
    if n != 0:
        return st[:h].lower(), int(st[h:n]),st[n:], idx
    return st[:h].lower(), int(st[h:]), "", idx

def solution1(files):
    import re
    a = sorted(files, key= lambda file: int(re.findall('\d+',file)[0]))
    b = sorted(a, key= lambda file: re.split('\d+',file.lower())[0])
    return b

fes = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution1(fes))
