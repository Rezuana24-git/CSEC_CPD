n=int(input())
for i in range(n):
    a=input()
    arr=[]
    for ch in range(len(a)-1, -1,-1):
        if a[ch] == 'p':
            arr.append('q')
        elif a[ch] == 'q':
            arr.append('p')
        else:
            arr.append('w')
    print(*arr,sep='')
