def solution(phone_book):
    import re
    pb = sorted(phone_book)
    lenp = len(pb)
    for i in range(lenp):
        p = re.compile(pb[i])
        for j in range(i+1, lenp):
            m = p.match(pb[j])
            if m:
                return False
    return True

pb_=["12","123","1235","567","88"]
print(solution(pb_))