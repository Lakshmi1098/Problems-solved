def value(r):
    if(r=='I'):
        return 1
    if r=='V':
        return 5
    if(r=='X'):
        return 10
    if r=='L':
        return 50
    if r=='C':
        return 100
    if r=='D':
        return 500
    if r=='M':
        return 1000
    
def rtod(n):
    i=0
    a=0
    while(i<len(n)):
        s1=value(n[i])
        if(i+1<len(n)):
            s2=value(n[i+1])
            if(s1>=s2):
                a=a+s1
                i=i+1
            else:
                a=a+s2-s1
                i=i+2
        else:
            a=a+s1
            i=i+1
    return a
n=input()
print(rtod(n))
