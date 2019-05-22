num=int(input())
l=[int(x) for x in str(num)]
i=int(input())
c=0
for j in range(0,len(l)):
    if(i==l[j]):
        c=c+1
print(c)
