t=int(input())
while(t>0):
    t-=1
    n=int(input())
    x=input()
    a='w'
    win=0
    for i in x:
        if a=='w' or a!=i:
            a=i
            win+=1
        elif a==i:
            a='w'
    print(win)
        