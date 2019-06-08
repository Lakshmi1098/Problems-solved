s=input()
a=[str(i) for i in str(s)]
st=sorted(a)
k=[]
for i in st:
    c=0
    for j in st:
        if(i==j):
            c=c+1

    k.append(c)
d=dict(zip(st,k))
for k in d:
    print(k,d[k])
