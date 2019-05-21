import math
t=int(input()) 
for i in range(t):
    n=int(input())
    sum=1
    j=2
    while(j<=int(math.sqrt(n))):
        if(n%j==0):
            sum=sum+j+int(n/j);
        j=j+j
    if(sum==n):
        print(1) 
    else:
        print(0)
 
