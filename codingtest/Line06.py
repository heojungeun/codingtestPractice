def solution(directory, command):
    from anytree import Node, RenderTree
    answer = []
    listnode = []
    listname = []
    if len(directory)==1:
        listnode.append(Node("/"))
    else:
        for x in directory:
            if x=="/":
                listnode.append(Node("/"))
                listname.append("/")
            else:
                listx = x.split("/")[1:]
                for idx, y in enumerate(listx):
                    if idx ==0:
                        n = Node(y,parent=listnode[0])
                        if y not in listname:
                            listnode.append(n)
                            listname.append(y)
                    else:
                        if y not in listname:
                            n = Node(y, parent=listnode[listnode.index(listx[idx - 1])])
                            listnode.append(n)
    print(RenderTree(listnode[0]))
    # for x in command:
    #     if x == "mkdir":
    #         listx = x.split("/")[1:]
    #         if len(listx)==1:
    #             Node(listx[0],parent=listnode[0])
    #         else:
    #             Node(listx[-1],parent=listx[-2])
    #     elif x == "rm":
    #         listx = x.split("/")[1:]
    #         if len(listx) == 1:
    #             listx[0].parent= None
    #         else:
    #             listx[-1].parent = None
    return answer

dir = [
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
]
cmd = [
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]

print(solution(dir,cmd))