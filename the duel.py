def minPower(p):
    t=True 
    k=1
    while(t):
        c=k
        for i in p:
            c+=i
            if c<=0:
                print(k)
                break
        if  c>0:
            t=False
        else:
            k+=1
    return k
        
