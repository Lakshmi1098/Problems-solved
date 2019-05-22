a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    j=1 
    while(j*j<=i):
        if(j*j==i):
            l.append(i)
        j=j+1 
    i=i+1 
print(*l)
