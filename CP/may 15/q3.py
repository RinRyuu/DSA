def sum_of(n):
    sum_of_9 = 45
    complete_sets = n // 9
    total = complete_sets * sum_of_9
    remainder = n % 9
    
    total += sum(i for i in range(1, remainder + 1))
    
    print(total)

t=int(input())
while(t>0):
    t-=1
    n=int(input())
    sum_of(n)

