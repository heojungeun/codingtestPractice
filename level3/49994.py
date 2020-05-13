def solution(dirs):
    arr = set()
    dico = {'U':[0,1], 'D':[0,-1], 'R':[1,0], 'L':[-1,0]}
    st= [0,0]
    for d in dirs:
        x, y = st
        x2, y2 = x+dico[d][0], y+dico[d][1]
        if -5 > x2 or x2 > 5 or -5 > y2 or y2 > 5:
            continue
        tmp = [str(x)+str(y),str(x2)+str(y2)]
        arr.add("".join(sorted(tmp)))
        st = [x2,y2]
    return len(arr)

ds = "LULLLLLLU"
print(solution(ds))