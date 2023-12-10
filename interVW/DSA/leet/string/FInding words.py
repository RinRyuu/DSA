words = ["abc","bcd","aaaa","cbc"]
x = "z"
a=[]
for i in range(len(words)):
    if x in words[i]:
        a.append(i)
        
print(a)