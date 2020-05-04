def solution(answer_sheet, sheets):
    answer = -1
    flag = 0
    st = []
    lensh = len(sheets)
    lenan = len(answer_sheet)
    maxa = 0
    for idx,i in enumerate(sheets):
        for idy, j in enumerate(sheets):
            if idx!=idy:
                for l, k in enumerate(answer_sheet):
                    if i[l] != k and j[l] != k and i[l]==j[l]:
                        st.append(l)
                lens = len(st)
                maxs, tmp=0,0
                if lens == 1:
                    maxs=1
                else:
                    for ele in range(0, lens):
                        if ele + 1 == lens:
                            break
                        if st[ele] == st[ele + 1] - 1:
                            tmp += 1
                        else:
                            tmp += 1
                            if maxs <= tmp:
                                maxs = tmp
                            tmp = 0
                tmp = lens + maxs**2
                maxa = max(tmp, maxa)
            st = []
    return maxa

ash = "24551"
sts = ["24553", "24553", "24553", "24553"]
print(solution(ash,sts))