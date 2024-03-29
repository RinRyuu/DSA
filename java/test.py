for _ in range(int(input())):
    n=int(input())-1
    data =input().split(' ')
    ans=[]
    for i in data:
        ans.append(int(i))

    max= ans.sort()
    total=0
    for x in range(len(ans)):
        if x!= n-1:
            total+=ans[x]
        else:
            total+=(ans[x]*2)

    if max>total:
        print(max+'ans')
    else:
        print(total+'total')
