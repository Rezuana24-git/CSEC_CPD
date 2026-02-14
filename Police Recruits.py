n=int(input())
m=list(map(int,input().split()))
hire=0
untreated=0
for i in m:
    if i>0:
        hire+=i
    else:
        if hire >0:
            hire-=1
        else:
            untreated+=1
print(untreated)
