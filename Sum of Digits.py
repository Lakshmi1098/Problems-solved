num=int(input())
l=[int(x) for x in str(num)]
print(sum(l))



num=int(input())
s=0
while(num!=0):
  r=num%10
  s=s+r
  num=num//10
print(s)
  
