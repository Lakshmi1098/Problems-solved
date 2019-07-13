s=input()
n=len(s)
c=0
for i in range(n):
  for j in rangr(i+1,n+1):
    k=s[i:j]
    if k==k[::-1] and len(k)>=2:
      c+=1
 print(c)
