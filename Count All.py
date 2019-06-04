
***********************************QUESTION************************************
SAMPLE INPUT 
5
5 6 7 8 4
SAMPLE OUTPUT 
12
Explanation
For 1, special elements are 5,6,7,8,4
For 2, special elements are 6,8,4
For 3, special element is 6
For 4, special elements are 8,4
For 5, special element is 5
Total count = 5+3+1+2+1 =12

*************************************SOLUTION******************************
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
        
