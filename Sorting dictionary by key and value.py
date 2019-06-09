***********************************BY VALUE***********************************
n=int(input())
d=dict(input().split() for _ in range(n))
a={}
a=sorted(d.items(),key=lambda x:x[1])
print(a)


*************************************BY KEY*******************************
n=int(input())
d=dict(input().split() for _ in range(n))
a={}
a=sorted(d.items(),key=lambda x:x[0])
print(a)
