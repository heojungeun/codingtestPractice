def solution(number, k):
    # import itertools
    # dig = []
    # for i in range(0,len(number)):
    #     dig.append(i)
    # dig = list(itertools.combinations(dig,k))
    # lenn = len(number)
    # arr = []
    # for x in dig:
    #     tmp = ''
    #     for i in range(lenn):
    #         if i in x:
    #             continue
    #         tmp += number[i]
    #     arr.append(int(tmp))
    # answer = str(max(arr))
    st = []
    for x in number:
        if k==0 or not st:
            st.append(x)
        else:
            if st[-1] < x:
                tmp = reversed(st)
                for e in tmp:
                    if e < x:
                        st.pop()
                        k -= 1
                        if k==0 or not st:
                            st.append(x)
                            break
                    else:
                        st.append(x)
                        break
            else:
                st.append(x)
    while k > 0:
        st.pop()
        k -= 1
    answer = "".join(st)
    return answer

def standardsolution(number,k):
    st = []
    for i, num in enumerate(number):
        while st and k>0 and st[-1]<num:
            st.pop()
            k -= 1
        if k==0:
            st += number[i:]
            break
        st.append(num)
    st = st[:-k] if k>0 else st
    return "".join(st)

n = "12"
nk = 1
print(solution(n,nk))