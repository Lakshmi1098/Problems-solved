import math
def a(arr,l,h,k):
    if l<=h:
        mid = math.floor((l+h)/2)
        if arr[mid]==k:
            return 1
        elif arr[mid]>k:
            return a(arr,l,mid-1,k)
        elif arr[mid]<k:
            return a(arr,mid+1,h,k)
    return -1
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(a(arr,0,n-1,k))
