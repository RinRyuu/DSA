t = int(input())

while t > 0:
    n = int(input('n= '))
    s = input('s= ')
    ans =''
    code = ['00','01','10','11']
    for i in range(n-1):
        f=s[i]+s[i+1]
        if (i+1)%2!=0:
            if f == code[0]:
                ans+='A'

            if f == code[1]:
                ans+='T'

            if f == code[2]:
                ans+='C'

            if f == code[3]:
                ans+='G'
            
    t -= 1
