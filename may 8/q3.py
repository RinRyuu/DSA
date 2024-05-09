t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    diss_a =[]
    for i in a:
        if i-y>0:
            diss_a.append(i-y)
        elif i-y<=0:
            diss_a.append(0)
    sum =0
    sum_nor=0
    for i in diss_a:
        sum+=i
    for i in a:
        sum_nor+=i
    
    if sum+x<sum_nor:
        print('COUPON')
    else:
        print('NO COUPON')
