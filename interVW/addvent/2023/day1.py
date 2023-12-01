file_path = "inputday1a.txt"
num = [0,1,2,3,4,5,9,6,7,8]
sum = 0
with open(file_path, "r") as file:
    lines = file.readlines()
    for i in range(1,1001): #(1,1001)
        list =[]
        if 1 <= i <= len(lines):
            desired_line = lines[i - 1].strip()
        print(desired_line)
        for j in desired_line:
            try:
                list.append(int(j))
            except:
                pass
        if len(list)==1:
            num = list[0]
        elif len(list)>1:
            num = list[0]*10 + list[-1]
        sum += num
print(sum)            
        
     
