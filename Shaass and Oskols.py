n=int(input())
b=list(map(int,input().split()))
m=int(input())
for i in range(m):
    x,y=map(int,input().split())
    x-=1
    left=y-1
    right=b[x]-y
    if x>0:
        b[x-1]+=left
    if x<n-1:
        b[x+1]+=right
    b[x]=0
for i in b:
    print(i)
