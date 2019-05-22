def s(N):
    j = 0
    while 2**j <= N:
        if 2**j == N:
            return "YES"
        j+=1
    return "NO"
t = int(input())
for i in range(0,t):
    N = int(input())
    print(s(N))
