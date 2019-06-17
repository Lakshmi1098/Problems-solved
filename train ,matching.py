'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
for k in range(t):
    n=int(input())
    r=n%12
    if(r==1):
        print(n+11,'WS')
    if r==2:
        print(n+9,'MS')
    if r==3:
        print(n+7,'AS')
    if r==4:
        print(n+5,'AS')
    elif r==5:
        print(n+3,'MS')
    elif r==6 :
        print(n+1,'WS')
    elif r==7:
        print(n-1,'WS')
    elif r==8:
        print(n-3,'MS')
    elif r==9:
        print(n-5,'AS')
    elif r==10:
        print(n-7,'AS')
    elif r==11:
        print(n-9,'MS')
    elif r==12:
        print(n-11,'WS')
    r=-1
