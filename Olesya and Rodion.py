n,t=map(int,input().split())
if t == 10 and n == 1:
    print(-1)
else:
    num = 10 ** (n - 1)
    rem = num % t
    if rem != 0:
        num += (t - rem)
    if len(str(num)) != n:
        print(-1)
    else:
        print(num)
