n=int(input())
m=list(map(int,input().split()))
left=0
right=n-1
serja=0 
dima=0
turn=0
while left <= right:
    if m[left]> m[right]:
        pick=m[left]
        left+=1
    else:
        pick=m[right]
        right-=1
    if turn==0:
        serja=serja+pick
    else :
        dima=dima+pick
    if turn==0:
        turn=1
    else:
        turn=0
print(serja,dima)
