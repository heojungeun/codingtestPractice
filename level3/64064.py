def solution1(user_id, banned_id):
    import re
    tmp = [[] for _ in banned_id]
    for i, x in enumerate(banned_id):
        tmps = x.replace("*",".")
        lenx = len(x)
        for id_ in user_id:
            if lenx != len(id_):
                continue
            if re.match(tmps,id_):
                tmp[i].append(id_)
    results = set()
    dfs(tmp, user_id, [], results)
    return len(results)

def dfs(cand, users, res,results):
    import copy
    if not cand:
        results.add(tuple(sorted(res)))
        return
    ncand = copy.deepcopy(cand)
    cur = ncand.pop()
    for item in cur:
        if item in users:
            nres = copy.deepcopy(res)
            nres.append(item)
            nuser = copy.deepcopy(users)
            nuser.remove(item)
            dfs(ncand, nuser, nres, results)

def solution(user_id, banned_id):
    import re
    from itertools import product
    tmp = [[] for _ in banned_id]
    lenb = len(banned_id)
    for i, x in enumerate(banned_id):
        tmps = x.replace("*",".")
        lenx = len(x)
        for id_ in user_id:
            if lenx != len(id_):
                continue
            if re.match(tmps,id_):
                tmp[i].append(id_)
    result = list(product(*tmp))
    answer = set()
    for r in result:
        setr = set(r)
        if len(setr) == lenb:
            answer.add("".join(sorted(setr)))
    return len(answer)

uid = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
bid = ["fr*d*", "*rodo", "******", "******"]
print(solution(uid, bid))