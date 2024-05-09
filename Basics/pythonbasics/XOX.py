import random

def game():
    Flag=True
    while(Flag):
        cha = input('plz select the charecter u want X or O: ').upper()
        if cha in ['X','O']:
            Flag=False
    
    boardr1 = [' ' , ' ',' ']
    boardr2 = [' ' , ' ',' ']
    boardr3 = [' ' , ' ',' ']
    
    startgame(cha,boardr1,boardr2,boardr3)
    
def startgame(cha,boardr1,boardr2,boardr3):
    Flag1=False
    avala = [0,1,2,3,4,5,6,7,8]
    if cha=='X':
        while(Flag1==False):
            try:
                i = int(input('where do u want to place X: '))
                print(
                    boardr1,
                    boardr2,
                    boardr3          
                )
                if i not in avala:
                    raise ValueError
                else:
                    print(i)
            except ValueError:
                i = random.choice(avala)
        
    

def main():
    key = 'z'
    while(key!='q'):
        print('''
        Q -> quit
        S -> start      
              ''')
        key = input('key -> ').lower()
        if key=='s':
            game()
            
    print('Game Ended')


if __name__ == '__main__':
    main()