There are 7 floors in BH3 and only 2 lifts. Initially Lift A is at the ground floor and
Lift B at the top floor. Whenever someone calls the lift from N th floor, 
the lift closest to that floor comes to pick him up. If both the lifts are at equidistant from 
the N th floor,them the lift from the lower floor comes up.
SAMPLE INPUT 
2
3
5
SAMPLE OUTPUT 
A
A
 
 **************ans************
t=int(input())
a=0
b=7
for i in range(0,t):
    c=int(input())
    d=b-c
    e=c-a
    if(d>=e):
        a=c
        print("A")
    else:
        b=c
        print("B")
