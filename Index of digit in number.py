num=int(input())
l=[int(x) for x in str(num)]
i=int(input())
for j in range(0,len(l)):
    if(i==l[j]):
        print(j)
        break
else:
    print(-1)
