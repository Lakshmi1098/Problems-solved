import math
t=int(input())
for i in range(t):
    n=int(input())
    s=int(math.sqrt(n))
    if(s*s==n):
        print(1)
    else:
        print(0)
