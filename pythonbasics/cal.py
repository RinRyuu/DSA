def ansfunc(a,b,operator):
    match operator:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return a/b
        case '%':
            return a%b         
    

def main():
    a = int(input('1st num: '))
    operator = input("operarator: ")
    b = int(input('2nd num: '))
    ans = ansfunc(a,b,operator)
    print(ans)
    
if __name__ == '__main__':
    main()