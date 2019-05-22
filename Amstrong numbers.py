T = int(input())
while T:
    sum = 0 
    N = input()
    for n in N:
        sum  += int(n)**3
    if sum == int(N):
        print('Yes')
    else:
        print('No')
    T -=1
    
    
    
t=int(input())
while t:
    n=int(input())
    n1=n
    su=0
    while n1:
        su+=(n1%10)**3
        n1=n1//10
    if(su==n):
        print("Yes")
    else:
        print("No")
    t-=1
