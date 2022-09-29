i=1
while i<4:
    j=1
    while j<4:
        if i==2:
            print(j+1,end=" ")
        elif i==3:
            print(j+2,end=" ")
        else:
            print(j,end=" ")
        j=j+1
    i=i+1
    print()