'''
list of add number from 0 to the limit (given by user)
'''
limit = int(input())
list = []
for i in range(1,limit):
    if not i%2==0:
        list.append(i)
print(list)