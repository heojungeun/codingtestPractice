def solution(n, delivery):
    answer = ''
    itemcheck = ["?"]*n
    delivery.sort(key= lambda x:x[2], reverse=True)
    for x in delivery:
        if x[2]==1:
            itemcheck[x[0]-1]="O"
            itemcheck[x[1]-1]="O"
        else:
            a,b=x[0],x[1]
            if itemcheck[a-1]=="O":
                itemcheck[b-1]="X"
            elif itemcheck[b-1]=="O":
                itemcheck[b - 1] = "X"
    return "".join(itemcheck)

num = 7
deli = [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]
print(solution(num,deli))