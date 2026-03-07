n=int(input())
for i in range (n):
    x,y,m= map(int,input().split())
    k=m-(m-y)%x
    print(k)
