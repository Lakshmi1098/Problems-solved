start=int(input())
end=int(input())
for i in range(start,end):
    t=i
    r=0
    k=len(str(i))
    while(i!=0):
        s=i%10
        r=r+s**k
        i=i//10
    
    if(t==r):
        print(t)
    
    
