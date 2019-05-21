SIMPLE SOLUTION:
num=int(input())
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("not a Prime number")
            break

    print("Prime number")
    
    
    OPTIMIZED SOLUTION:
    def prime(num):
    if(num<=1):
        return ("Not Prime")
    if(num==2 or num==3):
        return ("Prime")
    if(num%2==0 or num%3==0):
        return ("Not Prime")
    for i in range(5,num):
        if(num%i==0):
            return("Not Prime")
    return ("Prime")
    
    
num=int(input())
print(prime(num))
