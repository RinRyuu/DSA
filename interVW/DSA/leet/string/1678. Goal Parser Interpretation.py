a=''
command = "G()()()(al)"
for i in range(len(command)):
    if command[i]=='G':
        a=a+command[i]
    elif command[i]=='(':
        if command[i+1]==')':
            a=a+'o'
        elif command[i+1]=='a':
            a=a+'al'
print(a)