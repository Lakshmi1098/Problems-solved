def canWin(maze,k):
    l=[]
    t=-1
    c=len(maze[0])
    r=len(maze)
    for i in maze:
        l.append(list(i))
    cp=0
    rp=0
    while cp<c-1 and rp<r-1:
        if l[0][0]=='.':
            t+=1
        if l[rp][cp+1]=='.' or l[rp+1][cp]!='.':
            t+=1
            cp=cp+1
        elif l[rp][cp+1]!='.' or l[rp+1][cp] =='.':
            t+=1
            rp=rp+1
    if t==0:
        return "Better luck next time"
    elif t<=k:
        return "Fahad wins"


