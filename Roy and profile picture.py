Minimum dimension of the picture can be L x L, where L is the length of the side of square.
Now Roy has N photos of various dimensions.
Dimension of a photo is denoted as W x H 
where W - width of the photo and H - Height of the photo
When any photo is uploaded following events may occur:
  [1] If any of the width or height is less than L, user is prompted to upload another one. Print "UPLOAD ANOTHER" in this case.
  [2] If width and height, both are large enough and 
    (a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case.
    (b) else user is prompted to crop it. Print "CROP IT" in this case.
Given L, N, W and H as input, print appropriate text as output.


SAMPLE INPUT 
180
3
640 480
120 300
180 180

SAMPLE OUTPUT 
CROP IT
UPLOAD ANOTHER
ACCEPTED

************SOLUTION*************
l=int(input())
k=int(input())
for i in range(k):
    wh=input().split()
    w=int(wh[0])
    h=int(wh[1])
    if(w==l and h==l):
        print("ACCEPTED")
    elif(w>=l and h<l):
        print("UPLOAD ANOTHER")
    elif(h>=l and w<l):
        print("UPLOAD ANOTHER")
    elif(w<l and h<l):
        print("UPLOAD ANOTHER")
    elif(w>l and h>l and w==h):
        print("ACCEPTED")
    elif(w>l and h>l):
        print("CROP IT")
    else:
        print("CROP IT")
