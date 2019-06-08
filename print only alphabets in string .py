s=input()
a=''.join([i for i in s if i.isalpha()])
print(a)




s=input()
st=""
for i in s:
    if i.isalpha():
        st+=i
print(st)
