def check(my_string): 
    brackets = ['()', '{}', '[]'] 
    while any(x in my_string for x in brackets): 
        for br in brackets: 
            my_string = my_string.replace(br, '') 
    return not my_string 
   
t=int(input())
for i in range(t):
    string=input()
    print("YES"  if check(string) else "NO") 
