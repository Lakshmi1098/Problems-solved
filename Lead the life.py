def calculateProfit(n, earning, cost, e):
    # Write your code here
    s=0
    a=0
    b=len(earning)
    for i in range(1,b):
        s+=(e*earning[i])
    for i in range(1,b-1):
        a+=(e*cost[i])
    return s-a
    
