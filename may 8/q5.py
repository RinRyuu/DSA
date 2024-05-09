# t=int(input())

# while(t>0):
#     t-=1
#     n=int(input())
#     a = list(map(int, input().split()))
#     temp_ans=[]
#     ans=0
#     a=sorted(a)
#     mid=round(len(a)/2)-1
#     l_mid=mid
#     u_mid=mid+1
#     if len(a)%2==0:
#         for i in range(mid+1):
#             temp_ans.append((a[u_mid]-a[l_mid]))
#             l_mid-=1
#             u_mid+=1
#     else:
#         temp_ans.append(a[-1])
#         mid-=1
#         for i in range(mid+1):
#             temp_ans.append((a[u_mid]-a[l_mid]))
#             l_mid-=1
#             u_mid+=1
#     for i in temp_ans:
#         ans+=i
#     print(ans)
    
    
# t = int(input())

# while t > 0:
#     t-=1
#     n=int(input())
#     a = list(map(int, input().split()))
#     a=sorted(a)
#     mid=n//2 
#     ans=0
#     l_mid=mid
#     u_mid=mid+1
#     if n%2==0:
#         for i in range(mid):
#             ans+=a[mid]-a[i]
#             ans+=a[n-1-i]-a[mid]  
#     if n%2!=0:
#         ans+=a[-1]
#         mid-=1
#         for i in range(mid+1):
#             ans+=(a[u_mid]-a[l_mid])
#             l_mid-=1
#             u_mid+=1
#     print(ans)


    
t = int(input())

while t > 0:
    t-=1
    n=int(input())
    a = list(map(int, input().split()))
    a=sorted(a)
    ans=0
    max_sum = 0
    sum_so_far = 0

# Traverse the array
    for i in range(n):
        if i % 2 == 1:
            sum_so_far -= a[i]
        else:
            sum_so_far = max(a[i], sum_so_far + a[i])
        max_sum = max(max_sum, sum_so_far)

    sum_so_far = 0

# Traverse array
    for i in range(1, n):
        if i % 2 == 0:
            sum_so_far -= a[i]
        else:
            sum_so_far = max(a[i], sum_so_far + a[i])
            ans = max(max_sum, sum_so_far)

    print(ans)