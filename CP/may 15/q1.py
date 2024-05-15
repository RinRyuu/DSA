t=int(input())
while(t>0):
    t-=1
    a,b=map(int, input().split())
    
    for i in range(b):
        x=a+1000
        y=a*2
        if x>y:
            a=x
        else:
            a=y    
    
    print(a)