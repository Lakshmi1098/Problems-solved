def solve (Ar):
    r=[]
    r.append(n)
    for i in range(2,len(Ar)+1):
        c=0
        for j in range(0,len(Ar)):
            if(Ar[j]%i==0):
                c=c+1
        r.append(c)
    s=sum(r)
    return s
n = int(input())
Ar = list(map(int, input().split()))

out_ = solve(Ar)
print (out_)
        
