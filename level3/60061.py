def solution(n, build_frame):
    results = set()
    for (x,y,what,how) in build_frame:
        if how==1:
            results.add((x,y,what))
            istrue = check(results)
            if not istrue:
                results.remove((x,y,what))
        elif how==0:
            results.remove((x,y,what))
            istrue = check(results)
            if not istrue:
                results.add((x,y,what))
    results = [list(i) for i in results]
    return sorted(results, key=lambda x: (x[0],x[1],x[2]))

def check(res):
    for (x,y,kind) in res:
        if kind==0:
            if y==0 or (x-1,y,1) in res or (x,y-1,0) in res or (x,y,1) in res:
                continue
            else:
                return False
        elif kind==1:
            if (x,y-1,0) in res or (x+1,y-1,0) in res or ((x-1,y,1) in res and (x+1,y,1) in res):
                continue
            else:
                return False
    return True

num = 5
bf = [[1,0,0,1],
      [1,1,1,1],
      [2,1,0,1],
      [2,2,1,1],
      [5,0,0,1],
      [5,1,0,1],
      [4,2,1,1],
      [3,2,1,1]]
print(solution(num, bf))