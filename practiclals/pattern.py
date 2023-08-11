i=1
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()    
i=1
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()           
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()   
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()         
a=65
for i in range(1,6):
    for j in range(1,i+1):
        b=chr(a)
        print(b,end="")
    a+=1    
    print()              
i=0
j=0
while(i<=5):
    while(j<=i):
        print("*",end="")
        j=j+1
    j=0    
    i=i+1
    print('')        