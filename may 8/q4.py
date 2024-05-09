t= int(input())
while(t>0):
    t-=1
    leg=int(input())
    animal_count=0
    for i in range(leg):
        if leg-4>=0:
            leg-=4
            animal_count+=1
        elif leg-2>=0:
            leg-=2
            animal_count+=1
             
    print(animal_count)