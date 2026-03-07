t=int(input())
for i in range(t):
    bb=0
    bi=0
    n=int(input())
    for ch in range(1,n+1):
        a,b=map(int,input().split())
        if a <= 10: 
            if b>bb:
                bb=b
                bi=ch
    print(bi)
