************************************QUESTION ******************************
he task is to count all the possible paths from top left to bottom right of a mXn 
matrix with the constraints that from each cell you can either move only to right or down.

***********************************SOLUTION****************************
***********************combinatorics method***************************
def paths(m,n):
    p=1
    for i in range (n,(m+n-1)):
       p=p*i
       p//=(i-n+1)
    return p


t=int(input())
while(t):
    mn=input().split()
    m=int(mn[0])
    n=int(mn[1])
    print(paths(m,n))
    t=t-1
