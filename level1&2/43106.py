from itertools import combinations
from itertools import product
def solution(user_id, banned_id):
    import re
    if len(user_id)==1:
        return 1
    bids = []
    newban = []
    tmp = []
    for x in banned_id:
        if x not in newban:
            if x not in tmp:
                newban.append(x)
        else:
            newban.remove(x)
            tmp.append(x)
    for x in newban:
        tmp = []
        listx = x.replace("*",".")
        for id in user_id:
            if re.fullmatch(listx,id) != None:
                tmp.append(id)
        bids.append(tmp)
        #for tmpid in tmp:user_id.remove(tmpid)
    pbid = set(product(*bids))
    answer = len(pbid)
    for i in pbid:
        t = set(i)
        if len(t)<len(bids):
            answer -= 1
    return answer

uid = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
bid = ["*rodo", "*rodo", "******"]
print(solution(uid,bid))