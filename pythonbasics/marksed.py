Nso = int(input("Enter no. sem: "))
nosub =[]
for i in range(Nso):
    nosubs =int(input(f"enter no. of subs in{i+1} sem : "))
    nosub.append(nosubs)
maxinsem=[]
for i in range(Nso):
    print(f"marks obtained in {i+1}sem: ")
    for j in range((len(nosub)-1)):
        if j==0:
            max=0
        temp = int(input(""))
        while(temp>100):
            temp = int(input("invalid input"))
        if temp>max:
            max=temp
        
    maxinsem.append(max)
for _ in range(Nso):
    print(f"maximum marks in {_+1} sem is {maxinsem[_]}")