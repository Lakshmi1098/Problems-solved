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


*************EFFICIENT METHOD*********************
n=int(input())
a=list(map(int,input().split()))
MAX=max(a)
s=[]
count=[0]*(MAX+1)
s=[0]*(n+1)
for i in range(n):
    count[a[i]]+=1
for i in range(1,n+1):
    for j in range(i,MAX+1,i):
        s[i]+=count[j]
b=sum(s)
print(b)
        
