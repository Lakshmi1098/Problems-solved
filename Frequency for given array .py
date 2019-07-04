2
5
2 3 2 3 5
4
3 3 3 3

Output:
0 2 2 0 1
0 0 4 0

Explanation:
Testcase 1: Counting frequencies of each array elements, we have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.



************ANS**************
#code
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        a[i]=a[i]-1
    for j in range(n):
        a[a[j]%n]=a[a[j]%n]+n
    for i in range(n):
        print(a[i]//n,end=" ")
    print()
        
