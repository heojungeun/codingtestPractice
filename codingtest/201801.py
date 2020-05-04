# secret map
def solution(n, arr1, arr2):
    answer = []

    # for i in range(0,n):
    #     row = arr1[i] | arr2[i]
    #     str = bin(row)[2:].replace('0',' ')
    #     str = str.replace('1','#')
    #     while len(str) < n:
    #         str = ' '.__add__(str)
    #     answer.append(str)
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i|j)[2:])
        a12 = a12.rjust(n,'0')
        a12 = a12.replace('1','#').replace('0',' ')
        answer.append(a12)

    return answer

num = 6
ar1 = [46, 33, 33 ,22, 31, 50]
ar2 = [27 ,56, 19, 14, 14, 10]
print(solution(num, ar1, ar2))

#  ['######', '###  #', '##  ##', '#### ', '#####', '### # ']
#  ["######", "###  #", "##  ##", " #### ", " #####", "### # "]