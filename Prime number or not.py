SIMPLE SOLUTION:
num=int(input())
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("not a Prime number")
            break

    print("Prime number")
    
    
 ******************USING FUNCTION:**************
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



****************OPTIMIZED SOLUTION:**************
import math as m
def prime(n):
    if n<=1:
        return False
    elif n==2 or n==3:
        return n
    elif n>2 and n%2==0:
        return False
        
    d=m.floor(m.sqrt(n))
    for j in range(5,d):
        if n%i==0:
            return False
    return n


n=int(input())
print(prime(n))
