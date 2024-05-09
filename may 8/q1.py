a,b = map(int, input().split())
arry=[]
arry_str = input().split()
for i in arry_str:
    arry.append(int(i))
    
if b in arry:
    print('yes')
else:
    print('no')