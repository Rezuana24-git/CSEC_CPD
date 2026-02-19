m=list(map(int,input().split()))
arr=[]
for i in m:
    if i not in arr:
        arr.append(i)
s=len(arr)
print(4-s)
