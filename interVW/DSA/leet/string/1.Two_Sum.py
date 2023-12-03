'''https://leetcode.com/problems/two-sum/'''

nums = [2,2,11,15,7]
target = 4
# out = False
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if j<(len(nums)-1):
            
#             print('1')
#             if j==i+1:
#                 continue
#             if nums[j]+nums[i+1]==target:
#                 ans = [j,i+1]
#                 out = True
                
#     if out==True:
#         print(ans)
#         break

#hashmap
numMap = {}
n = len(nums)

        # Build the hash table
for i in range(n):
    numMap[nums[i]] = i

        # Find the complement
for i in range(n):
    print(i,'from last loop')
    complement = target - nums[i]
    if complement in numMap and numMap[complement] != i:
        print(f"{[i, numMap[complement]]}")

print('[]')
    
    