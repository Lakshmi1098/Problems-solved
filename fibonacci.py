n=int(input())
n1=0
n2=1 
c=0
if(n==1):
    print(n1)
else:
    while(c<n):
        print(n1,end=" ")
        nth=n1+n2
        n1=n2
        n2=nth
        c+=1
        

        
        
   for i in range(int(input())):
    N=int(input())
    c=[1,1]
    if N>2:
        for i in range(2,N):
            c.append(c[i-2]+c[i-1])
    print(*c)
    print(sum([i for i in c if i%2==0 if i<=N]))
